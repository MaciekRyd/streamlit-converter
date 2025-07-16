@echo off
echo Pobieranie zdalnych galezi z origin...
git fetch --all

for /f "delims=" %%b in ('git branch -r ^| findstr /v "HEAD"') do (
    set "branch=%%b"
    call :createBranch %%b
)

echo Gotowe!
goto :eof

:createBranch
setlocal
set "remoteBranch=%~1"
set "branchName=%remoteBranch:origin/=%"
for /f %%l in ('git branch --list %branchName%') do (
    endlocal
    goto :eof
)
echo Tworzenie lokalnej galezi: %branchName%
git branch --track %branchName% %remoteBranch% 2>nul
endlocal
goto :eof
