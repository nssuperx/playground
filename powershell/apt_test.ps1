$res = Invoke-WebRequest -Uri https://api.papermc.io/v2/projects/paper/versions/1.19.4
Write-Output $res

$paperVersions = ConvertFrom-Json $res.Content

Write-Output $paperVersions