@echo off
echo 🔄 Usuwanie plików tymczasowych Pythona...

:: Usuń katalogi __pycache__
for /r %%i in (.) do (
    if exist "%%i\__pycache__" (
        echo Usuwam: %%i\__pycache__
        rmdir /s /q "%%i\__pycache__"
    )
)

:: Usuń pliki .pyc i .pyo
for /r %%i in (*.pyc *.pyo) do (
    echo Usuwam: %%i
    del /q "%%i"
)

:: Usuń foldery build i dist
if exist build (
    echo Usuwam folder: build
    rmdir /s /q build
)
if exist dist (
    echo Usuwam folder: dist
    rmdir /s /q dist
)
if exist *.egg-info (
    echo Usuwam pliki *.egg-info
    del /q *.egg-info
)

echo ✅ Czyszczenie zakończone.
pause
