import PySimpleGUI as sg

layout = [  [sg.Text('Calendar')],
            [sg.In(key='-CAL-', enable_events=True, visible=False), sg.CalendarButton('Click here to open calendar', target='-CAL-', pad=None, font=('MS Sans Serif', 10, 'bold'),
                button_color=('red', 'white'), key='_CALENDAR_', format=('%d %B, %Y'))],
            [sg.Exit()]]

window = sg.Window('Calendar', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
window.close()