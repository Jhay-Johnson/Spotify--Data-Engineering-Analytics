import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import matplotlib.pyplot as plt
import re

# Initialize Spotify client credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="c1936cc16dd54babbc21ae58aeaaa88e",
    client_secret="ca8247d39d0c4e978a29e483aae90d49"
))

# Define track URL (Machi Open the Bottle - Yuvan)
track_url = "https://open.spotify.com/track/6YcBBZVKYYRirfeAt6BeGA"

# Extract track ID from URL using regex
track_id = re.search(r'track/([a-zA-Z0-9]+)', track_url).group(1)

# Fetch track details from Spotify API
track = sp.track(track_id)

# Extract key metadata
track_data = {
    'Track Name': track['name'],
    'Artist': track['artists'][0]['name'],
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}

# Display track metadata
print(f"\nTrack Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")

# Convert metadata to DataFrame
df = pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

# Save metadata to CSV file
df.to_csv('Spotify_track_data.csv', index=False)

# Visualize popularity and duration
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8, 5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('Value')
plt.show()
