# app/handlers.py
from flask import Flask, request
from flask_restful import Api, Resource
from controllers.employee_controller import EmployeeController
from services.employee_services import EmployeeService

app = Flask(__name__)
api = Api(app)

class EmployeeHandler(Resource):
    def get(self):
        
        employees = EmployeeService.get_all_employees()
        return {"employees": employees}

    def post(self):
        
        employee_controller = EmployeeController()
        return employee_controller.add_employee()
       


    def put(self, id):
        employee_controller = EmployeeController()
        data = request.get_json()
        name = data.get('name')

        if not name:
            return {"error": "Incomplete data"}, 400

        return employee_controller.update_employee_by_id(id)

    def delete(self, id):
        employee_controller = EmployeeController()
        return employee_controller.delete_employee_by_id(id)
