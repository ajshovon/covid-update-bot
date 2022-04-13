import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

class cred():
    API_TOKEN = os.getenv('API_TOKEN')
    OWNER_ID = os.getenv('OWNER_ID')
    DB_NAME = os.getenv('DB_NAME')
    USER_NAME = os.getenv('USER_NAME')
    USER_PASS = os.getenv('USER_PASS')
    HOST_NAME = os.getenv('HOST_NAME')