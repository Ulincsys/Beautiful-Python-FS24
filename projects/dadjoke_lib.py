import requests

def get_joke():
    # https://icanhazdadjoke.com/api
    api_url = "https://icanhazdadjoke.com/"
    
    h = {
        "User-Agent": "python API example",
        "Accept": "application/json"
    }
    
    response = requests.get(api_url, headers = h)
    
    if response.status_code == 200:
        return response.json()
    
if __name__ == "__main__":
    print(get_joke())
