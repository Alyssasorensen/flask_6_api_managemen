import azure.functions as func
import datetime
import json
import logging

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="calculation")
def calculation_get(req: func.HttpRequest) -> func.HttpResponse:
    calculation = req.params.get("calculation")
    if not calculation:
        calculation= "normal"
    if calculation:
        return func.HttpResponse(f'How are you feeling {calculation}?')