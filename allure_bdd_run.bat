@echo off
mkdir allure_bdd_reports
call "%~dp0.venv\Scripts\activate"
python -m behave -f allure_behave.formatter:AllureFormatter -o allure_bdd_reports/ features/