import FreeSimpleGUI as sg

label1 = sg.Text("Seleccionar archivo para comprimir")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Elejir")

label2 = sg.Text("Seleccionar carpeta de destino      ")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Elejir")

compress_button = sg.Button("Comprimir")
window = sg.Window("Compresor de archivos", 
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2]])

window.read()
window.close()