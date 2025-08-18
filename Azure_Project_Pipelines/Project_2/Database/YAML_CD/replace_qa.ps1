### UFS_DM
Get-ChildItem ..\..\..\..\Database\UFS_DM\ *.sql -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('bnlwe_fr01_d_56690_pa01_sqldb_dev_01', 'bnlwe_fr01_n_56690_pa01_sqldb_lqa_01') `
-replace ('\bbnlwe-fr01-d-56690-pa01-sqldb-dev-02\b', 'bnlwe-fr01-n-56690-pa01-sqldb-lqa-02') `
-replace ('\bbnlwe-fr01-d-56690-pa01-sql-dev-01.database.windows.net\b', 'bnlwe-fr01-n-56690-pa01-sql-lqa-01.database.windows.net') `
| Set-Content  $_.FullName }


### UFS_DW

Get-ChildItem ..\..\..\..\Database\UFS_DW\ *.sql -recurse | ForEach-Object { (Get-Content $_.FullName) `
-replace ('bnlwe_fr01_d_56690_pa01_sqldb_dev_02', 'bnlwe_fr01_n_56690_pa01_sqldb_lqa_02') `
-replace ('\bbnlwe-fr01-d-56690-pa01-sqldb-dev-03\b', 'bnlwe-fr01-n-56690-pa01-sqldb-lqa-03') `
-replace ('\bbnlwe-fr01-d-56690-pa01-sql-dev-01.database.windows.net\b', 'bnlwe-fr01-n-56690-pa01-sql-lqa-01.database.windows.net') `
| Set-Content  $_.FullName }
