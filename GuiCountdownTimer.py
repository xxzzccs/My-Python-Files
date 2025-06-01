
import time
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

colors = {"Blue": "#6f82e1"}

sg.theme("DarkTeal4")

# Creating the layout of the window as seen by the user 
layout = [[sg.Text("Select a start time", font=(12,19), text_color="#6f82e1")],
          [sg.Button("10s", size=(3, 3)), sg.Button("30s", size=(3,3)), sg.Button("50s", size=(3, 3))],
          [sg.Multiline(size=(20, 7), key="OUT", background_color="White", reroute_stdout=True, autoscroll=False, no_scrollbar=True, write_only=True)],
          [sg.Button("Exit")]]

window = sg.Window(title="Countdown Timer", layout=layout, text_justification='center')

# Countdown function to countdown given the start time 
def countdown_timer(start_time:int):
    while start_time > 0:
        hours = start_time // 3600
        mins, secs = divmod(start_time, 60)
        countdown_time = "{:02d} {:02d} {:02d}".format(hours, mins, secs)
        print(countdown_time)
        window.refresh()
        time.sleep(1.0)
        start_time -= 1
    print("00 00 00")
    print("Your time is up. Select a new time to continue.")

#Event Loop
def gui_window():
    while True:
        event, values = window.read()
        if event in (WINDOW_CLOSED, "Exit"):
            break
        if event == "10s":
            window["OUT"].update(countdown_timer(10))
        if event == "30s":
            window["OUT"].update(countdown_timer(30))
        if event == "50s":
            window["OUT"].update(countdown_timer(50))
        
    window.close()

if __name__ == '__main__':
    gui_window()

# countdown_timer(10)    
