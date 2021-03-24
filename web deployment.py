
import numpy as np
import pickle
from flask import Flask, request, render_template

model = pickle.load(open('heart.pkl', 'rb')) 

app = Flask(__name__)

@app.route('/predict', methods =['POST'])
def predict():
    
    features = [float(i) for i in request.form.values()]
    array_features = [np.array(features)]
    guess = model.predict(array_features)
    
    result = guess
    
    if result == 1:
        return render_template('Heart Disease Classifier.html', 
                               result = 'The patient does not have heart disease')
    else:
        return render_template('Heart Disease Classifier.html', 
                               result = 'The patient has heart disease')

if __name__ == '__main__':
    app.run()