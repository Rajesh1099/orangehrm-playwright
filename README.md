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

## Tech Stack

* Python
* Playwright
* Pytest
* Requests
* Pytest HTML Report

---

## Framework Structure

```text
OrangeHRM_Project/

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
git clone <repository-url>
cd OrangeHRM_Project
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

---

## Features Implemented

* Page Object Model (POM)
* Data-Driven Testing using JSON
* API Validation
* HTML Reporting
* Video Recording
* Screenshot Capture on Failure
* Cross-browser Execution Support

