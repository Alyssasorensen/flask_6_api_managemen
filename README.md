## flask_6_api_management
# HHA 504 Homework Assignment 6

The objective for this week's assignment is to create, document, and oversee APIs using Flask and FastAPI. Additionally, you'll delve into the distinctions between these two frameworks and seamlessly connect your APIs with Azure API Management.

## **Step-by-Step Instructions on Setting Up and Testing Both Flask and FastAPI Endpoints** 

### **Flask**

1. Install Flask:

If you haven't already installed Flask, you can do so using pip, the Python package manager.

```
pip install Flask
```

2. Create a Flask Application:

Create a Python script (e.g., app.py) for your Flask application. In this script, you will define your API endpoints.

```
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource', methods=['GET'])
def get_resource():
    # Define the data you want to return as a dictionary
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```

3. Define your endpoint:

In the code above, we've created a single endpoint at /api/resource that handles GET requests. It returns a JSON response with a sample dictionary.

4. Run the Flask Application: 

Save the app.py file and run the Flask application.

```
python app.py
```

This will start the development server, and your API will be accessible at http://127.0.0.1:5000/api/resource.

5. Access the API: 

Open your web browser or use a tool like curl or Postman to access the API. For example, you can open your browser and navigate to:

```
http://127.0.0.1:5000/api/resource
```

You should see a JSON response:

```
{
    "key1": "value1",
    "key2": "value2"
}
```

### **FastAPI**

Ensure you have an Azure account and an Azure subscription. 

1. Create an Azure Function:

First, create a new directory for your Azure Function project and navigate into it. You can use the Azure Functions Core Tools to create a new HTTP-triggered function. Open your terminal or command prompt and run the following commands:

```
func init YourFunctionApp --python
cd YourFunctionApp
func new --name YourHttpFunction --template "HTTP trigger"
```

Replace "YourFunctionApp" and "YourHttpFunction" with your preferred names.

2. Implement the Function:

Open the 'YourHttpFunction' directory in your code editor. In the '__init__.py' file, you can replace the existing code with your Flask-based API code. Here's an example:

```
import azure.functions as func
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/resource', methods=['GET'])
def get_resource(req: func.HttpRequest):
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    return func.HttpResponse(jsonify(data), mimetype="application/json")

if __name__ == '__main__':
    app.run()
```

You have essentially embedded your Flask app within the Azure Function.

3. Install Flask in the Function App:

You need to make sure Flask is available within the Azure Function app. To do this, create a 'requirements.txt' file in the same directory as your '__init__.py' with the following content:

```
Flask==2.1.1
```

Then, run the following command to install the dependencies:

```
pip install -r requirements.txt
```

4. Deploy the Function to Azure:

To deploy your Azure Function, you can use the Azure Functions Core Tools. Run the following command:

```
func azure functionapp publish YourFunctionAppName
```

Replace 'YourFunctionAppName' with the name of your Azure Function App.

5. Access the Azure Function:

Once deployed, your Flask-based API is now a serverless function. You can access it via an HTTP request by using the URL of your Azure Function App.

Your function's URL will be in the format:
'https://YourFunctionAppName.azurewebsites.net/api/YourHttpFunction'

Replace 'YourFunctionAppName' and 'YourHttpFunction' with the appropriate values.


## **Observations on the Differences Between Flask and FastAPI**

1. Ease of Use:

Flask: Flask is known for its simplicity and minimalistic design. It's easy to get started with, and its learning curve is relatively shallow.

FastAPI: FastAPI is designed to be easy to use and has a very intuitive API. It provides automatic data validation and serialization, making it quick to develop APIs.

2. Automatic Documentation:

Flask: Flask does not provide built-in support for automatic API documentation. You'll typically need to use tools like Swagger or other third-party libraries for documentation.

FastAPI: FastAPI automatically generates interactive API documentation using the OpenAPI standard. This documentation is available at /docs and /redoc endpoints and is very helpful for both developers and API consumers.

3. Request Handling:

Flask: Flask uses a more traditional request/response paradigm. You need to access request data using request object and handle responses explicitly.

FastAPI: FastAPI automatically parses request data based on type annotations and simplifies request handling. It also provides built-in support for handling query parameters, request bodies, and path parameters.

## **Documentation of APIs - Focusing on the Standard OpenAPI Format**

1. Install Azure Functions Core Tools:

First, ensure you have the Azure Functions Core Tools installed on your local development environment. You can follow the installation instructions for your platform here: Azure Functions Core Tools installation.

2. Create a New Azure Functions Project:

Open your terminal or command prompt and navigate to the directory where your Flask app is located.

