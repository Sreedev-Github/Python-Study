from pymongo import MongoClient
from bson import ObjectId


client = MongoClient("mongodb+srv://authuser:Evizeno1508@cluster0.m8edt49.mongodb.net/") # This will make sure even if we do not have a SSL the connection will be allowed.

db = client["ytmanager"]
video_collection = db["videos"]

print(video_collection)

def list_all_videos():
    for video in video_collection.find({}):
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def add_videos(name, time):
    video_collection.insert_one({"name" : name, "time": time})

def update_videos(video_id, new_name, new_time):
    video_collection.find_one_and_update(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )


def delete_videos(videoId):
    video_collection.delete_one({"_id": ObjectId(videoId)})




def main():

    while True:
        print("\n Youtube Manager | choose an option")
        print("1. List all favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")

        choice =  input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_videos(name, time)
            case '3':
                video_id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_videos(video_id, name, time)
            case '4':
                video_id = input("Enter video ID to delete: ")
                delete_videos(video_id)
            case '5':
                break
            case _:
                print("Invalid choice")

if __name__ == "__main__":
    main()