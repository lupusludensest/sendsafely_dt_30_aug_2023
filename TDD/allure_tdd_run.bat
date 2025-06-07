@echo off
call "%~dp0..\venv\Scripts\activate.bat"

REM Run all tests in the TDD directory and generate Allure reports
pytest --alluredir="%~dp0allure_tdd_reports" "%~dp0."

REM Pause to keep the window open after execution (optional)
pause


