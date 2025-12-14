import requests

def get_post_title():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)

    # Sunucu başarılı cevap verdiyse
    if response.status_code == 200:
        data = response.json()  # JSON -> Python dict
        print("Başlık:", data["title"])
    else:
        print("API hatası! Status code:", response.status_code)

get_post_title()
