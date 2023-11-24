from db.db.employees.models import Employees

class EmployeeService:

    def get_all_employees():
        # all_objects=[]
        # objects=Employees.objects.all()
        # for object in objects:
        #     all_objects.append(object.email)
        
        # return all_objects
        employees = Employees.objects.all()
        return [{"id": employee.id, "name": employee.name, "email": employee.email, "address": employee.address, "phone": employee.phone} for employee in employees]



    
    def add_employee(name, email, address, phone):
        employee = Employees(name=name, email=email, address=address, phone=phone)
        employee.save()

    
    def delete_employee_by_id(employee_id):
        Employees.objects.filter(id=employee_id).delete()

    
    def update_employee_by_id(employee_id, new_name):
        employee = Employees.objects.get(id=employee_id)
        employee.name = new_name
        employee.save()

    
    def update_employee_by_name(name, new_name):
        employees = Employees.objects.filter(name=name)
        for employee in employees:
            employee.name = new_name
            employee.save()

   
    def get_employees_by_names(names):
        employees = Employees.objects.filter(name__in=names)
        return [{"id": employee.id, "name": employee.name, "email": employee.email, "address": employee.address, "phone": employee.phone} for employee in employees]


