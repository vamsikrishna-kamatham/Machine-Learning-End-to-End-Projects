# Import necessary libraries
from flask import Flask, request, jsonify
import util

# Create Flask application instance
app = Flask(__name__)

# Bind function to URL route '/get_location_names'
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    # Get location names using 'util' module and jsonify them
    response = jsonify({
        'locations': util.get_location_names()
    })
    # Add Access-Control-Allow-Origin header to response
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# Bind function to URL route '/predict_home_price'
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # Get input parameters and convert them to appropriate data types
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])
    # Predict home price using 'util' module and jsonify the result
    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })

    # Add Access-Control-Allow-Origin header to response
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# Run the application if this script is being run directly
if __name__ == "__main__":
    # Print message and load saved artifacts before running the application
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    # Start Flask server
    app.run()