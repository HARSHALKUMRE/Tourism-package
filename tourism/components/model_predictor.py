import sys
import logging

import pandas as pd

from tourism.configuration.s3_Operations import S3Operation
from tourism.exception import TourismException
from tourism.utils.main_utils import MainUtils
from tourism.constant import MODEL_FILE_NAME, IO_FILES_BUCKET, ARTIFACTS_DIR

log_writer = logging.getLogger(__name__)

class TourismData:
    def __init__(
        self,
        Age: float,
        CityTier: int,
        DurationOfPitch: float,
        NumberOfPersonVisiting: int,
        NumberOfFollowups: float,
        PreferredPropertyStar: float,
        NumberOfTrips: float,
        Passport: int,
        PitchSatisfactionScore: int,
        OwnCar: int,
        NumberOfChildrenVisiting: float,
        MonthlyIncome: float,
        TypeofContact: str,
        Occupation: str,
        Gender: str,
        ProductPitched: str,
        MaritalStatus: str,
        Designation: str,
    ):

        self.Age = Age

        self.CityTier = CityTier

        self.DurationOfPitch = DurationOfPitch

        self.NumberOfPersonVisiting = NumberOfPersonVisiting

        self.NumberOfFollowups = NumberOfFollowups

        self.PreferredPropertyStar = PreferredPropertyStar

        self.NumberOfTrips = NumberOfTrips

        self.Passport = Passport

        self.PitchSatisfactionScore = PitchSatisfactionScore

        self.OwnCar = OwnCar

        self.NumberOfChildrenVisiting = NumberOfChildrenVisiting

        self.MonthlyIncome = MonthlyIncome

        self.TypeofContact = TypeofContact

        self.Occupation = Occupation

        self.Gender = Gender

        self.ProductPitched = ProductPitched

        self.MaritalStatus = MaritalStatus

        self.Designation = Designation

    def get_tourism_input_data_frame(self):

        log_writer.info(
            "Entered get_Tourism_input_data_frame method of TourismData class"
        )

        try: 
            tourism_input_data = self.get_tourism_as_dict()

            log_writer.info("Got tourism as a dict")

            log_writer.info(
                "Exited get_tourism_input_data_frame method of TourismData class"
            )
            return pd.DataFrame(tourism_input_data)
        except Exception as e:
            raise TourismException(e, sys) from e
    
    def get_tourism_as_dict(self):
        log_writer.info("Entered get_tourism_as_dict method as TourismData class")

        try:
            input_data = {
                "Age": [self.Age],
                "CityTier": [self.CityTier],
                "DurationOfPitch": [self.DurationOfPitch],
                "NumberOfPersonVisiting": [self.NumberOfPersonVisiting],
                "NumberOfFollowups": [self.NumberOfFollowups],
                "PreferredPropertyStar": [self.PreferredPropertyStar],
                "NumberOfTrips": [self.NumberOfTrips],
                "Passport": [self.Passport],
                "PitchSatisfactionScore": [self.PitchSatisfactionScore],
                "OwnCar": [self.OwnCar],
                "NumberOfChildrenVisiting": [self.NumberOfChildrenVisiting],
                "MonthlyIncome": [self.MonthlyIncome],
                "TypeofContact": [self.TypeofContact],
                "Occupation": [self.Occupation],
                "Gender": [self.Gender],
                "ProductPitched": [self.ProductPitched],
                "MaritalStatus": [self.MaritalStatus],
                "Designation": [self.Designation],
            } 

            log_writer.info("Created tourism data dict")

            input_data = pd.DataFrame(input_data)

            log_writer.info("Created a dataframe of tourism data")

            log_writer.info("Exited get_tourism_as_dict method as TourismData class")

            return input_data
        except Exception as e:
            raise TourismException(e, sys) from e

class ModelPredictor:
    def __init__(self):
        self.utils = MainUtils()

        self.s3 = S3Operation()

    def predict(self, X):
        log_writer.info("Entered predict method of TourismPredictor class")

        try:
            best_model = self.s3.load_model(
                MODEL_FILE_NAME, IO_FILES_BUCKET, ARTIFACTS_DIR
            )

             # self, model_name: str, bucket_name: str, model_dir: str = None

            log_writer.info("Loaded best model from s3 bucket")

            tourism_op = best_model.predict(X)

            log_writer.info("Used best model to get predictions")

            log_writer.info("Exited predict method of TourismPredictor class")

            return tourism_op
        except Exception as e:
            raise TourismException(e, sys) from e