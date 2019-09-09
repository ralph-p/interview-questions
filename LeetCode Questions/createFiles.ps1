$problemGroups = @()
$problemNames = @()


function Create-Files {
    param (
        [string]$pGroup,
        [string]$pName
    )
    New-Item -ItemType Directory -Path ".\$pGroup\$pName"
    New-Item -ItemType File -Path ".\$pGroup\$pName\index.js", ".\$pGroup\$pName\explanation.log"
    Set-Content -Path ".\$pGroup\$pName\explanation.log" -Value "Problem: `n`nSolution: `n`nTime: `n`nSpace `n"
}

$pGroup = "Matrix"
$pName = "Set Matrix Zeroes"

Create-Files $pGroup $pName
