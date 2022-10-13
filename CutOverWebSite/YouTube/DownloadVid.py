import PySimpleGUI as sg
from pytube import YouTube

def executar_download(link, path):
    video = YouTube(link)
    video.streams.get_lowest_resolution().download(output_path=path)
        
layout = [[sg.Text('Informe o Link do vídeo no YouTube'), sg.InputText()], #primeira linha
          [sg.Text('Informe o local de destino para salvar: '), sg.InputText(), sg.FolderBrowse()], #segunda linha
          [sg.Button('Baixar'), sg.Button('Cancelar')] #terceira linha
         ]

window = sg.Window('VideoDownloader', layout)

while True:
    event, values = window.read()
    if event == 'Cancelar' or event == sg.WIN_CLOSED:
        break
    elif event == 'Baixar':
        executar_download(values[0], values[1])
        sg.popup_ok('Download concluído com sucesso!')

window.close()