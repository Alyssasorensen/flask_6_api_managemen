import requests

url = 'https://us-east4-alyssacloud504hw.cloudfunctions.net/python-http-function'

test = requests.get(
    url, 
    params={"name": "alyssa"}
)

test
test.text