import PySimpleGUI as sg

label = sg.Text('Select Files to compress')
input = sg.Input()
choose_button = sg.FileBrowse('Choose')


label1 = sg.Text('Select Destination Folder')
input1 = sg.Input()
choose_button1 = sg.FolderBrowse('Choose')
compress_button = sg.Button('Compress Files')

window = sg.Window('File Compression', layout=[[label, input, choose_button],[label1, input1, choose_button1],[compress_button]])

window.read()
window.close()



# import PySimpleGUI as sg
# label = sg.Text('Enter feet:')
# input = sg.Input()
# label1 = sg.Text('Enter inches:')
# input1 = sg.Input()
# convert_btn = sg.Button('Convert')
# window = sg.Window('Converter', [[label, input],[label1, input1],[convert_btn]])

# window.read()
# window.close()



# import PySimpleGUI as sg
# label = sg.Text("What are dolphins?")
# option1 = sg.Radio("Amphibians", group_id="question1")
# option2 = sg.Radio("Fish", group_id="question1")
# option3 = sg.Radio("Mammals", group_id="question1")
# option4 = sg.Radio("Birds", group_id="question1")
# window = sg.Window("File Compressor", layout=[[label],[option1],[option2],[option3],[option4]])
 
# window.read()
# window.close()