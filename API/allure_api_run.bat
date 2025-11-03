@echo off
call "%~dp0..\venv_3.11\Scripts\activate.bat"

REM Run all tests in the API directory and generate Allure reports
pytest --alluredir="%~dp0allure_api_reports" "%~dp0."

REM Pause to keep the window open after execution (optional)
pause


