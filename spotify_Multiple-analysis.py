import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import re

# Setup Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="c1936cc16dd54babbc21ae58aeaaa88e",
    client_secret="ca8247d39d0c4e978a29e483aae90d49"
))

# List of Spotify track URLs
track_urls = [
    "https://open.spotify.com/track/6YcBBZVKYYRirfeAt6BeGA",  # Machi Open The Bottle - Yuvan
    "https://open.spotify.com/track/3AJwUDP919kvQ9QcozQPxg",  # Shape of You - Ed Sheeran
    "https://open.spotify.com/track/2XU0oxnq2qxCpomAAuJY8K",  # Blinding Lights - The Weeknd
    "https://open.spotify.com/track/6habFhsOp2NvshLv26DqMb",  # Believer - Imagine Dragons
    "https://open.spotify.com/track/1rqqCSm0Qe4I9rUvWncaom",  # Levitating - Dua Lipa
    "https://open.spotify.com/track/7qiZfU4dY1lWllzX7mPBI3",  # Despacito - Luis Fonsi
    "https://open.spotify.com/track/0eGsygTp906u18L0Oimnem",  # Someone Like You - Adele
    "https://open.spotify.com/track/2VxeLyX666F8uXCJ0dZF8B",  # Peaches - Justin Bieber
    "https://open.spotify.com/track/1fDsrQ23eTAVFElUMaf38X",  # Kaavaalaa - Anirudh Ravichander
    "https://open.spotify.com/track/4VqPOruhp5EdPBeR92t6lQ"   # Viva La Vida - Coldplay
]

# Collect all track metadata
track_data_list = []

for url in track_urls:
    try:
        track_id = re.search(r'track/([a-zA-Z0-9]+)', url).group(1)
        track = sp.track(track_id)
        track_data = {
            'Track Name': track['name'],
            'Artist': track['artists'][0]['name'],
            'Album': track['album']['name'],
            'Popularity': track['popularity'],
            'Duration (minutes)': track['duration_ms'] / 60000
        }
        track_data_list.append(track_data)
    except Exception as e:
        print(f"Error processing {url}: {e}")

# Convert list to DataFrame
df = pd.DataFrame(track_data_list)

# Save to CSV file
df.to_csv('Spotify_multiple_tracks.csv', index=False)

# Print the data table
print("\nSpotify Track Metadata:")
print(df)

# ------------------- Visualization -------------------
plt.figure(figsize=(12,6))

# Plot Popularity and Duration
plt.bar(df['Track Name'], df['Popularity'], label='Popularity', color='skyblue', alpha=0.7)
plt.plot(df['Track Name'], df['Duration (minutes)'] * 10,  # scaled for visual balance
         marker='o', color='orange', label='Duration (min, scaled x10)')

plt.title('Spotify Track Popularity and Duration Comparison')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Track Name')
plt.ylabel('Value')
plt.legend()
plt.tight_layout()
plt.show()
