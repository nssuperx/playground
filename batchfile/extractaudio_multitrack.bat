@ECHO OFF
setlocal ENABLEDELAYEDEXPANSION
cd /d %~dp0
for %%a in (%*) do (
    ffprobe %%a -hide_banner -show_entries format=nb_streams -of json > "%%~dpna_info.json"
    for /f "usebackq tokens=2 delims=: " %%b in (`findstr nb_streams "%%~dpna_info.json"`) do set STRM=%%b
    set /a NUM=!STRM!-1
    for /l %%i in (1, 1, !NUM!) do (
        ffmpeg -i %%a -map 0:%%i -vn -acodec copy "%%~dpna_%%i.m4a"
    )
    del "%%~dpna_info.json"
)
pause
