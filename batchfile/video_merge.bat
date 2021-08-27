@ECHO OFF
cd /d %~dp1

set originalFileName=%~n1
set outFilePath=%originalFileName%-out.mp4

type nul > tmp.txt

for %%a in (%*) do (
echo file '%%~nxa' >> tmp.txt
)

ffmpeg -safe 0 -f concat -i tmp.txt -vcodec copy -acodec copy %outFilePath%
rem ffmpeg -safe 0 -f concat -i tmp.txt -vcodec copy -acodec copy out.mp4

del tmp.txt
