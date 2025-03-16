import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
        )
    ''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    print()
    print("*************************************************************************************************************")
    for row in cursor.fetchall():
        print(row)
    print("*************************************************************************************************************")


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()



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

    conn.close()


if __name__ == "__main__":
    main()