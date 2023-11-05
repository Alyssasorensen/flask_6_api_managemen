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

## **Steps and Observations on Azure API Management Integration**

## **Challenges Encountered, Solutions Tried, and Conclusions**