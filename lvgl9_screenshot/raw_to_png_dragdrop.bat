@echo off
setlocal

if "%~1"=="" (
    echo Bitte eine .raw-Datei auf diese Batch-Datei ziehen.
    echo.
    pause
    exit /b 1
)

set "RAW_FILE=%~1"
set "META_FILE=%RAW_FILE%.txt"
set "SCRIPT_DIR=%~dp0"
set "PY_SCRIPT=%SCRIPT_DIR%raw_to_png.py"

if not exist "%PY_SCRIPT%" (
    echo Python-Skript nicht gefunden:
    echo %PY_SCRIPT%
    echo.
    pause
    exit /b 1
)

if not exist "%META_FILE%" (
    echo Metadatendatei nicht gefunden:
    echo %META_FILE%
    echo.
    echo Erwartet wird eine Datei mit Namen:
    echo %~nx1.txt
    echo.
    pause
    exit /b 1
)

python "%PY_SCRIPT%" "%RAW_FILE%" "%META_FILE%"

echo.
pause
