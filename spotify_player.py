#!/usr/bin/env python3
"""
Spotify Player - Control Spotify playback through the Spotify Web API
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import sys
import config

class SpotifyPlayer:
    def __init__(self):
        """Initialize Spotify player with authentication."""
        try:
            config.validate_config()
            self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                client_id=config.SPOTIFY_CLIENT_ID,
                client_secret=config.SPOTIFY_CLIENT_SECRET,
                redirect_uri=config.SPOTIFY_REDIRECT_URI,
                scope=config.SPOTIFY_SCOPE
            ))
            print("✓ Successfully authenticated with Spotify")
        except Exception as e:
            print(f"✗ Authentication failed: {e}")
            sys.exit(1)

    def get_available_devices(self):
        """Get list of available Spotify devices."""
        try:
            devices = self.sp.devices()
            if devices['devices']:
                print("\nAvailable devices:")
                for idx, device in enumerate(devices['devices']):
                    active = "🔊 ACTIVE" if device['is_active'] else ""
                    print(f"  {idx + 1}. {device['name']} ({device['type']}) {active}")
                return devices['devices']
            else:
                print("✗ No active Spotify devices found. Please open Spotify on a device.")
                return []
        except Exception as e:
            print(f"✗ Error getting devices: {e}")
            return []

    def search_track(self, query, limit=5):
        """Search for tracks on Spotify."""
        try:
            results = self.sp.search(q=query, type='track', limit=limit)
            tracks = results['tracks']['items']
            
            if tracks:
                print(f"\nSearch results for '{query}':")
                for idx, track in enumerate(tracks):
                    artists = ', '.join([artist['name'] for artist in track['artists']])
                    print(f"  {idx + 1}. {track['name']} - {artists}")
                return tracks
            else:
                print(f"✗ No tracks found for '{query}'")
                return []
        except Exception as e:
            print(f"✗ Error searching tracks: {e}")
            return []

    def play_track(self, track_uri=None, device_id=None):
        """Play a specific track or resume playback."""
        try:
            if track_uri:
                self.sp.start_playback(device_id=device_id, uris=[track_uri])
                print(f"▶ Playing track")
            else:
                self.sp.start_playback(device_id=device_id)
                print("▶ Resuming playback")
            return True
        except Exception as e:
            print(f"✗ Error playing track: {e}")
            return False

    def pause_playback(self):
        """Pause current playback."""
        try:
            self.sp.pause_playback()
            print("⏸ Paused playback")
            return True
        except Exception as e:
            print(f"✗ Error pausing playback: {e}")
            return False

    def next_track(self):
        """Skip to next track."""
        try:
            self.sp.next_track()
            print("⏭ Skipped to next track")
            return True
        except Exception as e:
            print(f"✗ Error skipping track: {e}")
            return False

    def previous_track(self):
        """Go to previous track."""
        try:
            self.sp.previous_track()
            print("⏮ Went to previous track")
            return True
        except Exception as e:
            print(f"✗ Error going to previous track: {e}")
            return False

    def get_current_playback(self):
        """Get information about current playback."""
        try:
            current = self.sp.current_playback()
            if current and current['item']:
                track = current['item']
                artists = ', '.join([artist['name'] for artist in track['artists']])
                is_playing = "▶" if current['is_playing'] else "⏸"
                print(f"\n{is_playing} Now playing: {track['name']} - {artists}")
                print(f"   Album: {track['album']['name']}")
                return current
            else:
                print("✗ No track currently playing")
                return None
        except Exception as e:
            print(f"✗ Error getting current playback: {e}")
            return None

    def set_volume(self, volume_percent):
        """Set playback volume (0-100)."""
        try:
            if 0 <= volume_percent <= 100:
                self.sp.volume(volume_percent)
                print(f"🔊 Volume set to {volume_percent}%")
                return True
            else:
                print("✗ Volume must be between 0 and 100")
                return False
        except Exception as e:
            print(f"✗ Error setting volume: {e}")
            return False

    def play_music(self, search_query=None):
        """Main function to play music on Spotify."""
        # Check for available devices
        devices = self.get_available_devices()
        if not devices:
            return False

        # Get active device or use first available
        active_device = None
        for device in devices:
            if device['is_active']:
                active_device = device['id']
                break
        if not active_device and devices:
            active_device = devices[0]['id']

        # If search query provided, search and play
        if search_query:
            tracks = self.search_track(search_query, limit=1)
            if tracks:
                track_uri = tracks[0]['uri']
                return self.play_track(track_uri, device_id=active_device)
        else:
            # Just resume playback
            return self.play_track(device_id=active_device)

        return False


def main():
    """Main entry point for the Spotify player."""
    print("🎵 Spotify Player")
    print("=" * 50)

    # Initialize player
    player = SpotifyPlayer()

    # Check command line arguments
    if len(sys.argv) > 1:
        # Join all arguments as search query
        search_query = ' '.join(sys.argv[1:])
        print(f"\nSearching for: {search_query}")
        player.play_music(search_query)
    else:
        # Interactive mode
        print("\nCommands:")
        print("  play <song name>  - Search and play a song")
        print("  pause             - Pause playback")
        print("  resume            - Resume playback")
        print("  next              - Skip to next track")
        print("  prev              - Go to previous track")
        print("  current           - Show current track")
        print("  devices           - Show available devices")
        print("  volume <0-100>    - Set volume")
        print("  quit              - Exit")
        print()

        while True:
            try:
                command = input("spotify> ").strip().lower()
                
                if not command:
                    continue
                
                if command == 'quit' or command == 'exit':
                    print("Goodbye!")
                    break
                elif command.startswith('play '):
                    query = command[5:]
                    player.play_music(query)
                elif command == 'pause':
                    player.pause_playback()
                elif command == 'resume':
                    player.play_track()
                elif command == 'next':
                    player.next_track()
                elif command == 'prev' or command == 'previous':
                    player.previous_track()
                elif command == 'current':
                    player.get_current_playback()
                elif command == 'devices':
                    player.get_available_devices()
                elif command.startswith('volume '):
                    try:
                        vol = int(command[7:])
                        player.set_volume(vol)
                    except ValueError:
                        print("✗ Invalid volume value. Use a number between 0-100")
                else:
                    print(f"✗ Unknown command: {command}")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"✗ Error: {e}")


if __name__ == "__main__":
    main()
