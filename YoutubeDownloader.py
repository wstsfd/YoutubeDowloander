# youtube downloader.py

import PySimpleGUI as sg
import os.path
from pytube import YouTube

# First the window layout in 2 columns

file_list_column = [
    [
        sg.Text("Youtube URL:"),
        sg.InputText(default_text='paste Youtube URL here',size=(40, 1), enable_events=True, key="-URL-"),
        #sg.FolderBrowse(),
        
        #define a button to recall the videolists
    ],
    [
        sg.Text("Output Folder:"),
        sg.In(size=(40, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
        
    ],
    [
        sg.Button(button_text='Show Streams', key='-STREAMS-') #show stream lists
        #define a button to recall the videolists
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(100, 20), key="-URL LIST-"
        )
    ],
]

video_download_column = [

    [sg.Text("Choose the tag number from stream list:")],
    [sg.InputText(size=(10, 1), enable_events=True, key="-TAG-")],
    #[sg.Image(key="-IMAGE-")], #image reviewer
    [sg.Button(button_text='download chosed stream', key='-DOWNLOAD-')],
    [sg.Button(button_text='download the best quality directly', key='-DOWNLOAD BEST-')]
]
# For now will only show the name of the file that was chosen

# ----- Full layout -----
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeperator(),
        sg.Column(video_download_column),
        #only one column
    ]
]

window = sg.Window("Youtube Downloader", layout)

# Run the Event Loop

yt = None
location = ''
while True:
    event, values = window.read()
    

    print(event)
    print(values)
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

    if event == '-STREAMS-':
        try:
            URL=values['-URL-']
            yt = YouTube(URL)
            window['-URL LIST-'].update(yt.streams)
            # how to get the folder path?
            location = values['-FOLDER-']
            print(URL)
        except:
            pass

        
    if event == '-DOWNLOAD-':
        try:
            tag = values['-TAG-']
            ys = yt.streams.get_by_itag(tag)
            ys.download(location)
            print('You entered ', values)
            print('You entered ', event)

        except:
            print('excpetion happened in Download')
            pass
 
    if event == '-DOWNLOAD BEST-':
        ys = yt.streams.get_highest_resolution()
        ys.download(location)

        print('this time')
       #try:
           
       #except:
        #   print('Exception happened in Download Best')
         #  pass
        
window.close()
