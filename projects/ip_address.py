import requests

def get_ip_address():
   api_url = "http://icanhazip.com"
   response = requests.get(api_url)
  
   if response.status_code == 200:
       return response.text

print(get_ip_address())