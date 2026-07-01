from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PIMPage

from utils.api_helper import EmployeeAPI
from utils.data_reader import load_employee_data


def test_employee_lifecycle(page: Page):

    employee_data = load_employee_data()

    login_page = LoginPage(page)
    dashboard_page = DashboardPage(page)
    pim_page = PIMPage(page)

    # Open application
    login_page.navigate()

    assert "login" in page.url.lower(), \
        f"Login page was not opened. Current URL: {page.url}"

    # Login
    login_page.login("Admin", "admin123")

    # Verify dashboard
    dashboard_page.verify_dashboard_loaded()

    # Open Add Employee page
    pim_page.open_add_employee_page()

    # Verify page loaded
    pim_page.verify_add_employee_page_loaded()

    # Add employee
    employee_id = pim_page.add_employee(
        employee_data["first_name"],
        employee_data["last_name"],
        employee_data["employee_id"],
        employee_data["profile_picture"]
    )

    assert employee_id == employee_data["employee_id"], \
        f"Unexpected employee ID returned. Expected '{employee_data['employee_id']}', got '{employee_id}'."

    # Verify employee created
    pim_page.verify_employee_created()

    # Employee List
    pim_page.open_employee_list()

    # Search employee
    pim_page.search_employee(employee_id)

    # Verify search result
    pim_page.verify_employee_found(employee_id)

    # Open employee record
    pim_page.edit_employee(employee_id)

    # Verify profile page
    pim_page.verify_employee_profile_opened()

    # Extract employee number from profile URL
    emp_number = page.url.split("/")[-1]

    assert emp_number, \
        "Employee Number could not be extracted from the profile URL."

    # Initialize API helper
    api = EmployeeAPI(page.context.request)

    # API validation - Verify employee created
    api.verify_employee_exists(
        emp_number,
        employee_id,
        employee_data["first_name"],
        employee_data["last_name"]
    )

    # Open Job tab
    pim_page.open_job_tab()

    # Verify Job tab
    pim_page.verify_employee_job_tab_opened()

    # Update job details through UI
    job_title, employment_status = pim_page.update_job_details()

    assert job_title == "QA Engineer", \
        f"Expected Job Title 'QA Engineer', but got '{job_title}'."

    assert employment_status == "Full-Time Permanent", \
        f"Expected Employment Status 'Full-Time Permanent', but got '{employment_status}'."

    # Verify updated in UI
    pim_page.verify_job_details_updated(
        job_title,
        employment_status
    )

    # Perform PUT request
    api.update_employee_job_details(emp_number)

    # Verify updated through API
    api.verify_job_details(
        emp_number,
        job_title,
        employment_status
    )

    # Open Employee List
    pim_page.open_employee_list()

    # Search employee
    pim_page.search_employee(employee_id)

    # Verify employee found
    pim_page.verify_employee_found(employee_id)

    # Click Delete button (do NOT confirm)
    pim_page.click_delete_employee(employee_id)

    # Delete employee through API
    api.delete_employee(emp_number)

    # Refresh page to sync UI with API
    page.reload()

    # Open Employee List
    pim_page.open_employee_list()

    # Search employee
    pim_page.search_employee(employee_id)

    # Verify employee deleted in UI
    pim_page.verify_employee_deleted(employee_id)

    # Verify employee deleted through API
    api.verify_employee_deleted(employee_id)

    # Logout
    login_page.logout()

    # Verify logout
    login_page.verify_logout_successful()

    # Verify session invalidated
    page.goto(
        "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    )

    assert "login" in page.url.lower(), \
        f"Session was still active after logout. Current URL: {page.url}"