@echo off
for %%f in (C:\Python27\Lib\site-packages\mathworks\*.py) do echo %%f... && copy /Y %%f C:\Users\Ryan\Documents\mathworks-git
pause > nul
exit