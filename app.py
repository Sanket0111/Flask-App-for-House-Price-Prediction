#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import joblib

app = Flask(__name__)

# Load the dataset and model
data = pd.read_csv('final_dataset.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))

@app.route('/')
def index():
    # Prepare the dropdown options for the form
    bedrooms = sorted(data['beds'].unique())
    bathrooms = sorted(data['baths'].unique())
    sizes = sorted(data['size'].unique())
    zip_codes = sorted(data['zip_code'].unique())

    return render_template('index.html', bedrooms=bedrooms, bathrooms=bathrooms, sizes=sizes, zip_codes=zip_codes)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        bedrooms = int(request.form.get('beds'))
        bathrooms = float(request.form.get('baths'))
        size = float(request.form.get('size'))
        zipcode = int(request.form.get('zip_code'))

        # Prepare input data for the model
        input_data = pd.DataFrame([[bedrooms, bathrooms, size, zipcode]], 
                                  columns=['beds', 'baths', 'size', 'zip_code'])

        # Replace unknown categories with the mode of the column
        for column in input_data.columns:
            unknown_categories = set(input_data[column]) - set(data[column].unique())
            if unknown_categories:
                input_data[column] = input_data[column].replace(unknown_categories, data[column].mode()[0])

        # Make the prediction
        prediction = pipe.predict(input_data)[0]

        # Format the prediction to two decimal places
        formatted_price = f"{prediction:,.2f}"

        return jsonify({'price': formatted_price})

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)


# In[ ]:




