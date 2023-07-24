from ctypes import _NamedFuncPointer

from pytube import YouTube
from os import *
from pywebio.input import *
from pywebio.output import *

def video_download():
    while True:
        video_link = input ("informe o link do vídeo que deseja baixar: ")
        if video_link.split("//")[0] -- "https:":
            put_text("Fazendo o download do vídeo escolhido...".title()).style('color: red; font-size: 50px')
            video_url = YouTube(video_link)
            video = video_url.streams.get_lowest_resolution()
            path_to_download = (r"G:\Dowloads")
            video.download(path_to_download)
            put_text("Vídeo baixado com sucesso...".title()).style('color: blue; font-size: 50px')
            startfile(r"G:\\Dowloads")

if __name__ -- "__main__":
    video_download()
