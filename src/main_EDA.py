#!/usr/bin/env python
# coding: utf-8

# Import necessary libraries
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import warnings as w
w.filterwarnings('ignore')  # Suppress warnings

# Get current and parent directory paths
import os
root_path = os.getcwd()
parent_directory = os.path.dirname(root_path)
print("Root directory path:", parent_directory)

# Load Spotify dataset
df = pd.read_csv(parent_directory + '/data/Most Streamed Spotify Songs 2024.csv', encoding='latin1')
df.head(5)

# View column names
df.columns

# Check for missing values in the dataset
df.isna().sum()

# Drop 'TIDAL Popularity' column due to too many missing values
df.drop("TIDAL Popularity", axis=1, inplace=True)

# Get top 50 albums by frequency
top_albums = df['Album Name'].value_counts().nlargest(50)
top_albums_df = top_albums.reset_index()
top_albums_df.columns = ['Album Name', 'Count']

# Plot: Top 50 albums by count
plt.figure(figsize=(15, 5))
sn.barplot(x='Album Name', y='Count', data=top_albums_df, palette='viridis')
plt.title('Top 50 Albums by Count', fontsize=15)
plt.xlabel('Album Name', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.savefig(parent_directory + "/results/Top 50 Albums by Count.png", bbox_inches='tight')
plt.show()

# Get top 50 tracks by frequency
top_tracks = df['Track'].value_counts().nlargest(50)
top_tracks_df = top_tracks.reset_index()
top_tracks_df.columns = ['Track Name', 'Count']

# Plot: Top 50 tracks by count
plt.figure(figsize=(15, 5))
sn.barplot(x='Track Name', y='Count', data=top_tracks_df, palette='viridis')
plt.title('Top 50 Tracks by Count', fontsize=15)
plt.xlabel('Track Name', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.savefig(parent_directory + "/results/Top 50 Track by Count.png", bbox_inches='tight')
plt.show()

# Get top 50 artists by frequency
top_artists = df['Artist'].value_counts().nlargest(50)
top_artists_df = top_artists.reset_index()
top_artists_df.columns = ['Artist Name', 'Count']

# Plot: Top 50 artists by count
plt.figure(figsize=(15, 5))
sn.barplot(x='Artist Name', y='Count', data=top_artists_df, palette='viridis')
plt.title('Top 50 Artists by Count', fontsize=15)
plt.xlabel('Artist Name', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.savefig(parent_directory + "/results/Top 50 Artist by Count.png", bbox_inches='tight')
plt.show()

# Select top and bottom artists based on 'All Time Rank'
top_20_artist = df[['Artist', 'All Time Rank']].head(20)
least_20_artist = df[['Artist', 'All Time Rank']].tail(20)

# Plot: Top 20 artists by Spotify rank
plt.title("Top 20 Artists by Rank on Spotify")
plt.xlabel("Artist Name")
sn.barplot(x=top_20_artist['Artist'], y=top_20_artist['All Time Rank'], palette='viridis')
plt.xticks(rotation=65)
plt.savefig(parent_directory + "/results/TOP 20 ARTIST BY RANK ON SPOTIFY.png", bbox_inches='tight')
plt.show()

# Plot: Least popular 20 artists by Spotify rank
plt.title("Least Popular Top 20 Artists by Rank on Spotify")
plt.xlabel("Artist Name")
plt.ylabel("All Time Rank")
sn.barplot(x=least_20_artist['Artist'], y=least_20_artist['All Time Rank'], palette='viridis')
plt.xticks(rotation=75)
plt.savefig(parent_directory + "/results/LEAST POPULAR TOP 20 ARTIST BY RANK ON SPOTIFY.png", bbox_inches='tight')
plt.show()

# Prepare detailed info for top 20 tracks
about_track = df[['Track', 'Album Name', 'Artist', 'Track Score']]
top_20_tracks = about_track.head(20)

# Plot: Track Score vs Track, Album, Artist
fig, axes = plt.subplots(3, 1, figsize=(14, 18))
sn.barplot(x='Track Score', y='Track', data=top_20_tracks, ax=axes[0], palette='coolwarm')
axes[0].set_title('Track Score vs. Track')
sn.barplot(x='Track Score', y='Album Name', data=top_20_tracks, ax=axes[1], palette='viridis')
axes[1].set_title('Track Score vs. Album Name')
sn.barplot(x='Track Score', y='Artist', data=top_20_tracks, ax=axes[2], palette='magma')
axes[2].set_title('Track Score vs. Artist')
plt.tight_layout()
plt.savefig(parent_directory + "/results/Track Score vs. Track-Track Score vs. Album Name-Track Score vs. Artist.png", bbox_inches='tight')
plt.show()

# Plot: Track vs Spotify Playlist Reach by Artist
plt.figure(figsize=(12, 8))
sn.lineplot(x='Track', y='Spotify Playlist Reach', data=df.head(20), hue="Artist", marker='o')
plt.xlabel('Track', color='Red')
plt.ylabel('Spotify Playlist Reach', color='Red')
plt.xticks(rotation=90, color='blue')
plt.yticks(color='blue')
plt.title('Track vs Spotify Playlist Reach by Artist', color='blue')
plt.savefig(parent_directory + "/results/Track vs Spotify Playlist Reach by Artist.png", bbox_inches='tight')
plt.show()

# Plot: Artist vs Spotify Playlist Reach by Albums
plt.figure(figsize=(12, 8))
sn.lineplot(x='Artist', y='Spotify Playlist Reach', data=df.head(15), hue="Album Name", marker='o', dashes=True)
plt.xlabel('Artist', color='Red')
plt.ylabel('Spotify Playlist Reach', color='Red')
plt.xticks(rotation=90, color='blue')
plt.yticks(color='blue')
plt.title('Artist vs Spotify Playlist Reach by Albums', color='blue')
plt.savefig(parent_directory + "/results/Artist vs Spotify Playlist Reach by Albums.png", bbox_inches='tight')
plt.show()

# Plot: Track vs Spotify Streams by Artist
plt.figure(figsize=(12, 8))
sn.barplot(x='Track', y='Spotify Streams', data=df.head(20), hue="Artist", palette='Reds')
plt.xlabel('Track', color='Red')
plt.ylabel('Spotify Streams', color='Red')
plt.xticks(rotation=90, color='blue')
plt.yticks(color='blue')
plt.title('Track vs Spotify Streams by Artist', color='blue')
plt.savefig(parent_directory + "/results/Track vs Spotify Streams Reach by Artist.png", bbox_inches='tight')
plt.show()

# Plot: Artist vs Spotify Popularity by Album
plt.figure(figsize=(12, 8))
sn.barplot(x='Artist', y='Spotify Popularity', data=df.head(20), hue="Album Name", palette='Reds')
plt.xlabel('Artist', color='Red')
plt.ylabel('Spotify Popularity', color='Red')
plt.xticks(rotation=90, color='blue')
plt.yticks(color='blue')
plt.title('Artist vs Spotify Popularity by Albums', color='blue')
plt.savefig(parent_directory + "/results/Artist vs Spotify Popularity by Albums.png", bbox_inches='tight')
plt.show()

# Plot: Artist vs YouTube Views by Albums
plt.figure(figsize=(12, 8))
sn.scatterplot(x='Artist', y='YouTube Views', data=df.head(20), hue="Album Name", palette='coolwarm', s=150)
plt.xlabel('Artist', color='green')
plt.ylabel('YouTube Views', color='green')
plt.xticks(rotation=45, color='black')
plt.yticks(color='black')
plt.title('Artist vs YouTube Views by Albums', color='violet')
plt.savefig(parent_directory + "/results/Artist vs YouTube Views by Albums.png", bbox_inches='tight')
plt.show()
