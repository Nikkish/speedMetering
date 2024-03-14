import PySimpleGUI as sg
from main import *

layout = [
    [sg.Text('Выберите скорость выспроизведения потока видеокадров для обработки:'), sg.Slider(orientation ='horizontal', key='stSlider', range=(1,100)), sg.Button('Запуск')],
    [sg.Text('Скорость объекта на взлете: ' + 'м/с', key='ress')]
]
window = sg.Window('111', layout)
while True:                             
    event, values = window.read()
    if event in (None, 'Exit', 'Cancel'):
        break
    elif event == 'Запуск':
        oo = NewW()
        res = oo.estimateSpeedNew()
        window['ress'].update(res)







  