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

    # Verify employee created
    pim_page.verify_employee_created()

    # Employee List
    pim_page.open_employee_list()

    # Search employee
    pim_page.search_employee(employee_id)

    # Verify search result
    pim_page.verify_employee_found(employee_id)

    # Open employee record
    pim_page.open_employee_record()

    # Verify profile page
    pim_page.verify_employee_profile_opened()

    #Extract employee number from profile URL
    emp_number = page.url.split("/")[-1]
   
    # Open Job tab
    pim_page.open_job_tab()

    # Verify Job tab
    pim_page.verify_employee_job_tab_opened()

    # Update job details
    job_title, employment_status = pim_page.update_job_details()

    # Verify employee details exist/updated correctly in UI.
    pim_page.verify_job_details_updated(job_title, employment_status)

    # API validation - Verify employee details exist/updated correctly
    api = EmployeeAPI(page.context.request)
    api.verify_employee_exists(emp_number,employee_id, employee_data["first_name"], employee_data["last_name"])
    api.verify_job_details(emp_number, job_title, employment_status)

    #deleting the employee
    
    # Employee List
    pim_page.open_employee_list()

    # Search employee
    pim_page.search_employee(employee_id)

    # Verify search result
    pim_page.verify_employee_found(employee_id)

    # Delete employee
    pim_page.delete_employee()

    # Verify employee details are deleted successfully in UI.
    pim_page.verify_employee_deleted(employee_id)

    # API validation - Verify employee details are deleted
    api.verify_employee_deleted(employee_id)

    # Logout
    login_page.logout()

    # Verify logout
    login_page.verify_logout_successful()

    # Verify session invalidated
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
    
    assert "login" in page.url.lower(), \
    f"Session still active. Current URL: {page.url}"

