import os
import requests
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

print("Requesting access token from Spotify...")

auth_url = 'https://accounts.spotify.com/api/token'

auth_data = {
    'grant_type':'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET
}

auth_response = requests.post(auth_url, data=auth_data)

if auth_response.status_code == 200:
    access_token = auth_response.json().get('access_token')
    print("Successfully received access token!")
    print(f"Token: {access_token[:20]}...")

else:
    print("Error getting access token:", auth_response.text)
    access_token = None


if access_token:
    playlist_id = '17HavEMnas7letvIiK9why' 
    playlist_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    params = {
        "market": "US"
    }

    print("\n--- Making The Final API Request ---")
    print(f"DEBUG: Sending request to: {playlist_url}")
    
    response = requests.get(playlist_url, headers=headers, params=params)


    if response.status_code == 200:
        print("\n>>> SUCCESS! The connection worked! <<<")
        playlist_data = response.json()
        track_count = len(playlist_data.get("items", []))
        print(f"Successfully fetched info for {track_count} tracks!")
    else:
        print("\n>>> ERROR! The request failed. See details below. <<<")
        print(f"Status Code: {response.status_code}")
        print(f"Full URL Tried: {response.url}")
        print(f"Response Reason: {response.text}")
        print("-----------------------------------------------------")


import pandas as pd

if 'playlist_data' in locals():
    # A list to hold all of our processed track info
    tracks_list = []

    for item in playlist_data.get('items', []):
        track_info = item.get('track')

        if track_info:
            track_dict = {
                'track_id': track_info.get('id'),
                'track_name': track_info.get('name'),
                'artist_name': track_info['artists'][0]['name'] if track_info['artists'] else None,
                'album_name': track_info['album']['name'] if track_info.get('album') else None,
                'popularity': track_info.get('popularity')
            }
            tracks_list.append(track_dict)

    df = pd.DataFrame(tracks_list)
    print("\nProcessed data into a pandas DataFrame:")
    print(df.head())

if not os.path.exists('data'):
        os.makedirs('data')

csv_path = 'data/spotify_playlist_tracks.csv'
df.to_csv(csv_path, index=False)

print(f"\nData successfully saved to {csv_path}")