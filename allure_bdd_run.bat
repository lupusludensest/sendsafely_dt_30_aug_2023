@echo off
mkdir allure_bdd_reports
"%~dp0.venv\Scripts\python.exe" -m behave -f allure_behave.formatter:AllureFormatter -o allure_bdd_reports/ features/