# Spotify--Data-Engineering-Analytics
# 🎵 Spotify Song Metadata Analysis

This project demonstrates a **Data Engineering + Data Analysis workflow** using the **Spotify Web API**.  
It fetches detailed metadata about songs (like track name, artist, album, popularity, and duration), stores it using **pandas**, and visualizes insights with **matplotlib**.

---

## 📘 Project Overview

This project connects to the **Spotify Developer API** through the `spotipy` library to extract metadata for a specific track or playlist.  
The goal is to showcase how to:
- Authenticate using Spotify’s **Client Credentials Flow**
- Extract structured song data
- Clean and store it using **pandas**
- Visualize key metrics like song popularity and duration

---

## 🧠 Tech Stack

| Category | Technology |
|-----------|-------------|
| Language | Python |
| API | Spotify Web API |
| Libraries | spotipy, pandas, matplotlib, re |
| Data Storage | CSV (local) |
| IDE | PyCharm / Jupyter Notebook |

---

## ⚙️ How It Works

1. **Spotify API Setup**
   - Created an app on [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
   - Used the generated `client_id` and `client_secret` for authentication.

2. **Extract Track Data**
   - Fetched a song’s metadata using its Spotify track URL.
   - Example track: *“Machi Open the Bottle”* by Yuvan Shankar Raja.

3. **Transform Data**
   - Parsed relevant fields such as:
     - Track name  
     - Artist  
     - Album  
     - Popularity  
     - Duration (in minutes)

4. **Load & Visualization**
   - Saved the extracted data as `Spotify_track_data.csv`
   - Visualized track popularity and duration using **bar charts**.

---

## 📊 Sample Output

**Data Preview:**
| Track Name | Artist | Album | Popularity | Duration (minutes) |
|-------------|---------|--------|-------------|--------------------|
| Machi Open the Bottle | Yuvan Shankar Raja | Anjaan (Original Motion Picture Soundtrack) | 54 | 4.23 |

**Visualization Example:**
A simple bar chart comparing popularity vs duration for the track.

---

## 🚀 Future Improvements

- Extend analysis to entire **playlists** or **artists**
- Integrate **audio features** (danceability, energy, tempo, etc.)
- Store data in a **SQL database** or **data warehouse**
- Build a **Streamlit dashboard** for interactive insights

---
