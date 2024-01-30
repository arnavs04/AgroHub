from flask import Flask, render_template
import pickle
import os

app = Flask(__name__)

model_dir = 'models'  # Directory where your .pkl files are stored

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cropdamages')
def cropdamages():
  
    return render_template('cropdamages.html')

@app.route('/croprecommendation')
def croprecommendation():
   
    return render_template('croprecommendation.html')

@app.route('/yieldfinder')
def yieldfinder():

    return render_template('yieldfinder.html')

if __name__ == '__main__':
    app.run(debug=True)