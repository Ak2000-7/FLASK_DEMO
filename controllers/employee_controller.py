from services.employee_services import EmployeeService
from flask import request

class EmployeeController:
    def add_employee(self):
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        address = data.get('address')
        phone = data.get('phone')

        if not all([name, email, address, phone]):
            return {"error": "Incomplete data"}, 400

        EmployeeService.add_employee(name, email, address, phone)
        return {"message": "Employee added successfully"}

    def delete_employee_by_id(self, employee_id):
        EmployeeService.delete_employee_by_id(employee_id)
        return {"message": "Employee deleted successfully"}

    def update_employee_by_id(self, employee_id):
        data = request.get_json()
        name = data.get('name')

        if not name:
            return {"error": "Incomplete data"}, 400

        EmployeeService.update_employee_by_id(employee_id, name)
        return {"message": "Employee updated successfully"}

    def update_employee_by_name(self, name):
        data = request.get_json()
        new_name = data.get('new_name')

        if not new_name:
            return {"error": "Incomplete data"}, 400

        EmployeeService.update_employee_by_name(name, new_name)
        return {"message": "Employee updated successfully"}

    def get_employees_by_names(self):
        data = request.get_json()
        names = data.get('names')

        if not names:
            return {"error": "No names provided"}, 400

        employees = EmployeeService.get_employees_by_names(names)
        return {"employees": employees}
