@echo off

echo Set java path. Use Minecraft Launcher java runtime. (java8)
set PATH=%PATH%;C:\Program Files (x86)\Minecraft Launcher\runtime\jre-legacy\windows-x64\jre-legacy\bin

echo Set Android Debug Bridge path. Use Unity SDK.
set PATH=%PATH%;C:\Program Files\Unity\Hub\Editor\2021.1.19f1\Editor\Data\PlaybackEngines\AndroidPlayer\SDK\platform-tools

echo;
echo %PATH%
