$srcDir = "."
$timeDiffSeconds = 30

Push-Location $srcDir

New-Item ".\merged" -ItemType Directory
$files = Get-ChildItem .\* -Include *.mp4 | Sort-Object -Property Name
$format = "yyyyMMddHHmmss"
$isContinuous = $false
$firstFileName = ""
$mergedDir = ""

for ($i = 0; $i -lt $files.Count; $i++) {
    $file = $files[$i].Name
    $timediff = $timeDiffSeconds + 1
    if ($i + 1 -lt $files.Count) {
        $nextFile = $files[$i + 1].Name
        # ファイル名から日時部分を抽出
        # Geminiで生成
        $dateTime1 = [datetime]::ParseExact($file.Substring(0, $format.Length), $format, $null)
        $dateTime2 = [datetime]::ParseExact($nextFile.Substring(0, $format.Length), $format, $null)
        $timeDiff = New-TimeSpan -Start $dateTime1 -End $dateTime2
    }

    if ($timeDiff.TotalSeconds -le $timeDiffSeconds) {
        if (!$isContinuous) {
            $firstFileName = [System.IO.Path]::GetFileNameWithoutExtension($file)
            $mergedDir = ".\merged\$firstFileName"
            New-Item $mergedDir -ItemType Directory
            New-Item -Path "tmp.txt" -ItemType File -Force
        }
        $isContinuous = $true
        Move-Item "$file" "$mergedDir\$file"
        Add-Content -Path "tmp.txt" -Value "file '$mergedDir\$file'"
    }
    elseif ($isContinuous) {
        Move-Item "$file" "$mergedDir\$file"
        Add-Content -Path "tmp.txt" -Value "file '$mergedDir\$file'"
        $isContinuous = $false
        ffmpeg -safe 0 -f concat -i tmp.txt -vcodec copy -acodec copy "$firstFileName-out.mp4"
        Remove-Item "tmp.txt"
    }
}

Remove-Item "tmp.txt"
Pop-Location
