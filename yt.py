import os
from yt_dlp import YoutubeDL
#ea ai sy banaia tha 

def download_hd_video(video_url):
    # Video download krne ki settings
    ydl_opts = {
        # 'bestvideo+bestaudio' se sab se achi quality download hogi
        # 'best' backup k liye hai agar ffmpeg na ho tu 720p tak download kr ley ga
        "format": "bestvideo+bestaudio/best",
        # Downloaded file ka naam aur location (is waqt jahan script hai wahin save hogi)
        "outtmpl": "%(title)s.%(ext)s",
        # Audio aur video ko merge kr k MP4 banane k liye
        "merge_output_format": "mp4",
        "format": "best",
        "outtmpl": "%(title)s.%(ext)s",
    }

    try:
        print("Searching and downloading the best quality...")
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("\n✨ Video kamyabi se download ho gayi hai!")

    except Exception as e:
        print(
            f"\n❌ Aik galti hui hai. Shayed link ghalat hai ya FFmpeg install nahi hai. Error: {e}"
        )


if __name__ == "__main__":
    # User se link mangein ga
    link = input("YouTube Video ka Link yahan paste karein: ").strip()

    if link:
        download_hd_video(link)
    else:
        print("Aap ne koi link enter nahi kiya.")