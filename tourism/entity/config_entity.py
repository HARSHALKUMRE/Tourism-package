import os 

from pymongo import MongoClient

class DatabaseConfig:
    def __init__(self):
        self.DATABASE_NAME = "iNeuron"
        
        self.COLLECTION_NAME = "tourism"
        
        self.MONGO_DB_URL = f'mongodb+srv://harshal:Harshal@123@cluster0.ppzqzhg.mongodb.net/?retryWrites=true&w=majority'
        
    def get_database_config(self):
        return self.__dict__
        
class S3Config:
    def __init__(self):
        self.IO_FILES_BUCKET = "tourism-io-files"

    def get_s3_config(self):
        return self.__dict__


class TunerConfig:
    def __init__(self):
        self.verbose = 2

        self.cv = 2

        self.n_jobs = -1

    def get_tuner_config(self):
        return self.__dict__