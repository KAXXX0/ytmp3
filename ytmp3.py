import tkinter as tk
import pytube
import os

def download():
    # Get the URL from the text entry field
    url = url_entry.get()

    # Create a PyTube YouTube object
    yt = pytube.YouTube(url)

    # Get the highest quality audio stream and download it
    stream = yt.streams.filter(only_audio=True).first()

    # Update the status label to show that the download has started
    status_label.config(text="Downloading...")

    # Download the stream and rename the file to have an mp3 extension
    stream.download()
    os.rename(stream.default_filename, stream.default_filename[:-4] + ".mp3")

    # Update the status label to show that the download is complete
    status_label.config(text="Download Complete! You may exit.")

# Create the main window
window = tk.Tk()
window.geometry("800x600")

# Create a label for the URL entry field
url_label = tk.Label(window, text="Enter the URL of a YouTube video:")
url_label.pack()

# Create a text entry field for the URL
url_entry = tk.Entry(window)
url_entry.pack()

# Create a button to start the download
download_button = tk.Button(window, text="Download", command=download)
download_button.pack()

# Create a label to show the status of the download
status_label = tk.Label(window, text="")
status_label.pack()

# Run the main event loop
window.mainloop()