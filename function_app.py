import azure.functions as func
import logging
from Endpoints.student_functions import bp as student_functions_blueprint

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

app.register_functions(student_functions_blueprint)
