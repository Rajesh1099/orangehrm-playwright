import json

def load_employee_data():
    
    # Read employee test data from JSON file
    with open("testdata/employee.json", "r") as file:
        employee_data = json.load(file)

    return employee_data