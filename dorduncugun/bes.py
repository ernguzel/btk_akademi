import requests

def fetch_users():
    url = "https://jsonplaceholder.typicode.com/users"
    users = requests.get(url).json()
    return [
        (u["id"], u["name"], u["email"])
        for u in users
        if "email" in u
    ]


print(fetch_users())