import json


def load_data():
    # Python has try-except-finally
    try:
        with open('youtube.txt', 'r') as file:
            data = json.load(file)
           # print(type(data)) # We have a JSON list here
            return data 
            # This above line reads and loads the data, then converts it into JSON.
    except FileNotFoundError:
        return []
    
# This is a helper method which helps save the data
def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    # We use enumerate so that we get indexing for it
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        
        print(f"{index}. {video['name']} | {video['time']}")
    print("*" * 70)

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)

    index = int(input("Enter the video number to update: "))
    if 1<= index <= len(videos):
        name = input("Enter the new video name: ")
        time = input("Enter the video time: ")
        if name and time:
            videos[index-1] = {'name': name, 'time': time}
        else:
            print("Please provide a valid input")
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the video number to delete: "))
    if 1 <= index <= len(videos): 
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected")


def main():

    videos = load_data()

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
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            # Handles all other inputs
            case _:
                print("Invalid Choice")

# This is the standard way of running main program at the start of the code. Just industry standard thing
if __name__ == "__main__":
    main()