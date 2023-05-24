import sys
from typing import List, Tuple

from pandas import DataFrame

from tourism.components.data_ingestion import DataIngestion
from tourism.exception import TourismException
from tourism.logger import logging

class TrainPipeline:
    def __init__(self):
        pass

    
    def start_data_ingestion(self) -> Tuple[DataFrame, DataFrame]:
        logging.info("Entered the start_data_ingestion method of TrainPipeline class")

        try:
            logging.info("Getting the data from mongodb")

            data_ingestion = DataIngestion()

            train_data, test_set = data_ingestion.initiate_data_ingestion()

            logging.info("Got the train_set and test_set from mongodb")

            logging.info(
                "Exited the start_data_ingestion method of TrainPipeline class"
            )

            return train_data, test_set

        except Exception as e:
            raise TourismException(e, sys) from e
        
    
    def run_pipeline(self) -> None:
        logging.info("Entered the run_pipeline method of TrainPipeline class")

        try:
            train_set, test_set = self.start_data_ingestion()

            logging.info("Exited the run_pipeline method of TrainPipeline class")

        except Exception as e:
            raise TourismException(e, sys) from e