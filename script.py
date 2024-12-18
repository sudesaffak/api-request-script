import requests

API_URL = "https://random.dog/woof.json"
TOTAL_REQUESTS = 100
SIZE_LIMIT = 1050000

bigger_count = 0  
smaller_count = 0  


for i in range(1, TOTAL_REQUESTS + 1):
    try:
        # API'ye istek gönder
        response = requests.get(API_URL)
        data = response.json()
        image_url = data["url"]  
        
        # Resmi indir ve boyutunu ölç
        image_response = requests.get(image_url)
        response_size = len(image_response.content)
        
        # Boyut kontrolü
        if response_size > SIZE_LIMIT:
            bigger_count += 1
        else:
            smaller_count += 1
        
       
        print(f"{i}. İstek: Dosya Boyutu = {response_size} byte")

    except Exception as e:
        print(f"{i}. istekte hata oluştu: {e}")

# Sonuçları yazdır
print("\nSonuçlar:")
print(f"1050000 byte'dan büyük dosya sayisi: {bigger_count}")
print(f"1050000 byte'dan küçük dosya sayisi: {smaller_count}")
