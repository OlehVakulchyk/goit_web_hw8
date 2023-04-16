# from mongoengine import *
# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://goit-web10:131065@goitlearn-10.m8bniak.mongodb.net/test?retryWrites=true&w=majority"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

from mongoengine import connect
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

mongo_user = config.get('DB', 'user')
mongodb_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

# connect to cluster on AtlasDB with connection string

connect(
    host=f"""mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority""", ssl=True
    )
