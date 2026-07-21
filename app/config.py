#we will writee schemas andd url things

from dotenv import load_dotenv
import os

load_dotenv()  # it autmaticallay detect the .env file and load all the env vars in env format of python dict
#os.getenv() :- use to get the value of the env var or environment variable
#why we use this :- is to maintaing the security 

MONGODB_URL = os.getenv("MONGODB_URL") #we can also use os.getenv("MONGODB_URL",default_value)
DATABASE_NAME = os.getenv("DATABASE_NAME") #we can also use os.getenv("DATABASE_NAME",default_value)

