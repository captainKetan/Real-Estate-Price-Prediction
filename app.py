from flask import Flask, request, jsonify, render_template
import utils
import requests

app = Flask(__name__)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': utils.get_location_names()
    })
    return response

@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    if request.method == 'GET':
        locations = utils.get_location_names()
        return render_template('app.html', locations=locations)
    else:
        total_sqft = float(request.form['Squareft'])
        bhk = int(request.form['uiBHK'])
        bath = int(request.form['uiBathrooms'])
        location = request.form['uiLocations']

        response = utils.get_estimated_price(location,total_sqft,bhk,bath)
        
    return render_template('app.html', final_result=response, locations=utils.get_location_names())

if __name__ == "__main__":
    utils.load_saved_artifacts()
    app.run(host='0.0.0.0')