import os

import motor.motor_asyncio

from dotenv import load_dotenv

load_dotenv()

PASSWORD = "thisisahardcodedpasswordfortesting"
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DB]
