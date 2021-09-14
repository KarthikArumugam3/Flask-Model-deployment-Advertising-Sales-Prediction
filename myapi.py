from flask import Flask,request, jsonify
import joblib
import pandas as pd

# Create the flask application
app = Flask(__name__)

# Connect POST routing call/ API routing call - predict() function
@app.route('/predict',methods=['POST'])
def predict():

    #Get JSON request
    feat_data = request.json

    # Convert JSON to pandas df (matches up with col names)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)

    # Return the prediction as JSON
    prediction = list(model.predict(df))


    return jsonify({'prediction':str(prediction)})  # return prediction

# Load my model and setup the column names
if __name__ == '__main__':
    model = joblib.load("final_model.pkl")
    col_names = joblib.load('column_names.pkl')

    app.run(debug=True)
