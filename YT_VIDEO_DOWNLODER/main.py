from pytube import YouTube
from tkinter import Tk
from tkinter import filedialog

def download_video(url, save_path):
  try:
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension='mp4')
    high_resolution_video = streams.get_highest_resolution()
    high_resolution_video.download(output_path=save_path)
    print('Video Downloaded Successfully!')
  except Exception as e:
    print(e)

def open_file_dialog():
 folder = filedialog.askdirectory()
 if folder:
   print(f"selected folder: {folder}")
 return folder


if __name__ == '__main__':
  window = Tk()
  window.withdraw()

  video_url = input('Enter a youtube video url: ')
  save_path = open_file_dialog()

  if save_path:
    print('Download Started...')
    download_video(video_url, save_path)
  else:
    print("invalid location")