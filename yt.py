import os
# from yt_dlp import YoutubeDL
# #ea ai sy banaia tha 
# #  08/06/2026 python 02:31:00
# #  09/06/2026 python 03:00:00
# #  12/06/2026
# #  13/06/2026
# def download_hd_video(video_url):
#     # Video download krne ki settings
#     ydl_opts = {
#         # 'bestvideo+bestaudio' se sab se achi quality download hogi
#         # 'best' backup k liye hai agar ffmpeg na ho tu 720p tak download kr ley ga
#         "format": "bestvideo+bestaudio/best",
#         # Downloaded file ka naam aur location (is waqt jahan script hai wahin save hogi)
#         "outtmpl": "%(title)s.%(ext)s",
#         # Audio aur video ko merge kr k MP4 banane k liye
#         "merge_output_format": "mp4",
#         "format": "best",
#         "outtmpl": "%(title)s.%(ext)s",
#     }

#     try:
#         print("Searching and downloading the best quality...")
#         with YoutubeDL(ydl_opts) as ydl:
#             ydl.download([video_url])
#         print("\n✨ Video kamyabi se download ho gayi hai!")

#     except Exception as e:
#         print(
#             f"\n❌ Aik galti hui hai. Shayed link ghalat hai ya FFmpeg install nahi hai. Error: {e}"
#         )


# if __name__ == "__main__":
#     # User se link mangein ga
#     link = input("YouTube Video ka Link yahan paste karein: ").strip()

#     if link:
#         download_hd_video(link)
#     else:
#         print("Aap ne koi link enter nahi kiya.")

import yt_dlp
#  ea ytsy mp3 download krny k lea code hy
#  ea code meny  Ai sy copy kia tha 
def download_youtube_as_mp3(video_url):
    # Configuration options for yt-dlp
    ydl_opts = {
        # Select the best quality audio stream available
        'format': 'bestaudio/best',
        # Restrict filenames to handle special characters cleanly
        'restrictfilenames': True,
        # Define how the output file should be named and where to save it
        'outtmpl': '%(title)s.%(ext)s',
        # Tell yt-dlp to extract the audio and convert it via FFmpeg
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # Bitrate quality (e.g., 192 or 320 kbps)
        }],
    }

    try:
        print("Starting download and conversion... Please wait.")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download and MP3 conversion successful!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Replace with the URL of the YouTube video you want to convert
    url = input("Enter the YouTube URL: ").strip()
    download_youtube_as_mp3(url)