from flask import Flask, render_template, request
import pickle
import os
import pandas as pd
app = Flask(__name__)

model_dir = 'models'  

# Define paths to .pkl files
cropdamages_model_path = os.path.join(model_dir, 'cropdamagesmodel.pkl')
croprecommendation_model_path = os.path.join(model_dir, 'croprecommendationmodel.pkl')
yieldfinder_model_path = os.path.join(model_dir, 'YieldFinder.pkl')

# Load .pkl files
with open(cropdamages_model_path, 'rb') as file:
    cropdamages_model = pickle.load(file)

with open(croprecommendation_model_path, 'rb') as file:
    croprecommendation_model = pickle.load(file)

with open(yieldfinder_model_path, 'rb') as file:
    yieldfinder_model = pickle.load(file)

df = pd.read_csv("data/Crop_Agriculture_Data_2.csv")

X = df.drop(columns=['Crop_Damage']) 
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_page():
    return render_template('index.html')

@app.route('/FAQ.html')
def faq():
    return render_template('FAQ.html')

@app.route('/features.html')
def features():
    return render_template('features.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/model1.html', methods=['GET', 'POST'])
def model1():
    # Load pickled model
    pickled_model_path = os.path.join(model_dir, 'croprecommendationmodel.pkl')
    with open(pickled_model_path, 'rb') as file:
        pickled_model = pickle.load(file)

    if request.method == 'POST':
        # Get input values from the form
        n = float(request.form['N'])
        p = float(request.form['P'])
        k = float(request.form['K'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # Make a prediction using the loaded model
        input_data = [[n, p, k, temperature, humidity, ph, rainfall]]
        prediction = pickled_model.predict(input_data)[0]

        # You can pass the prediction to the template and display it
        return render_template('model1.html', prediction=prediction)

    return render_template('model1.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load pickled model
    pickled_model_path = os.path.join(model_dir, 'croprecommendationmodel.pkl')
    with open(pickled_model_path, 'rb') as file:
        pickled_model = pickle.load(file)

    # Get input values from the form
    n = float(request.form['N'])
    p = float(request.form['P'])
    k = float(request.form['K'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    # Make a prediction using the loaded model
    input_data = [[n, p, k, temperature, humidity, ph, rainfall]]
    prediction = pickled_model.predict(input_data)[0]

    # You can pass the prediction to the template and display it
    return render_template('model1.html', prediction=prediction)

@app.route('/model2.html', methods=['GET', 'POST'])
def model2():
    if request.method == 'POST':
        # Get user inputs from the form
        crop = request.form['crop']
        avg_rainfall = float(request.form['avg_rainfall'])
        pesticides_tonnes = float(request.form['pesticides_tonnes'])
        avg_temp = float(request.form['avg_temp'])

        # Make prediction using the loaded model (yieldfinder_model)
        prediction = yieldfinder_model.predict([[crop, avg_rainfall, pesticides_tonnes, avg_temp]])

        # Render template with prediction
        return render_template('model2.html', prediction=prediction)

    return render_template('model2.html')

@app.route('/model3.html', methods=['GET', 'POST'])
def model3():
    if request.method == 'POST':
        crop_type = request.form['crop_type']
        soil_type = request.form['soil_type']
        pesticide_category = request.form['pesticide_category']
        num_doses_week = int(request.form['num_doses_week'])
        num_weeks_used = int(request.form['num_weeks_used'])
        num_weeks_quit = int(request.form['num_weeks_quit'])
        season = request.form['season']

        prediction = predict_damage(X,crop_type, soil_type, pesticide_category, num_doses_week, num_weeks_used, num_weeks_quit, season)
        return render_template('model3.html', prediction=prediction)

    return render_template('model3.html')
@app.route('/predict_crop_damage', methods=['GET', 'POST'])
def predict_crop_damage():
    if request.method == 'POST':
        crop_type = request.form['crop_type']
        soil_type = request.form['soil_type']
        pesticide_category = request.form['pesticide_category']
        num_doses_week = int(request.form['num_doses_week'])
        num_weeks_used = int(request.form['num_weeks_used'])
        num_weeks_quit = int(request.form['num_weeks_quit'])
        season = request.form['season']

        # Pass X to the predict_damage function
        prediction = predict_damage(X, crop_type, soil_type, pesticide_category, num_doses_week, num_weeks_used, num_weeks_quit, season)
        return render_template('model3.html', prediction=prediction)

    return render_template('model3.html')

def predict_damage(X, Crop_Type, Soil_Type, Pesticide_Use_Category, Number_Doses_Week, Number_Weeks_Used, Number_Weeks_Quit, Season):
    # Initialize input data with zeros for all columns
    input_data = [[0] * (len(X.columns))]

    # Map input values to the corresponding column indices if the columns exist
    if f'Crop_Type_{Crop_Type}' in X.columns:
        input_data[0][X.columns.get_loc(f'Crop_Type_{Crop_Type}')] = 1
    if f'Soil_Type_{Soil_Type}' in X.columns:
        input_data[0][X.columns.get_loc(f'Soil_Type_{Soil_Type}')] = 1
    if f'Pesticide_Use_Category_{Pesticide_Use_Category}' in X.columns:
        input_data[0][X.columns.get_loc(f'Pesticide_Use_Category_{Pesticide_Use_Category}')] = 1

    # Set values for numerical features
    input_data[0][X.columns.get_loc('Number_Doses_Week')] = Number_Doses_Week
    input_data[0][X.columns.get_loc('Number_Weeks_Used')] = Number_Weeks_Used
    input_data[0][X.columns.get_loc('Number_Weeks_Quit')] = Number_Weeks_Quit

    # Map season input to the corresponding column index if the column exists
    if f'Season_{Season}' in X.columns:
        input_data[0][X.columns.get_loc(f'Season_{Season}')] = 1

    prediction = cropdamages_model.predict(input_data)
    return prediction[0]


@app.route('/pricing.html')
def pricing():
    return render_template('pricing.html')

@app.route('/weather.html')
def weather():
    return render_template('weather.html')

if __name__ == '__main__':
    app.run(debug=True)
