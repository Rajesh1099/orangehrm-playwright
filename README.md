# OrangeHRM Employee Lifecycle Automation

## Overview

This project automates the Employee Lifecycle Management workflow in OrangeHRM using Playwright, Pytest, and Python.

The automation covers employee creation, employee update, API validation, employee deletion, and logout functionality using a Page Object Model (POM) framework.

---

## Test Scenario Covered

The automated workflow includes:

* Login with valid admin credentials
* Add a new employee using JSON test data
* Upload employee profile picture
* Search and verify created employee
* Update Job Title and Employment Status
* Validate employee information through API
* Delete employee record
* Verify employee deletion
* Logout from the application

---

## API Testing and Enhancements

This project also includes validation improvements to make the employee lifecycle flow more reliable and easier to review:

* API helper methods support `GET`, `PUT`, and `DELETE` requests for employee data verification.
* The main test cross-checks UI actions with API responses to confirm employee creation, job updates, and deletion state.
* Assertions include clear failure messages so each step is easier to diagnose when something breaks.
* The test flow is ordered to match the lifecycle sequence: create, validate, update, validate, delete, and verify removal.

---

## Tech Stack

- Python
- Playwright
- Pytest
- pytest-playwright
- Requests (Playwright APIRequestContext)
- pytest-html

---

## Framework Structure

```text
orangehrm-playwright/

├── pages/
│   ├── login_page.py
│   ├── dashboard_page.py
│   └── pim_page.py

├── tests/
│   └── test_employee_lifecycle.py

├── utils/
│   ├── api_helper.py
│   └── data_reader.py

├── testdata/
│   ├── employee.json
│   └── profile.png

├── reports/
├── screenshots/
├── videos/

├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Setup

### Clone Repository

```bash
git clone https://github.com/Rajesh1099/orangehrm-playwright.git
cd orangehrm-playwright
```

### Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux / Mac

```bash
python -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## Test Data

Employee test data is maintained in:

```text
testdata/employee.json
```

Sample:

```json
{
  "first_name": "Rajesh",
  "last_name": "Lingampalli",
  "employee_id": "254862",
  "profile_picture": "testdata/profile.png"
}
```

---

## Execution

Run all tests:

```bash
pytest -v
```

Run with browser visible:

```bash
pytest -v --headed
```

Run in slow mode:

```bash
pytest -v --headed --slowmo 500
```

Run using Chromium:

```bash
pytest -v --browser chromium
```

---

## Reports and Artifacts

After execution, the following artifacts are generated:

### HTML Report

```text
reports/report.html
```

### Video Recording

```text
videos/
```

### Failure Screenshots

```text
screenshots/
```

Screenshots are automatically captured when a test fails.

The test configuration is set up to record videos during execution and generate an HTML report at the end of the run.

---

## Features Implemented

* Page Object Model (POM)
* Data-Driven Testing using JSON
* API Validation
* API-assisted cross-checking of UI data
* Descriptive assertions with clear failure messages
* HTML Reporting
* Video Recording
* Screenshot Capture on Failure
* Cross-browser Execution Support

