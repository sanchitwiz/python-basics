import requests

def fetch_ramdom_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        return username
    else:
        raise Exception("Failed to Fetch user data")


def main():
    try:
        data = fetch_ramdom_user()
        print(data)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()