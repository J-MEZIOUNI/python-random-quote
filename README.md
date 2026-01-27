# Let's Write a Python Quote Bot!

This repository will get you started with building a quote bot in Python. It's meant to be used along with the [Learning Lab](https://lab.github.com) intro to Python.

When complete, you'll be able to grab random quotes from the command line, like this:

> **$** python get-quote.py
> 
> Keep it logically awesome
> 
> **$** python get-quote.py
> 
> Speak like a human

## Start the Tutorial

You can find your next step in [this repo's issues](../../issues/)!

---

# 🎵 Spotify Player

Control your Spotify playback directly from the command line!

## Features

- 🎧 Play music by searching for songs, artists, or albums
- ⏯️ Control playback (play, pause, skip, previous)
- 🔊 Adjust volume
- 📱 View and select available Spotify devices
- 🎵 See currently playing track information
- 💬 Interactive command-line interface

## Setup

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Create Spotify App

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
2. Log in with your Spotify account
3. Click "Create an App"
4. Fill in the app name and description
5. Once created, you'll see your **Client ID** and **Client Secret**
6. Click "Edit Settings" and add `http://localhost:8888/callback` to the Redirect URIs

### 3. Configure Environment Variables

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your Spotify credentials:
   ```
   SPOTIFY_CLIENT_ID=your_actual_client_id
   SPOTIFY_CLIENT_SECRET=your_actual_client_secret
   SPOTIFY_REDIRECT_URI=http://localhost:8888/callback
   ```

### 4. First Run Authentication

The first time you run the player, you'll need to authenticate:

1. Run the player: `python spotify_player.py`
2. A browser window will open asking you to authorize the app
3. After authorizing, you'll be redirected to a localhost URL
4. Copy the entire URL from your browser and paste it back into the terminal
5. The authentication token will be cached for future use

## Usage

### Quick Play

Play a song directly from the command line:

```bash
python spotify_player.py "Bohemian Rhapsody"
python spotify_player.py "The Beatles Hey Jude"
```

### Interactive Mode

Run without arguments for interactive mode:

```bash
python spotify_player.py
```

Available commands:
- `play <song name>` - Search and play a song
- `pause` - Pause playback
- `resume` - Resume playback
- `next` - Skip to next track
- `prev` - Go to previous track
- `current` - Show current track info
- `devices` - Show available Spotify devices
- `volume <0-100>` - Set volume level
- `quit` - Exit the player

### Examples

```bash
spotify> play Imagine Dragons Believer
spotify> pause
spotify> current
spotify> volume 75
spotify> next
spotify> devices
```

## Requirements

- Python 3.6+
- Active Spotify Premium account (required for playback control)
- Spotify app running on at least one device (computer, phone, etc.)

## Troubleshooting

**No devices found:**
- Make sure Spotify is open and active on at least one device
- Try playing something on Spotify first, then run the player

**Authentication errors:**
- Check that your Client ID and Client Secret are correct in `.env`
- Make sure the Redirect URI matches exactly: `http://localhost:8888/callback`
- Delete the `.cache` file and try authenticating again

**Playback control not working:**
- Spotify Premium is required for playback control via the API
- Ensure you have an active playback session on a device

## License

MIT
