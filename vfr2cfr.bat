@ECHO OFF
cd /d %~dp0
for %%a in (%*) do (
ffmpeg -i %%a -r 60 -vsync cfr -af aresample=async=1 -vcodec utvideo -acodec pcm_s16le "%%~dpna.avi"
)
pause