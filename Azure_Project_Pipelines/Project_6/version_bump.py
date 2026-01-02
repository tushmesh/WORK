#!/usr/bin/env python3
"""
Semantic Version Bumping Script
Handles branch-specific versioning with conventional commits
Only release, qlt and prod branches create tags - all others are treated as development
"""

import os
import re
import subprocess
import sys
from typing import Optional, Tuple


class VersionBumper:
    def __init__(self, repo_name: str, branch_name: str, access_token: str, commit_message: str):
        self.repo_name = repo_name
        self.branch_name = branch_name
        self.access_token = access_token
        self.commit_message = commit_message
        self.branch_prefix = None
        self.target_prefix = None
        
        # Determine the actual repository path
        self.repo_path = self.find_repo_path(repo_name)
    
    def find_repo_path(self, repo_name: str) -> str:
        """Find the repository path - handles different working directories"""
        possible_paths = [
            repo_name,  # Relative path
            os.path.join(os.getcwd(), repo_name),  # Current dir + repo
            os.path.join(os.environ.get('BUILD_SOURCESDIRECTORY', ''), repo_name)  # Azure build dir
        ]
        
        for path in possible_paths:
            if os.path.exists(path) and os.path.isdir(path):
                print(f"Found repository at: {path}")
                return path
        
        # If not found, check current directory
        if os.path.exists('.git'):
            print("Using current directory as repository")
            return os.getcwd()
        
        raise FileNotFoundError(f"Could not find repository: {repo_name}")
    
    def run_command(self, cmd: str, check: bool = True) -> str:
        """Execute shell command and return output"""
        try:
            # Use stdout and stderr parameters for compatibility with older Python
            result = subprocess.run(
                cmd, 
                shell=True, 
                stdout=subprocess.PIPE, 
                stderr=subprocess.PIPE, 
                text=True, 
                check=check
            )
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Command failed: {cmd}")
            print(f"Error: {e.stderr.decode() if isinstance(e.stderr, bytes) else e.stderr}")
            if check:
                raise
            return ""
    
    def setup_git(self):
        """Configure git with proper credentials"""
        self.run_command(f'git config user.email "azure-pipelines@{self.repo_name}"')
        self.run_command('git config user.name "Azure Pipelines"')
        self.run_command(f'git config http.extraheader "AUTHORIZATION: bearer {self.access_token}"')
        self.run_command("git fetch --all --tags --force")
    
    def parse_branch_info(self):
        """Extract branch prefix and target environment"""
        # Clean branch name (remove refs/heads/)
        branch_clean = self.branch_name.replace("refs/heads/", "")
        
        # Versioned branches - these create tags
        versioned_branches = {
            "release": "release", 
            "staging": "release",
            "qlt": "qlt",  # Quality branch - same as release
            "quality": "qlt",
            "main": "prod",
            "master": "prod",
            "prod": "prod",
            "production": "prod"
        }
        
        # Handle hotfix branches separately
        if branch_clean.startswith("hotfix/"):
            self.branch_prefix = "hotfix"
            target_branch = branch_clean.replace("hotfix/", "")
            self.target_prefix = versioned_branches.get(target_branch, "release")
        elif branch_clean in versioned_branches:
            # This is a versioned branch (release, qlt, or prod)
            self.branch_prefix = versioned_branches[branch_clean]
            self.target_prefix = self.branch_prefix
        else:
            # All other branches are development (no versioning)
            self.branch_prefix = "dev"
            self.target_prefix = "dev"
        
        print(f"Branch: {branch_clean}")
        print(f"Using prefix: {self.branch_prefix}")
        if self.branch_prefix == "hotfix":
            print(f"Hotfix target: {self.target_prefix}")
    
    def get_latest_tag(self, prefix: str) -> Optional[str]:
        """Get the latest semantic version tag for given prefix"""
        tags_output = self.run_command(f'git tag -l "{prefix}-*"', check=False)
        if not tags_output:
            return None
        
        tags = tags_output.split('\n')
        # Sort semantically (handles v1.10.0 > v1.9.0 correctly)
        def version_key(tag):
            # Extract version numbers from tag
            version_part = tag.split('-')[-1] if '-' in tag else tag
            numbers = re.findall(r'\d+', version_part)
            return [int(num) for num in numbers]
        
        tags.sort(key=version_key)
        return tags[-1] if tags else None
    
    def parse_version(self, version_str: str) -> Tuple[int, int, int]:
        """Parse version string into major, minor, patch components"""
        if not version_str or version_str == "0.0.0":
            return 0, 0, 0
        
        try:
            parts = version_str.split('.')
            major = int(parts[0]) if len(parts) > 0 else 0
            minor = int(parts[1]) if len(parts) > 1 else 0
            patch = int(parts[2]) if len(parts) > 2 else 0
            return major, minor, patch
        except (ValueError, IndexError):
            print(f"Warning: Could not parse version '{version_str}', using 0.0.0")
            return 0, 0, 0
    
    def determine_base_version(self) -> Tuple[str, Optional[str]]:
        """Determine the base version to start from"""
        # For dev branches, skip version determination entirely
        if self.branch_prefix == "dev":
            return "0.0.0", None
            
        latest_branch_tag = self.get_latest_tag(self.branch_prefix)
        
        # SPECIAL CASE: Release or QLT branch with no existing tags - start fresh from 1.0.0
        if self.branch_prefix in ["release", "qlt"] and not latest_branch_tag:
            print(f"First {self.branch_prefix} - starting fresh from 1.0.0")
            return "1.0.0", None
        
        # Hotfix branch logic
        if self.branch_prefix == "hotfix":
            latest_target_tag = self.get_latest_tag(self.target_prefix)
            if latest_target_tag:
                base_version = latest_target_tag.replace(f"{self.target_prefix}-", "")
                print(f"Hotfix for {self.target_prefix}. Using base version: {base_version}")
                return base_version, latest_target_tag
            return "0.0.0", None
        
        # Normal branch logic (for prod and existing release/qlt tags)
        if latest_branch_tag:
            base_version = latest_branch_tag.replace(f"{self.branch_prefix}-", "")
            print(f"Latest {self.branch_prefix} tag: {latest_branch_tag}")
            return base_version, latest_branch_tag
        
        # For prod branch with no existing tags, use the highest version from release or qlt
        if self.branch_prefix == "prod":
            # Check both release and qlt branches for the latest version
            latest_release_tag = self.get_latest_tag("release")
            latest_qlt_tag = self.get_latest_tag("qlt")
            
            # Determine which version is higher
            release_version = self.parse_version(latest_release_tag.replace("release-", "") if latest_release_tag else "0.0.0")
            qlt_version = self.parse_version(latest_qlt_tag.replace("qlt-", "") if latest_qlt_tag else "0.0.0")
            
            # Compare versions to find the highest
            if latest_release_tag and latest_qlt_tag:
                if release_version > qlt_version:
                    base_version = latest_release_tag.replace("release-", "")
                    print(f"Using latest release version as base: {base_version}")
                else:
                    base_version = latest_qlt_tag.replace("qlt-", "")
                    print(f"Using latest qlt version as base: {base_version}")
            elif latest_release_tag:
                base_version = latest_release_tag.replace("release-", "")
                print(f"Using latest release version as base: {base_version}")
            elif latest_qlt_tag:
                base_version = latest_qlt_tag.replace("qlt-", "")
                print(f"Using latest qlt version as base: {base_version}")
            else:
                base_version = "0.0.0"
            
            return base_version, None
        
        print(f"No {self.branch_prefix} tag found. Starting from: 0.0.0")
        return "0.0.0", None
    
    def analyze_commit_message(self) -> str:
        """Determine version bump type based on commit message"""
        message = self.commit_message.lower()
        
        # Major version triggers
        if any(pattern in message for pattern in ["breaking change", "chore!", "feat!"]):
            return "major"
        # Minor version triggers  
        elif "feat" in message:
            return "minor"
        # Default to patch
        else:
            return "patch"
    
    def calculate_next_version(self, base_version: str, has_existing_tag: bool) -> Tuple[str, str]:
        """Calculate the next version based on branch rules and commit message"""
        # ALL development branches (dev prefix) skip versioning
        if self.branch_prefix == "dev":
            print("Skipping version bump in development branch - no tags will be created")
            return None, "SKIP"
        
        major, minor, patch = self.parse_version(base_version)
        bump_type = self.analyze_commit_message()
        
        print(f"Current version: {major}.{minor}.{patch}")
        print(f"Commit message indicates: {bump_type} bump")
        
        # Branch-specific rules
        if self.branch_prefix in ["release", "qlt"]:
            if not has_existing_tag:
                # FIRST RELEASE/QLT: Use the fresh start version (1.0.0)
                return base_version, "INITIAL"
            else:
                # EXISTING RELEASE/QLT: Follow semantic versioning
                if bump_type == "major":
                    return f"{major + 1}.0.0", "MAJOR"
                elif bump_type == "minor":
                    return f"{major}.{minor + 1}.0", "MINOR"
                else:
                    return f"{major}.{minor}.{patch + 1}", "PATCH"
        
        elif self.branch_prefix == "prod":
            if not has_existing_tag:
                # FIRST PROD RELEASE: Use exact version from release/qlt
                return f"{major}.{minor}.{patch}", "INITIAL"
            else:
                if bump_type == "major":
                    return f"{major + 1}.0.0", "MAJOR"
                else:
                    return f"{major}.{minor}.{patch + 1}", "PATCH"
        
        elif self.branch_prefix == "hotfix":
            if bump_type in ["major", "minor"]:
                raise ValueError("Breaking changes or new features not allowed in hotfix branches!")
            return f"{major}.{minor}.{patch + 1}", "HOTFIX"
        
        else:
            # Safety net - should never reach here for dev branches
            print(f"Skipping version bump in {self.branch_prefix} branch")
            return None, "SKIP"
    
    def create_and_push_tag(self, new_tag: str):
        """Create and push the new git tag"""
        # Check if tag exists
        tag_exists = self.run_command(f'git show-ref --tags "{new_tag}"', check=False)
        
        if tag_exists:
            print(f"Warning: Tag {new_tag} already exists. Using existing tag.")
        else:
            # Create and push new tag
            self.run_command(f'git tag "{new_tag}"')
            self.run_command(f'git push origin "{new_tag}"')
            print(f"Successfully created tag: {new_tag}")
        
        # Set Azure DevOps variables
        print(f"##vso[task.setvariable variable=RELEASE_VERSION]{new_tag}")
        print(f"##vso[build.updatebuildnumber]{new_tag}")
    
    def run(self):
        """Main execution method"""
        print("=== Starting Version Bump ===")
        print(f"Repository: {self.repo_name}")
        print(f"Repo Path: {self.repo_path}")
        print(f"Branch: {self.branch_name}")
        print(f"Commit Message: {self.commit_message}")
        print(f"Current Working Directory: {os.getcwd()}")
        
        try:
            # Change to repo directory using absolute path
            os.chdir(self.repo_path)
            print(f"Changed to: {os.getcwd()}")
            
            # Setup and process
            self.setup_git()
            self.parse_branch_info()
            
            # Skip early for development branches
            if self.branch_prefix == "dev":
                print("=== Version Bump Skipped (Development Branch) ===")
                return
                
            base_version, latest_tag = self.determine_base_version()
            has_existing_tag = latest_tag is not None
            
            next_version, bump_type = self.calculate_next_version(base_version, has_existing_tag)
            
            # Skip if no version calculated
            if next_version is None:
                print("=== Version Bump Skipped ===")
                return
            
            # Determine final tag name
            if self.branch_prefix == "hotfix":
                new_tag = f"{self.target_prefix}-{next_version}"
            else:
                new_tag = f"{self.branch_prefix}-{next_version}"
            
            print(f"Bumping {bump_type} version from {base_version} to: {next_version}")
            print(f"New tag: {new_tag}")
            
            # Create and push tag
            self.create_and_push_tag(new_tag)
            
            print("=== Version Bump Complete ===")
            
        except Exception as e:
            print(f"ERROR: {str(e)}")
            sys.exit(1)


def main():
    if len(sys.argv) != 5:
        print("Usage: python version_bump.py <reponame> <branchname> <accesstoken> <commit_message>")
        sys.exit(1)
    
    repo_name, branch_name, access_token, commit_message = sys.argv[1:5]
    
    bumper = VersionBumper(repo_name, branch_name, access_token, commit_message)
    bumper.run()


if __name__ == "__main__":
    main()