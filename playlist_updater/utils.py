import requests
import hashlib

def download_playlist(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def calculate_checksum(content):
    return hashlib.sha256(content.encode()).hexdigest()