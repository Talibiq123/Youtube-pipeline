import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def fetch_channel_data(channel_id):
    print(f"Ready to fetch data for channel: {channel_id} using API_KEY: {API_KEY[:5]}...")

if __name__ == "__main__":
    fetch_channel_data("UC_x5XG1OV2P6uZZ5FSM9Ttw")
