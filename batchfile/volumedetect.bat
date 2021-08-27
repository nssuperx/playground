@ECHO OFF
cd /d %~dp0
ffmpeg -i %1 -vn -af volumedetect -f null -
pause