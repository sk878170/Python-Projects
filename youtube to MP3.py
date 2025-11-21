from pytube import YouTube

def download_youtube_video(url, output_path):
    try:
        video = YouTube(url)
        print("Available streams:")
        for stream in video.streams.filter(file_extension="mp4"):
            print(stream)

        # Attempt to get stream by itag 22, but also handle if itag 22 is not available
        stream = video.streams.get_by_itag(140)
        if stream is None:
            raise ValueError("itag 22 is not available for this video")

        print(f"Downloading stream: {stream}")
        stream.download(output_path)
        print(f"Downloaded to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Usage
download_youtube_video("https://youtu.be/y7MW7d8fb1Y?si=Vw5IScT9d9TbDIG1", r"C:\Users\shubh\Music")
