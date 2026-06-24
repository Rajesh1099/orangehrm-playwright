class EmployeeAPI:

    def __init__(self, request):
        self.request = request

    def get_all_employees(self):
        response = self.request.get("https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees")

        assert response.status == 200

        return response.json()
    
    def verify_employee_exists(self, emp_number, employee_id, first_name, last_name):
        response = self.request.get(
        f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees/{emp_number}")

        assert response.status == 200, "Employee API request failed"

        employee = response.json()["data"]

        assert employee["employeeId"] == employee_id, \
        f"Expected Employee ID '{employee_id}', got '{employee['employeeId']}'"

        assert employee["firstName"] == first_name, \
        f"Expected First Name '{first_name}', got '{employee['firstName']}'"

        assert employee["lastName"] == last_name, \
        f"Expected Last Name '{last_name}', got '{employee['lastName']}'"

    
    def verify_job_details(self, emp_number, expected_job_title, expected_status):
        response = self.request.get(f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees/{emp_number}/job-details")
        assert response.ok, "Job Details API request failed"

        data = response.json()["data"]

        actual_job_title = data["jobTitle"]["title"]
        actual_status = data["empStatus"]["name"]

        assert actual_job_title == expected_job_title, \
        f"Expected Job Title '{expected_job_title}', got '{actual_job_title}'"

        assert actual_status == expected_status, \
        f"Expected Employment Status '{expected_status}', got '{actual_status}'"    


    def verify_employee_deleted(self, employee_id):
        employees = self.get_all_employees()["data"]

        for employee in employees:
            if employee["employeeId"] == employee_id:
                assert False, f"Employee ID '{employee_id}' still exists in API response"
