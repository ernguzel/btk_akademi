import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "BTK Eğitim",
    "body": "Python desteği.",
    "userId": 1
}

response = requests.post(url, json=payload)

print("Durum:", response.status_code)
print("API Yanıtı:", response.json())
