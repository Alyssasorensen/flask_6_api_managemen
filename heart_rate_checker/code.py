import requests 
import pandas as pd 

df = pd.DataFrame({
    'heartrate_num1': [102, 121, 63, 76],
    'heartrate_num2': [80, 59, 109, 75]
})

df[:1]['heartrate_num1']


analysis = requests.get(
    url = 'https://us-east4-alyssacloud504hw.cloudfunctions.net/python-http-function',
    params = ({
        "heartrate_num1": df[:1]['heartrate_num1'],
        "heartrate_num2": df[:1]['heartrate_num2']
    })
)

analysis.text