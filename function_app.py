import azure.functions as func
import logging
from Endpoints.student_functions import bp as student_functions_blueprint
from Endpoints.countries_functions import bp as countries_function
    
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

app.register_functions(student_functions_blueprint)
app.register_functions(countries_function)
