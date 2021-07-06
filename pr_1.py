import PySimpleGUI as sg

# Define the window's contents
layout = [[sg.Text("What's your name?")],
          [sg.Input()],
          [sg.Button('Ok')]]

# Create the window
window = sg.Window('Window Title', layout)

# Display and interact with the Window
event, values = window.read()

# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()  