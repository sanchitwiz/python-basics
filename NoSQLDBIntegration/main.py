from pymongo import MongoClient
from bson.objectid import ObjectId  # Correct import





client = MongoClient("mongodb+srv://sanchitvohra13:tW4nJsy4H0p6bCNI@cluster-first-python.5qanh.mongodb.net/", tlsAllowInvalidCertificates=True)

db = client["youtubemanager"]
video_collections = db["videos"]

print(video_collections)





def list_videos():
    for video in video_collections.find():
        print(f"ID: {video['_id']}, Name: {video['name']} Duration: {video['time']}")

def add_video(name, time):
    video_collections.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collections.update_one(
        {'_id': ObjectId(video_id)},  # Fixed ObjectId usage
        {"$set": {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collections.delete_one({"_id": ObjectId(video_id)})  # Fixed ObjectId usage

def main():
    while True:
        print("\n* Youtube Manager with DB: ")
        print("1. List all youtube videos ")
        print("2. Add a Youtube Video ")
        print("3. Update a Youtube Video details ")
        print("4. Delete a youtube video ")
        print("5. Exit the app ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter Video Name: ")
                time = input("Enter Video Duration: ")
                add_video(name, time)
            case '3':
                video_id = input("Enter Video ID to update: ")
                name = input("Enter Video Name: ")
                time = input("Enter Video Duration: ")
                update_video(video_id, name, time)
            case '4':
                video_id = input("Enter Video ID to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice ")

if __name__ == "__main__":
    main()
