      Get-ChildItem ./npm/ArmTemplate/*.json -recurse | ForEach-Object { (Get-Content $_.FullName) `
      -replace ('\b \b', '') `
      -replace ('\bdlmsfnex2010prdev\b', 'dlmsfnex2110prqa') `
      -replace ('\badb-4968596736585562.2\b', 'adb-5609439055045080.0') `
      -replace ('\29c98eb3-1108-49b3-9f5a-76a3e203abda\b', 'd16d4b04-d334-4dc5-8beb-0a207a31b71e') `
      -replace ('\keyvault-msfnex20-cx-dev\b', 'keyvault-msfnex21-cx-qa') `
      -replace ('\msfnex20-datalake-MS-GLB-Connexus-dev\b', 'msfnex21-datalake-MS-GLB-Connexus-qa') `
      -replace ('\cosmos-msfnex20-10-centralnode-glb-dev\b', 'cosmos-msfnex21-10-centralnode-glb-qa') `
      -replace ('\https://function-msfnex20-10-centralnode-dev.azurewebsites.net\b', 'https://function-msfnex21-10-centralnode-qa.azurewebsites.net') `
      | Set-Content  $_.FullName }
      Get-Content ./npm/ArmTemplate/ARMTemplateForFactory.json