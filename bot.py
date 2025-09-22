import requests
import time

# === CONFIG ===
TELEGRAM_TOKEN = "8445745064:AAEcVGNMnrv9VvWA69RWcBJcC2d1xW4ZPTI"
CHANNEL_ID = "@ringzon"  # aapka channel username
FETCH_INTERVAL = 3600  # seconds (1 ghanta me new songs post honge)

SEARCH_KEYWORD = "new hindi songs"
SONGS_LIMIT = 5

def send_photo(photo_url, caption):
    """Telegram channel par gaane ki photo + caption bhejne ke liye"""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendPhoto"
    payload = {
        "chat_id": CHANNEL_ID,
        "photo": photo_url,
        "caption": caption,
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print("Error sending photo:", e)

def fetch_and_send_songs():
    """iTunes API se songs fetch karke Telegram par bhejta hai"""
    url = f"https://itunes.apple.com/search?term={SEARCH_KEYWORD}&entity=musicTrack&limit={SONGS_LIMIT}"
    try:
        response = requests.get(url).json()
        for song in response.get("results", []):
            track_name = song.get("trackName")
            artist = song.get("artistName")
            preview_url = song.get("previewUrl")
            artwork_url = song.get("artworkUrl100")

            caption = f"🎵 *{track_name}*\n🎤 {artist}\n🎧 [Preview]({preview_url})"
            send_photo(artwork_url, caption)
    except Exception as e:
        print("Error fetching songs:", e)

if __name__ == "__main__":
    while True:
        fetch_and_send_songs()
        time.sleep(FETCH_INTERVAL)
