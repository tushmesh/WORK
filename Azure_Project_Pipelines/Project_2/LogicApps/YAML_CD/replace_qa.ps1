### UFS_GLO_Cn_01
$filename01="..\..\..\..\LogicApps\UFS_GLO_Cn_01\template.json"
Get-ChildItem  $filename01 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('workflows_UFS_GLO_Dev_Cn_01_name', 'workflows_UFS_GLO_QA_Cn_01_name') `
-replace ('UFS_GLO_Dev_Cn_01', 'UFS_GLO_QA_Cn_01') `
-replace ('connections_azureblob_1_externalid', 'connections_azureblob_3_externalid') `
-replace ('connections_sql_4_externalid', 'connections_sql_5_externalid') `
-replace ('connections_sql_3_externalid', 'connections_sql_6_externalid') `
-replace ('\bsql-4\b', 'sql-5') `
-replace ('\bazureblob-1\b', 'azureblob-3') `
-replace ('\bsql-3\b', 'sql-6') `
-replace ('\bazureblob_1\b', 'azureblob') `
-replace ('\bbnlwestgunileverfr01054\b', 'bnlwestgunileverfr01115') `
| Set-Content  $_.FullName }

$initial=@'
"name": "@parameters('$connections')['sql']['connectionId']"
'@
$to=@'
"name": "@parameters('$connections')['sql_3']['connectionId']"
'@
(Get-Content $filename01).Replace($initial,$to)| Set-Content $filename01
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

########

$initial=@'
"name": "@parameters('$connections')['sql_1']['connectionId']"
'@
$to=@'
"name": "@parameters('$connections')['sql_2']['connectionId']"
'@
(Get-Content $filename01).Replace($initial,$to)| Set-Content $filename01
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

########

$initial=@'
"connectionId": "[parameters('connections_sql_4_externalid')]",
'@
$to=@'
"connectionId": "[parameters('connections_sql_5_externalid')]",
'@
(Get-Content $filename01).Replace($initial,$to)| Set-Content $filename01
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

####

$initial=@'
"connectionId": "[parameters('connections_sql_4_externalid')]",
'@
$to=@'
"connectionId": "[parameters('connections_sql_5_externalid')]",
'@
(Get-Content $filename01).Replace($initial,$to)| Set-Content $filename01
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

########

$initial=@'
"connectionId": "[parameters('connections_sql_3_externalid')]",
'@
$to=@'
"connectionId": "[parameters('connections_sql_6_externalid')]",
'@
(Get-Content $filename01).Replace($initial,$to)| Set-Content $filename01
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"sql_1": {
'@
$to=@'
"sql_3": {
'@
(Get-Content $filename01).Replace($initial,$to)| Set-Content $filename01
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

###

$initial=@'
"sql": {
'@
$to=@'
"sql_2": {
'@
(Get-Content $filename01).Replace($initial,$to)| Set-Content $filename01
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

### UFS_GLO_Cn_02

$filename02="..\..\..\..\LogicApps\UFS_GLO_Cn_02\template.json"
Get-ChildItem  $filename02 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('workflows_UFS_GLO_Dev_Cn_02_name', 'workflows_UFS_GLO_QA_Cn_02_name') `
-replace ('UFS_GLO_Dev_Cn_02', 'UFS_GLO_QA_Cn_02') `
-replace ('connections_sql_3_externalid', 'connections_sql_5_externalid') `
-replace ('connections_sql_4_externalid', 'connections_sql_6_externalid') `
-replace ('\bsql-3\b', 'sql-5') `
-replace ('\bsql-4\b', 'sql-6') `
| Set-Content  $_.FullName }

$initial=@'
"name": "@parameters('$connections')['sql_1']['connectionId']"
'@
$to=@'
"name": "@parameters('$connections')['sql_3']['connectionId']"
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"name": "@parameters('$connections')['sql']['connectionId']"
'@
$to=@'
"name": "@parameters('$connections')['sql_2']['connectionId']"
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"sql": {
'@
$to=@'
"sql_2": {
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"connectionName": "sql-3",
'@
$to=@'
"connectionName": "sql-5",
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"sql_1": {
'@
$to=@'
"sql_3": {
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"connectionId": "[parameters('connections_sql_4_externalid')]",
'@
$to=@'
"connectionId": "[parameters('connections_sql_6_externalid')]",
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"connectionId": "[parameters('connections_sql_3_externalid')]",
'@
$to=@'
"connectionId": "[parameters('connections_sql_5_externalid')]",
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"connectionName": "sql-4",
'@
$to=@'
"connectionName": "sql-6",
'@
(Get-Content $filename02).Replace($initial,$to)| Set-Content $filename02
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

### UFS_GLO_Cn_03
$filename03="..\..\..\..\LogicApps\UFS_GLO_Cn_03\template.json"
Get-ChildItem  $filename03 -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('workflows_UFS_GLO_Dev_Cn_03_name', 'workflows_UFS_GLO_QA_Cn_03_name') `
-replace ('UFS_GLO_Dev_Cn_03', 'UFS_GLO_QA_Cn_03') `
-replace ('connections_sql_externalid', 'connections_sql_7_externalid') `
-replace ('bnlwe-fr01-d-56690-pa01-aasdb-dev-01', 'bnlwe-fr01-n-56690-pa01-aasdb-lqa-01') `
-replace ('bnlwefr01d56690pa01aasdev01', 'bnlwefr01n56690pa01aaslqa01') `
| Set-Content  $_.FullName }

$initial=@'
"name": "@parameters('$connections')['sql_2']['connectionId']"
'@
$to=@'
"name": "@parameters('$connections')['sql_1']['connectionId']"
'@
(Get-Content $filename03).Replace($initial,$to)| Set-Content $filename03
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"name": "@parameters('$connections')['sql']['connectionId']"
'@
$to=@'
"name": "@parameters('$connections')['sql_1']['connectionId']"
'@
(Get-Content $filename03).Replace($initial,$to)| Set-Content $filename03
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"sql": {
'@
$to=@'
"sql_1": {
'@
(Get-Content $filename03).Replace($initial,$to)| Set-Content $filename03
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"connectionId": "[parameters('connections_sql_externalid')]",
'@
$to=@'
"connectionId": "[parameters('connections_sql_7_externalid')]",
'@
(Get-Content $filename03).Replace($initial,$to)| Set-Content $filename03
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"connectionName": "sql",
'@
$to=@'
"connectionName": "sql-7",
'@
(Get-Content $filename03).Replace($initial,$to)| Set-Content $filename03
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
Microsoft.Web/connections/sql",
'@
$to=@'
Microsoft.Web/connections/sql-7",
'@
(Get-Content $filename03).Replace($initial,$to)| Set-Content $filename03
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue

$initial=@'
"sql_2": {
'@
$to=@'
"sql_1": {
'@
(Get-Content $filename03).Replace($initial,$to)| Set-Content $filename03
Remove-Variable to -ErrorAction SilentlyContinue
Remove-Variable initial -ErrorAction SilentlyContinue