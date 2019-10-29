from pymongo import MongoClient

client=MongoClient("mongodb+srv://test:1234@cluster0-wytxl.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database('water_quality_uk')
