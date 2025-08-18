### UFS_GLO_Cn_01
$filename01="..\..\..\..\LogicApps\UFS_GLO_Cn_01\*.json"
Get-ChildItem  $filename01 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('workflows_UFS_GLO_Dev_Cn_01_name', 'workflows_UFS_GLO_PRD_Cn_01_name') `
-replace ('UFS_GLO_Dev_Cn_01', 'UFS_GLO_PRD_Cn_01') `
-replace ('\bbnlwestgunileverfr01054\b', 'bnlwestgunileverfr01118') `
-replace ('\bbnlwe-fr01-n-56690-PA01-rg\b', 'bnlwe-fr01-p-56626-PA01-rg') `
-replace ('\bFS_Dev_BlobConnection\b', 'FS_Prd_BlobConnection') `
| Set-Content  $_.FullName }

$initial=@'
"ITSG": "56690",
'@
$to=@'
"ITSG": "56626",
'@
Get-ChildItem  $filename01 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace "$initial", "$to" `
| Set-Content  $_.FullName }

### UFS_GLO_Cn_02

$filename02="..\..\..\..\LogicApps\UFS_GLO_Cn_02\*.json"
Get-ChildItem  $filename02 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('workflows_UFS_GLO_Dev_Cn_02_name', 'workflows_UFS_GLO_PRD_Cn_02_name') `
-replace ('UFS_GLO_Dev_Cn_02', 'UFS_GLO_PRD_Cn_02') `
-replace ('\bbnlwe-fr01-n-56690-PA01-rg\b', 'bnlwe-fr01-p-56626-PA01-rg') `
| Set-Content  $_.FullName }
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"ITSG": "56690",
'@
$to=@'
"ITSG": "56626",
'@
Get-ChildItem  $filename01 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace "$initial", "$to" `
| Set-Content  $_.FullName }
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

### UFS_GLO_Cn_03
$filename03="..\..\..\..\LogicApps\UFS_GLO_Cn_03\*.json"
Get-ChildItem  $filename03 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('workflows_UFS_GLO_Dev_Cn_03_name', 'workflows_UFS_GLO_PRD_Cn_03_name') `
-replace ('UFS_GLO_Dev_Cn_03', 'UFS_GLO_PRD_Cn_03') `
-replace ('bnlwe-fr01-d-56690-pa01-aasdb-dev-01', 'bnlwe-fr01-p-56626-pa01-aasdb-prd-01') `
-replace ('bnlwefr01d56690pa01aasdev01', 'bnlwefr01p56626pa01aasprd01') `
-replace ('\bbnlwe-fr01-n-56690-PA01-rg\b', 'bnlwe-fr01-p-56626-PA01-rg') `
| Set-Content  $_.FullName }

$initial=@'
"ITSG": "56690",
'@
$to=@'
"ITSG": "56626",
'@
Get-ChildItem  $filename01 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace "$initial", "$to" `
| Set-Content  $_.FullName }
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue