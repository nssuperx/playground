@ECHO OFF
cd /d %~dp0
for %%a in (%*) do (
lame -V0 %%a "%%~dpna.mp3"
)
