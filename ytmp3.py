import os
import pytube


def on_progress(stream, chunk, remaining):
    """
    Show the download progress as a percentage.
    """
    downloaded = stream.filesize - remaining
    percent = (downloaded / stream.filesize) * 100
    print(f"Downloading... {percent:.2f}% complete")


def download(url):
    """
    Download the audio from a YouTube video using PyTube and return the filename.
    """
    yt = pytube.YouTube(url, on_progress_callback=on_progress)
    stream = yt.streams.filter(only_audio=True).first()
    stream.download()
    filename = stream.default_filename[:-4] + ".mp3"
    os.rename(stream.default_filename, filename)
    return filename


if __name__ == "__main__":
    url = input("Enter the URL of a YouTube video: ")
    filename = download(url)
    print(f"Download complete. Audio saved as {filename}.")
