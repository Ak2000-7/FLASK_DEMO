import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "db.db.settings")
django.setup()

from django.core.management import call_command
from flask import Flask
from flask_restful import Api
from handlers.employee_handler import EmployeeHandler

local_server = True
app = Flask(__name__)


#engine = create_engine('mysql://root:@localhost/test1?unix_socket=/tmp/mysql.sock', echo=True)


# if local_server:
#     app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password@localhost/company"
# else:
#     app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:password@localhost/company"



# db.init_app(app)

api = Api(app)


api.add_resource(EmployeeHandler, '/employees','/employees/<int:id>')


app.run(debug=True)
