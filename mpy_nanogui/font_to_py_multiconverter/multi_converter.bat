@echo off
setlocal enabledelayedexpansion

echo Passed files:


for %%F in (%*) do (
    echo %%F

    set "ttf_file=%%~fF"

    set "filename=%%~nF"

    :: Convert - to _
    set "safe_filename=!filename:-=_!"

    set "out_dir=!safe_filename!_pyfont"

    if not exist "!out_dir!" (
        mkdir "!out_dir!"
    )

    :: Enter font sizes here
    for %%S in (10 12 15 18 20 22 25 28 30 32 35 40 45 50) do (
        set "out_file=!out_dir!\!safe_filename!_%%S.py"
        echo Konvertiere: !ttf_file! ? !out_file!
        python font_to_py.py "!ttf_file!" %%S "!out_file!"
    )
)

pause