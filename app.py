from flask import Flask, render_template, request
import numpy as np
import pickle

# Load the trained model
with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    input_data = [float(data['Adult Mortality']),
                  float(data['Alcohol']),
                  float(data['Percentage Expenditure']),
                  float(data['Hepatitis B']),
                  float(data['Measles']),
                  float(data['BMI']),
                  float(data['Polio']),
                  float(data['Total expenditure']),
                  float(data['Diphtheria']),
                  float(data['HIV/AIDS']),
                  float(data['GDP']),
                  float(data['Population']),
                  float(data['Income composition of resources']),
                  float(data['Schooling'])]
    input_data = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
