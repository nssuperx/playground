@echo off
rem set java path
set JAVA_HOME=%LOCALAPPDATA%\packages\microsoft.4297127d64ec6_8wekyb3d8bbwe\localcache\local\runtime\java-runtime-gamma\windows-x64\java-runtime-gamma

rem run
%JAVA_HOME%\bin\java.exe -jar %1 > nul
