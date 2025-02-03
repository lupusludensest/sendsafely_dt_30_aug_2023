@echo off
call .venv\Scripts\activate
behave -f allure_behave.formatter:AllureFormatter -o allure_bdd_reports/ features/