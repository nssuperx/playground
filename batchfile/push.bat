@echo off
cd /d %~dp0
robocopy unity Z:\unity /s /mir /xo /l /r:1
choice /m "同期してもいいですか(local to server)"
if not %errorlevel%==1 (
    goto end
)
echo 同期します(local to server)
robocopy unity Z:\unity /s /mir /xo /r:1

:end
echo 終了します
pause
