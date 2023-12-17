@ECHO OFF
cd /d %~dp0
@REM 32 40 48 56 64 80 96 112 128 160 192 224 256 320
set bitrate=192
for %%a in (%*) do (
lame -b %bitrate% %%a "%%~dpna.mp3"
)
