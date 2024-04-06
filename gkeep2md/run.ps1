# .\run.ps1 -dir <directory>
Param($dir)

go build

$files = Get-ChildItem $dir *.json
foreach($f in $files){
    .\gkeep2md.exe -f $f
}
