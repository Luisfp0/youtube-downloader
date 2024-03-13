from pytube import YouTube
import os

def download_video(url):
    yt = YouTube(url)
    video = yt.streams.first()
    pasta = os.path.expanduser('./Downloads')
    video.download(pasta)

video_url = input('Digite a URL do vídeo: ')
download_video(video_url)
