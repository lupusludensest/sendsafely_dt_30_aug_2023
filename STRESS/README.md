# Load Testing with Locust

This directory contains basic load testing scripts using the Locust framework.

## Setup and Running Instructions

### 0. Prerequisites
Navigate to the working directory:
```powershell
cd E:\Gurov_SSD_256\IT\Testing\Automation_08_09_2019\sendsafely_dt_30_aug_2023\STRESS
```

### 1. Environment Setup
Create and activate virtual environment:
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 2. Install Dependencies
Install Locust in the virtual environment:
```powershell
pip install locust
```

### 3. Running Tests

#### a) Web UI Mode (Recommended)
```powershell
locust -f test_load_stress_basic.py
```
Then press Enter to open your default browser:
1. Open http://localhost:8089 in your browser
2. Configure test parameters in the web interface:
   - Number of users to simulate
   - Spawn rate (users started per second)
   - Host URL to test
   - Advanced options (test duration, etc.)
3. Click "Start" to begin the test

#### b) Command Line Mode
With all parameters specified:
```powershell
locust -f test_load_stress_basic.py --host https://your-target-website.com --users 5000 --spawn-rate 20
```

#### c) Additional Options
Browser Interface Settings:
1. Number of users - How many virtual users to simulate
2. Rump up - How quickly to start new users (per second)
3. Host - The target URL you want to test
4. Advanced Options - Configure test duration and other parameters
5. Click "START"

Command Line Options:
- Run without web interface:
  ```powershell
  locust -f test_load_stress_basic.py --headless
  ```
- Show only summary stats:
  ```powershell
  locust -f test_load_stress_basic.py --only-summary
  ```

### 4. Saving Test Results
- Generate HTML report:
  ```powershell
  locust -f test_load_stress_basic.py --html=report.html
  ```
- Generate CSV results:
  ```powershell
  locust -f test_load_stress_basic.py --csv=results
  ```

### 5. Stopping the Test
- In web UI mode: Click "Stop" in the web interface
- In command line mode: Press Ctrl+C

### 6. Cleanup
Deactivate virtual environment when done:
```powershell
deactivate
```