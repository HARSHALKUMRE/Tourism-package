import os 

from pymongo import MongoClient

from dotenv import load_dotenv
print(f"Reading Environment Variables")
load_dotenv()

import urllib

user = urllib.parse.quote_plus(os.getenv("USER"))
passwd = urllib.parse.quote_plus(os.getenv("PASS"))

class DatabaseConfig:
    def __init__(self):
        self.DATABASE_NAME = "iNeuron"
        
        self.COLLECTION_NAME = "tourism"
        
        self.MONGO_DB_URL = "mongodb+srv://%s:%s@cluster0.ppzqzhg.mongodb.net/?retryWrites=true&w=majority" % (user, passwd)
        
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