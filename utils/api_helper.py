class EmployeeAPI:

    def __init__(self, request):
        self.request = request

    def get_all_employees(self):
        response = self.request.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees"
        )

        assert response.status == 200, \
            "Failed to fetch employee list from API."

        return response.json()

    def verify_employee_exists(self, emp_number, employee_id, first_name, last_name):

        response = self.request.get(
            f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees/{emp_number}"
        )

        assert response.status == 200, \
            "Employee API request failed."

        employee_data = response.json()["data"]

        assert employee_data["employeeId"] == employee_id, \
            f"Expected Employee ID '{employee_id}', got '{employee_data['employeeId']}'."

        assert employee_data["firstName"] == first_name, \
            f"Expected First Name '{first_name}', got '{employee_data['firstName']}'."

        assert employee_data["lastName"] == last_name, \
            f"Expected Last Name '{last_name}', got '{employee_data['lastName']}'."

    def verify_job_details(self, emp_number, expected_job_title, expected_status):

        response = self.request.get(
            f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees/{emp_number}/job-details"
        )

        assert response.status == 200, \
            "Job Details API request failed."

        job_details = response.json()["data"]

        actual_job_title = job_details["jobTitle"]["title"]
        actual_status = job_details["empStatus"]["name"]

        assert actual_job_title == expected_job_title, \
            f"Expected Job Title '{expected_job_title}', got '{actual_job_title}'."

        assert actual_status == expected_status, \
            f"Expected Employment Status '{expected_status}', got '{actual_status}'."

    def update_employee_job_details(self, emp_number):

        # Payload captured from the OrangeHRM Network request.
        # joinedDate is required by the API even when it is not updated.
        # jobTitleId = 9  -> QA Engineer
        # empStatusId = 3 -> Full-Time Permanent

        payload = {
            "joinedDate": None,
            "jobTitleId": 9,
            "empStatusId": 3
        }

        response = self.request.put(
            f"https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees/{emp_number}/job-details",
            data=payload
        )

        assert response.status == 200, \
            "Failed to update employee job details through API."

        updated_job_data = response.json()["data"]

        assert updated_job_data["jobTitle"]["title"] == "QA Engineer", \
            f"Expected Job Title 'QA Engineer', got '{updated_job_data['jobTitle']['title']}'."

        assert updated_job_data["empStatus"]["name"] == "Full-Time Permanent", \
            f"Expected Employment Status 'Full-Time Permanent', got '{updated_job_data['empStatus']['name']}'."

        return updated_job_data

    def delete_employee(self, emp_number):

        # Payload captured from the OrangeHRM Network request.
        # DELETE API expects Employee Number (empNumber), not Employee ID.

        payload = {
            "ids": [int(emp_number)]
        }

        response = self.request.delete(
            "https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/pim/employees",
            data=payload
        )

        assert response.status == 200, \
            "Failed to delete employee through API."

        deleted_employee = response.json()["data"]

        assert str(emp_number) in deleted_employee, \
            f"Employee Number '{emp_number}' was not deleted successfully."

        return deleted_employee

    def verify_employee_deleted(self, employee_id):

        employees = self.get_all_employees()["data"]

        for employee in employees:
            assert employee["employeeId"] != employee_id, \
                f"Employee ID '{employee_id}' still exists in API response."