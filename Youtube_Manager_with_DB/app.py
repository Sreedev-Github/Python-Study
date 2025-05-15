import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

# Triple quoting helps us save the format as it is
cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            time TEXT NOT NULL
        )               
''')

def list_all_videos():
    cursor.execute("SELECT* FROM videos")
    # No need to store the cursor in a variable as it already holds the value inside of it.
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    # ? will act as a variable sapce
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit() # Stores it in DB

def update_videos(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))

    conn.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,)) # THis last comma is import as then only it will be sent as tuple
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Video")
        print("3. Update Video")
        print("4. Delete Video")
        print("5. Exit App")

        choice = input("Enter your choice: ")



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

    # This helps prevent any extra memory use and db corruption
    conn.close()

if __name__ == "__main__":
    main()