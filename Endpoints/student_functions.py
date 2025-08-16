import json
import logging
import azure.functions as func

logger = logging.getLogger(__name__)

bp = func.Blueprint()

@bp.route(route="http_trigger")
def http_trigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    lastname = req.params.get('lastname')
    if not name or not lastname:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
            lastname = req_body.get('lastname')
            
    if name and lastname:
        return func.HttpResponse(f"Hello, {name} {lastname}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name and lastname in the query string or in the request body for a personalized response.",
             status_code=200
        )