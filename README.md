# Selenium Automation Project

## Tech Stack
- Python 3.10+
- Selenium 4.21.0
- Pytest 8.2.0

## Setup

1. Install dependencies:
   pip install -r requirements.txt

2. Download ChromeDriver:
   https://chromedriver.chromium.org/

3. Add ChromeDriver to PATH

## Run Tests

pytest tests/

## Test Scenario

- Open SauceDemo
- Login with valid credentials
- Validate inventory page
- Open product
- Validate product title

## Notes

- Uses Page Object Model for maintainability
- Easy to scale for more tests

## Run 

- pip install -r requirements.txt
- pytest tests/
