@echo on


set /p "username= Username (Just type anything if you don't need to sign in) : "
set /p "password= Password (Just type anything if you don't need to sign in) : "

python ./downloader.py --username %1 %username% --password %2 %password%

cmd.exe

