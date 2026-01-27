import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
SPOTIFY_REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI', 'http://localhost:8888/callback')

# Spotify API scopes needed for playback control
SPOTIFY_SCOPE = 'user-modify-playback-state user-read-playback-state user-read-currently-playing'

def validate_config():
    """Validate that all required configuration is present."""
    if not SPOTIFY_CLIENT_ID:
        raise ValueError("SPOTIFY_CLIENT_ID is not set. Please check your .env file.")
    if not SPOTIFY_CLIENT_SECRET:
        raise ValueError("SPOTIFY_CLIENT_SECRET is not set. Please check your .env file.")
    return True
