import json

def load_data():
    try:
        with open("database.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helper(videos):
    with open("database.txt", "w") as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration {video['time']}")
    print("*" * 50)

def add_video(videos):
    name = input("\nEnter Video Name: ")
    time = input("Enter Video Time: ")
    videos.append({"name": name, "time" : time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("\nEnter The Video Number To Update "))
    if 1 <= index <= len(videos):
        name = input("\nEnter The New Video Name ")
        time = input("Enter The New Video Time ")
        videos[index-1] = {"name" : name, "time" : time}
        save_data_helper(videos)
    else:
        print("\nInvalid Video Number Selected")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("\nEnter The Video Number To Be Deleted "))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("\nInvalid Video Number Selected")

def main():
    videos = load_data()
    while True:
        print("\nVideo Library Organizer | Choose An Option")
        print("1. List All Youtube Videos")
        print("2. Add A Youtube Video")
        print("3. Update A Youtube Video Details")
        print("4. Delete A Youtube Video")
        print("5. Exit")

        choice = input("Enter Your Choice ")

        match choice:
            case "1":
                list_all_videos(videos)
            case "2":
                add_video(videos)
            case "3":
                update_video(videos)
            case "4":
                delete_video(videos)
            case "5":
                break
            case _:
                print("Invalid Choide")

if __name__ == "__main__":
    main()