Run the following command to create a new Azure Functions project:

```
func init YourFunctionApp --python
```

Replace "YourFunctionApp" with your preferred project name.

3. Add a New HTTP Trigger Function:

Run the following command to create a new HTTP-triggered function:

```
func new --name YourHttpFunction --template "HTTPTrigger"
```

Replace "YourHttpFunction" with a name for your HTTP-triggered function.

4. Update the Function Code:

Open the generated YourHttpFunction/__init__.py file and replace the function code with your Flask app code. You can modify it to use the azure.functions package.

Here's an example of how you can adapt your Flask app code to work with Azure Functions:

```
import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    name = req.params.get('name', 'World')
    return func.HttpResponse(f'Hello {name}!')
```

5. Deploy the Function App:

Run the following command to deploy your Azure Function App to Azure:

```
func azure functionapp publish YourFunctionAppName
```

Replace "YourFunctionAppName" with your desired Azure Function App name.

6. Access Your Function:

After successful deployment, you can access your serverless function using the provided URL. It will be in the format: https://YourFunctionAppName.azurewebsites.net/api/YourHttpFunction.

Replace "YourFunctionAppName" with your actual function app name and "YourHttpFunction" with the name of your HTTP-triggered function.

## **Steps and Observations on Azure API Management Integration**

To add Swagger/OpenAPI documentation to your Flask app using the "flasgger" package, you can follow these instructions:

1. Install Flask and Flasgger:

First, ensure you have Flask and the flasgger package installed. You can install them using pip:

```
pip install Flask
pip install flasgger
```

2. Modify Your Flask App:

Update your Flask app to include the flasgger extension for generating Swagger documentation. Here's how you can modify your Flask app:

```
from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    """
    Home endpoint.
    This is the home endpoint of the API.
    ---
    responses:
      200:
        description: A welcome message
    """
    return 'Welcome to my Flask API'

@app.route('/calculation', methods=['GET'])
def calculation_get():
    """
    Calculate something.
    This endpoint performs a calculation based on input data.
    ---
    parameters:
      - name: input_data
        in: query
        type: string
        required: true
        default: 0
    responses:
      200:
        description: The result of the calculation
    """
    input_data = request.args.get('input_data', 0)
    # Perform your calculation here
    result = input_data * 2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
```

In the code above, we've added the Swagger(app) line to initialize flasgger. We've also added docstring-style comments with descriptions for each endpoint and the expected request and response formats.

3. Generate Swagger Documentation:

When you run your Flask app, you can access the Swagger documentation at /apidocs by default. For example, if your Flask app is running locally, you can access the documentation at:

```
http://127.0.0.1:5000/apidocs
```

The Swagger documentation provides an interactive UI for exploring and testing your API.

4. Customize the Documentation:

You can further customize the Swagger documentation by adding more details to the docstring comments, including request parameters, example values, and more. Refer to the 'flasgger' documentation and Swagger specification for advanced customization options.

5. Run and Test Your App:

Start your Flask app:

```
python app.py
```

Access the Swagger documentation in your browser, and you can test your API endpoints interactively. The documentation will also include the details you provided in the docstring comments. 

## **Challenges Encountered, Solutions Tried, and Conclusions**

I encountered a few challenges trying to do the Azure API deployment. I tried different steps, but was not able to successfully deploy it.  

I was able to do the following steps with no issues. 

1. Installing the Azure CLI:

```
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

2. Then I logged in:

```
az login --use-device-code
```

3. Then I ran the following code:

```
sudo apt-get install azure-functions-core-tools-4
```

Each of the steps worked properly. However, when trying to view the function_app.py, it would not show the URL, so then I was not able to view the API.

However, I still proceeded with each of the steps to see if it would work. 

4. I created a new resource group:

```
az group create --name AzureFunctionsQuickstart-rg --location eastus
```

5. Then I created a new storage account:

```
az storage account create --name alyssaflaskazure504 --location eastus --resource-group AzureFunctionsQuickstart-rg --sku Standard_LRS
```

6. Then I tried to create the functionapp, and this is where I kept receiving an error. 

```
az functionapp create --resource-group AzureFunctionsQuickstart-rg --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name Alyssa150 --os-type linux --storage-account alyssaflaskazure504
```

When running this in the terminal, I kept receiving this error message:

"usage error: You must specify one of these parameter --plan NAME_OR_ID | --consumption-plan-location LOCATION"

I was getting confused because in the code I included "--consumption-plan-location LOCATION," and I wrote that it is "eastus."

To try and solve this issues, I also included a code with both the NAME and LOCATION, as well as one with just the NAME. After doing these codes, I kept receiving the same error message.