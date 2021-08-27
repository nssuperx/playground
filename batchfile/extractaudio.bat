@ECHO OFF
cd /d %~dp0
for %%a in (%*) do (
ffmpeg -i %%a -vn -acodec copy "%%~dpna.ogg"
)
