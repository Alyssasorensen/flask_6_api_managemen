import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Parse the query parameter from the request
    heart_rate = req.params.get('heart_rate', '80')

    # Convert heart rate to an integer
    heart_rate_num = int(heart_rate)

    # Calculate the sum
    hr_sum = heart_rate_num + heart_rate_num

    # Create a JSON response
    response = {
        'entered_heart_rate': heart_rate_num,
        'hr_sum': hr_sum
    }

    return func.HttpResponse(json.dumps(response), mimetype="application/json")
