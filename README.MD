# Python API test framework

## Requirements
Python 3.8 — https://www.python.org/downloads/

## Installation
1. Install Python 3.8
2. Create new virtual environment (https://docs.python.org/3/library/venv.html) and use package manager pip to install all requirements: ```pip install -r requirements.txt```;
3. Follow this guide to install Allure (required to generate reports) — https://docs.qameta.io/allure/#_get_started


## Run your tests
Run tests:
- Single-thread — execute command `pytest tests/` to run all tests in 1 thread.

Run tests and generate report:
- Execute command `pytest tests/ --alluredir=./allure_results` to run all tests and generate Allure report files in directory `./allure_reports`. To run human-readable Allure report, execute command from the same directory `allure serve ./allure_results`.    
