# SendSafely Testing Project

This project contains a comprehensive testing suite for SendSafely, implementing multiple testing approaches including TDD, BDD, API Testing, and Load Testing.

## Environment Setup (Updated June 8, 2025)
- Python 3.11 (using venv_3.11)
- Chrome Browser: Version 137.0.7151.69
- ChromeDriver: Version 137.0.7151.68 (local installation at C:\Webdrivers\chromedriver.exe)
- Tests configured for visible (non-headless) mode
- Standard resolution window size

## Project Structure

```
sendsafely_dt_30_aug_2023/
├── API/                  # API Testing suite
├── STRESS/              # Load Testing with Locust
├── TDD/                 # Test-Driven Development tests
├── features/           # Behavior-Driven Development (BDD) tests
│   ├── steps/         # Step definitions for BDD
│   └── tests/         # Feature files
├── pages/              # Page Object Models
└── app/                # Application core
```

## Testing Approaches

### 1. BDD (Behavior-Driven Development)
Located in `features/` directory.

#### Setup
1. Create and activate virtual environment:
```powershell
python -m venv venv_3.11
.\venv_3.11\Scripts\Activate.ps1
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
pip install pynput pyautogui  # Additional dependencies for UI automation
```

#### Running BDD Tests
Use the batch files in the root directory:
- .\allure_bdd_run.bat - Executes BDD tests
- .\allure_bdd_report.bat - Generates Allure report for BDD tests

Tests are organized in feature files:
- .\sendsafely_pytested_blue_top_1.feature
- .\sendsafely_pytested_bttns_clckd_2.feature
- .\sendsafely_pytested_sign_up_right_3.feature

### 2. TDD (Test-Driven Development)
Located in `TDD/` directory.

#### Running TDD Tests
Use the batch files in the TDD directory:
- .\allure_tdd_run.bat - Executes TDD tests
- .\allure_tdd_report.bat - Generates Allure report for TDD tests

Available tests:
- Blue top navigation tests
- Button click tests
- Sign up tests
- Security bug reporting tests

### 3. API Testing
Located in `API/` directory.

#### Running API Tests
Use the batch files in the API directory:
- .\allure_api_run.bat - Executes API tests
- .\allure_api_report.bat - Generates Allure report for API tests

Available tests:
- GET security text tests
- POST email tests

### 4. Load Testing (Stress Tests)
Located in `STRESS/` directory.

See [STRESS/README.md](STRESS/README.md) for detailed instructions on running load tests with Locust.

## Page Objects
Located in `pages/` directory:
- .\base_page.py - Base class with common functionality
- .\main_page.py - Main page specific elements and actions
- .\all_locators_bdd.py - Locators for BDD tests
- .\all_locators_tdd.py - Locators for TDD tests

## Getting Started

1. Clone the repository
2. Create and activate virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Choose your testing approach:
   - For BDD: Run .\allure_bdd_run.bat
   - For TDD: Run .\allure_tdd_run.bat
   - For API: Run .\allure_api_run.batC:\Users\rapid\test_send_bug_report.jpg
   - For Load Testing: Follow instructions in STRESS/README.md

5. View test results:
   - For BDD: Run .\allure_bdd_report.bat
   - For TDD: Run .\allure_tdd_report.bat
   - For API: Run .\allure_api_report.bat
   - For Load Testing: Check generated HTML/CSV reports

## Requirements
See `requirements.txt` for all Python dependencies.

## Recent Updates (June 8, 2025)
- Fixed ChromeDriver configuration and path settings
- Updated browser window size for better test stability
- Corrected virtual environment paths in batch files
- Fixed TDD test runner configuration
- Added proper error handling for test assets
- Updated dependencies to include UI automation tools

## Notes
- Make sure to activate the virtual environment before running any tests
- Allure framework is required for viewing test reports
- Each testing approach has its own set of locators and configurations
- Load testing requires separate setup as described in STRESS/README.md
- ChromeDriver is now configured locally instead of using WebDriver Manager
- Tests run in visible mode for better debugging
- Window size standardized for consistent UI testing