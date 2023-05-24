import os, sys
import pandas as pd
import numpy as np
from tourism.constant import *
from tourism.logger import logging
from tourism.exception import TourismException
from tourism.pipeline.training_pipeline import TrainPipeline

def main():
    try:
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")

if __name__ == "__main__":
    main() 