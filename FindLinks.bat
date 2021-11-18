@echo on

set /p "source= Base url : "

python ./download.py --source %1 %source%

cmd.exe

