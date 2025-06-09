@echo off

REM Check if the directory exists; if not, create it
if not exist "allure_bdd_reports" (
    mkdir allure_bdd_reports
) else (
    echo "Directory allure_bdd_reports already exists."
)

REM Run behave with Allure formatter
"%~dp0.venv\Scripts\python.exe" -m behave -f allure_behave.formatter:AllureFormatter -o allure_bdd_reports features/