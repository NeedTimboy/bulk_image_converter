import os
from PIL import Image
import PySimpleGUI as sg

# Function to convert images
def convert_images(folder, source_type, target_type):
    for file_name in os.listdir(folder):
        if file_name.endswith(source_type):
            img = Image.open(os.path.join(folder, file_name))
            if target_type == ".jpg" or target_type == ".jfif":
                img = img.convert("RGB")  # JPG/JFIF doesn't support transparency
            target_file = os.path.join(folder, os.path.splitext(file_name)[0] + target_type)
            img.save(target_file)

# Layout for the GUI
layout = [
    [sg.Text('Select Folder')],
    [sg.Input(), sg.FolderBrowse(key='-FOLDER-')],
    [sg.Text('Convert from')],
    [sg.Combo(['.jpg', '.png', '.webp', '.gif', '.jfif'], default_value='.jpg', key='-SOURCE-')],
    [sg.Text('Convert to')],
    [sg.Combo(['.jpg', '.png', '.webp', '.gif', '.jfif'], default_value='.png', key='-TARGET-')],
    [sg.Button('Convert'), sg.Button('Exit')]
]

# Create the Window
window = sg.Window("Tim's Bulk Image File Converter", layout)

# Event Loop to process events
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Convert':
        folder = values['-FOLDER-']
        source_type = values['-SOURCE-']
        target_type = values['-TARGET-']
        if folder and source_type and target_type and source_type != target_type:
            convert_images(folder, source_type, target_type)
            sg.popup('Conversion Complete!')
        else:
            sg.popup('Please select a valid folder and ensure source and target types are different!')

window.close()
