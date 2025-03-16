from pymongo import MongoClient


client = MongoClient("mongodb+srv://sanchitvohra13:tW4nJsy4H0p6bCNI@cluster-first-python.5qanh.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["youtubemanager"]
video_collections = db["videos"]

print(video_collections)

