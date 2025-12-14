import requests

url = "https://jsonplaceholder.typicode.com/this_endpoint_does_not_exist"

try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # 4xx / 5xx hataları fırlatır
except requests.Timeout:
    print("İstek zaman aşımına uğradı.")
except requests.ConnectionError:
    print("Sunucuya bağlanılamadı.")
except requests.HTTPError as e:
    print("Sunucu hata döndürdü:", e)
else:
    print("Başarılı:", response.json())
