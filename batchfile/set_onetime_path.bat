@echo off

echo Set java path. Use Minecraft Launcher java runtime. (java17)
set PATH=%PATH%;%LOCALAPPDATA%\packages\microsoft.4297127d64ec6_8wekyb3d8bbwe\localcache\local\runtime\java-runtime-beta\windows-x64\java-runtime-beta\bin

echo Set Android Debug Bridge path. Use Unity SDK.
set PATH=%PATH%;C:\Program Files\Unity\Hub\Editor\2021.1.22f1\Editor\Data\PlaybackEngines\AndroidPlayer\SDK\platform-tools

echo;
echo %PATH%
