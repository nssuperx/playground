$folders = Get-ChildItem -Path . -Filter $Args[0] -Recurse -Directory -Force -ErrorAction SilentlyContinue

# https://qiita.com/sukakako/items/b9d4c10b75cf7c2fe965
$shell = New-Object -ComObject Shell.Application
$trash = $shell.NameSpace(10)

foreach ($folder in $folders) {
    Write-Host $folder.FullName
    $trash.MoveHere($folder.FullName)
}
