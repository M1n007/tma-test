
from dotenv import load_dotenv

import os

load_dotenv()

def getEnv(key):
    return os.getenv(key)

