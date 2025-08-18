import json
import argparse
import re


def split_version(version):
    if args.prefix:
        version = version.replace(args.prefix, '')
    tmp = version.split('-')
    build = int(tmp[1]) if len(tmp) == 2 else 0
    tmp = tmp[0].split('.')
    return (int(tmp[0]), int(tmp[1]), int(tmp[2]), build)


def check_max(versions, sprint=None):
    found = False
    max_v = [0, 1, 0, 0]
    if sprint:
        max_v[0] = int(sprint)
    for version in versions:
        if version == 'latest':
            continue
        major, minor, fix, build = split_version(version)
        if sprint and int(sprint) != major:
            continue
        if major < max_v[0] or (major == max_v[0] and minor < max_v[1]) or (major == max_v[0] and minor == max_v[1] and fix < max_v[2]) or (major == max_v[0] and minor == max_v[1] and fix == max_v[2] and build < max_v[3]):
            continue
        max_v = [major, minor, fix, build]
        found = True
    return (max_v, found)


def new_version(versions, u_type):
    old_version, found = check_max(versions, args.sprint)
    sprint = int(args.sprint) if args.sprint and u_type != 'sprint' else old_version[0]
    if found and u_type == 'sprint':
        v = '{}{}.{}.{}'.format(prefix, sprint, 1, 0)
    elif found and u_type == 'minor':
        v = '{}{}.{}.{}'.format(prefix, sprint, old_version[1]+1, 0)
    elif found and u_type in ['fix', 'releasefix']:
        v = '{}{}.{}.{}'.format(prefix, sprint,
                                   old_version[1], old_version[2]+1)
    else:
        v = '{}{}.{}.{}'.format(prefix, sprint, old_version[1], old_version[2])
    return v


def prepare_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--versions', '-v', nargs='*', required=True, help='version history of is tags')
    # parser.add_argument('--version-key', help='')
    parser.add_argument('--type', '-t', required=True,
                        choices=['sprint', 'minor', 'fix', 'release_fix'], help='Type of upgrade')
    parser.add_argument('--prefix', '-p', help='')
    parser.add_argument(
        '--sprint', help='Force the script to use the passed sprint number')
    return parser.parse_args()


args = prepare_args()

prefix = args.prefix if args.prefix else ""

# print("##DEBUG## [get_new_version.py] - input: args.versions - value:", args.versions)
if not args.versions:
    # print("ERROR - param 'versions' is empty, I can't calculate a new version")
    print("1.0.0")
else:    
    version_bc = new_version(args.versions, args.type)
    # print("##DEBUG## [get_new_version.py] - calculated new version - value:", version_bc)
    print(version_bc)


