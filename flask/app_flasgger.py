from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

@app.route('/')
def home():
    return f'Welcome to my Flask Endpoint'

@app.route('/calculation', methods=['GET'])
def calculation_get():
    """
    This endpoint returns a greeting message.
    ---
    parameters:
      - name: heart_rate
        in: query
        type: string
        required: false
        default: normal
    responses:
      200:
        description: A greeting message
    """
    heart_rate = request.args.get('heart_rate', 'normal')
    return f'How are you feeling {heart_rate}?'

@app.route('/calculation', methods=['POST'])
def calculation_post():
    """
    This endpoint returns a greeting message based on the name provided in the JSON body.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: data
          required:
            - name
          properties:
            name:
              type: string
              default: normal
    responses:
      200:
        description: A greeting message
      400:
        description: Invalid JSON
    """
    data = request.get_json()
    if data is None:
        return jsonify({'error': 'Invalid JSON'}), 400
    
    heart_rate = data.get('heart_rate', 'normal')
    return jsonify({'message': f'How are you feeling {heart_rate}?'})

if __name__ == '__main__':
    app.run(debug=True)
