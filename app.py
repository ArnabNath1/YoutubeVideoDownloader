import streamlit as st
from pytube import YouTube
import os

# Function to download YouTube video
def download_video(url, selected_quality):
    try:
        yt = YouTube(url)
        st.write("Video Title:", yt.title)
        st.write("Downloading...")
        stream = yt.streams.filter(progressive=True, file_extension='mp4').get_by_resolution(selected_quality)
        download_path = os.path.join(os.path.expanduser("~\Downloads"))
        stream.download(output_path=download_path)
        st.success("Download completed successfully!")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Streamlit UI
st.title("YouTube Video Downloader")

url = st.text_input("Enter YouTube Video URL:", "")
quality_options = ["1080p", "720p", "480p", "360p"]

selected_quality = st.selectbox("Select Video Quality:", quality_options)

if st.button("Download"):
    if url.strip() == "":
        st.warning("Please enter a YouTube video URL.")
    else:
        download_video(url, selected_quality)