@echo off

set PROJECT_DIR=E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019\sendsafely_dt_30_aug_2023
set VENV_PYTHON=%PROJECT_DIR%\venv_3.11\Scripts\python.exe

REM Check if the directory exists; if not, create it
if not exist "%PROJECT_DIR%\TDD\allure_tdd_reports" (
    mkdir "%PROJECT_DIR%\TDD\allure_tdd_reports"
) else (
    echo "Directory allure_tdd_reports already exists."
)

REM Run pytest with Allure reporting
"%VENV_PYTHON%" -m pytest "%PROJECT_DIR%\TDD" --alluredir="%PROJECT_DIR%\TDD\allure_tdd_reports"

REM Pause to keep the window open
pause