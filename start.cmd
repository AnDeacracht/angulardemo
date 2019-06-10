@echo off
START /B CMD /C CALL "cmd /c start angulardemo-frontend\src\startclient.cmd"
START /B CMD /C CALL "cmd /c start angulardemo\startserver.cmd"
pause