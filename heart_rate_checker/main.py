from markupsafe import escape
import functions_framework
import json
import pandas as pd 

@functions_framework.http
def hello_http(request):

# Heart rate, this will be a number 
# We will sum a patients heart rate from two different visits to get a count 
# If the count is above 100, so if > 100, return response 
# Also say that they are possibly experiencing tachycardia 

    request_args = request.args

    if request_args and "heart rate" in request_args:
        heartrate_value1 = request_args["heart rate"]
    else:
        heartrate_value1 = 80

    if request_args and "heart rate" in request_args:
        heartrate_value2 = request_args["heart rate"]
    else:
        heartrate_value2 = 80

    # Step 1 convert everything to numbers 
    heartrate_num1 = int(heartrate_value1)
    heartrate_num2 = int(heartrate_value2)

    # Step 2 we now some them all together 
    hr_sum = heartrate_num1 + heartrate_num2 

    # Step 3 create a json object to return to the user 
    output = json.dumps(
        {
            "entered_heartrate1" : heartrate_num1, 
            "entered_heartrate2": heartrate_num2 , 
            "hr_sum" : hr_sum
        }
    )

    return f"Heart value 1 entered: {escape(heartrate_value1)}!"