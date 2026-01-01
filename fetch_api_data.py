import requests

BASE_URL = "https://www.googleapis.com/youtube/v3"
API_KEY = "YOUR_API_KEY"   # keep this in env variable later

params = {
    "part": "snippet,contentDetails",
    "channelId": "UC0yXUUIaPVAqZLgRjvtMftw",
    "key": "AIzaSyCNfHIK_Ize8fFFbTnCmJYi6_rwu2whf28"
}

response = requests.get(f"{BASE_URL}/activities", params=params)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Error:", response.json())
