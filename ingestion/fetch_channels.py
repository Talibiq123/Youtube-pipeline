import os
import json
import requests
from datetime import datetime
from dotenv import load_dotenv

# Load API key
load_dotenv(dotenv_path="config/.env")
API_KEY = os.getenv("YOUTUBE_API_KEY")

BASE_URL = "https://www.googleapis.com/youtube/v3/channels"

def fetch_channel_data(channel_id):
    params = {
        "part": "snippet,statistics,contentDetails",
        "id": channel_id,
        "key": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()

    return response.json()

def save_raw_data(data):
    today = datetime.utcnow().strftime("%Y-%m-%d")

    base_path = f"raw_data/channels/ingestion_date={today}"
    os.makedirs(base_path, exist_ok=True)

    file_path = os.path.join(base_path, "channels.json")

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

    print(f"Raw data saved to {file_path}")

if __name__ == "__main__":
    channel_id = "UC_x5XG1OV2P6uZZ5FSM9Ttw"
    data = fetch_channel_data(channel_id)
    save_raw_data(data)
