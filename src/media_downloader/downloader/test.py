import yt_dlp


url = input("URL: ")

with yt_dlp.YoutubeDL() as ydl:
    metadata = ydl.extract_info(url, download=False)

print(metadata["webpage_url"])