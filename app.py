from flask import Flask, request, render_template, jsonify
from flask_cors import CORS, cross_origin
from tourism.exception import TourismException
from tourism.logger import logging
from tourism.components.model_predictor import ModelPredictor, TourismData
from tourism.constant import APP_HOST, APP_PORT
from tourism.pipeline.training_pipeline import TrainPipeline

application = Flask(__name__)
app = application

@app.route('/')
@cross_origin()
def home_page():
    return render_template('index.html')


@app.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def predict_datapoint():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        
        tourism_data = TourismData(
            Age = float(request.form.get('Age')),
            CityTier = int(request.form.get('CityTier')),
            DurationOfPitch = float(request.form.get('DurationOfPitch')),
            NumberOfPersonVisiting = int(request.form.get('NumberOfPersonVisiting')),
            NumberOfFollowups = float(request.form.get('NumberOfFollowups')),
            PreferredPropertyStar = float(request.form.get('PreferredPropertyStar')),
            NumberOfTrips = float(request.form.get('NumberOfTrips')),
            Passport = int(request.form.get('Passport')),
            PitchSatisfactionScore = int(request.form.get('PitchSatisfactionScore')),
            OwnCar = int(request.form.get('OwnCar')),
            NumberOfChildrenVisiting = float(request.form.get('NumberOfChildrenVisiting')),
            MonthlyIncome = float(request.form.get('MonthlyIncome')),
            TypeofContact = request.form.get('TypeofContact'),
            Occupation = request.form.get('Occupation'),
            Gender = request.form.get('Gender'),
            ProductPitched = request.form.get('ProductPitched'),
            MaritalStatus = request.form.get('MaritalStatus'),
            Designation = request.form.get('Designation')
        )

        tourism_df = tourism_data.get_tourism_as_dict()

        print(tourism_df)

        tourism_predictor = ModelPredictor()

        tourism_value = tourism_predictor.predict(X=tourism_df)[0]

        if tourism_value == 1:
            results = "The Tourist bought the package"

        else:
            results = "The Tourist didn't buy the package"
        return render_template('index.html', results=results, tourism_df=tourism_df)


@app.route("/train")
@cross_origin()
def trainRoute():
    try:
        train_pipeline = TrainPipeline()

        train_pipeline.run_pipeline()

        return Response("Training successful !!")

    except Exception as e:
        return Response(f"Error Occurred! {e}")


if __name__ == "__main__":
    app.run(host=APP_HOST, port=APP_PORT)