import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account


key_path = "google_credentials.json"

# Set the environment variable for Google Cloud authentication
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_path

# --- Step 2: Define Your BigQuery Project Details ---
# Get your Project ID from the Google Cloud Console.
project_id = 'spotify-project-465312' 
dataset_id = 'spotify_data'
table_id = 'top_songs'

# --- Step 3: Load Data and Upload to BigQuery ---
# The path to your CSV file
csv_file_path = 'data/spotify_playlist_tracks.csv'

# Read the data from your CSV into a pandas DataFrame
df = pd.read_csv(csv_file_path)

print(f"Loaded {len(df)} rows from {csv_file_path}")

# The full path to the BigQuery table
table_full_path = f"{project_id}.{dataset_id}.{table_id}"

# Use pandas-gbq to upload the DataFrame to BigQuery
# 'replace' means it will overwrite the table if it already exists
df.to_gbq(table_full_path, project_id=project_id, if_exists='replace')

print(f"Data successfully uploaded to BigQuery table: {table_full_path}")