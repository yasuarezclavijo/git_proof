import json
import logging

import azure.functions as func

bp = func.Blueprint()

@bp.route(route="countries")
def countries_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request for countries list.')

    # Sample list of countries - you can expand this or load from a database
    countries = [
        {"code": "US", "name": "United States"},
        {"code": "CA", "name": "Canada"},
        {"code": "MX", "name": "Mexico"},
        {"code": "BR", "name": "Brazil"},
        {"code": "AR", "name": "Argentina"},
        {"code": "CO", "name": "Colombia"},
        {"code": "ES", "name": "Spain"},
        {"code": "FR", "name": "France"},
        {"code": "DE", "name": "Germany"},
        {"code": "IT", "name": "Italy"},
        {"code": "UK", "name": "United Kingdom"},
        {"code": "JP", "name": "Japan"},
        {"code": "CN", "name": "China"},
        {"code": "IN", "name": "India"},
        {"code": "AU", "name": "Australia"}
    ]

    return func.HttpResponse(
        json.dumps(countries),
        mimetype="application/json",
        status_code=200
    )