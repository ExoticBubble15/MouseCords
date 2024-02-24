from tkinter import *
import pyautogui as mouse
import keyboard
    
def getPos(preface = ""):
    x, y = mouse.position()
    return (f'{preface}({x}, {y})')

def updateText():
    if keyboard.is_pressed('enter'):
        if(savedCords[len(savedCords)-1] != getPos()):
            savedCords.append(getPos())

    cursorCordsdisplay.config(text=getPos("Current position: "))
    savedCordsdisplay.config(text=savedCordsString())
    window.after(1, updateText)

savedCords = [getPos()]
def savedCordsString(includeEnd = False):
    returnString = (f'Start: {savedCords[0]}')

    if len(savedCords) <= displayCount or includeEnd: 
        startPos = 1
    else:
        startPos = len(savedCords)-displayCount
    for i in range(startPos, len(savedCords)):
        returnString += (f'\nSave {i}: {savedCords[i]}')

    if includeEnd:
        returnString += (f'\nEnd: {getPos()}')
    return returnString

def close():
    print(savedCordsString(True))
    window.destroy()

displayCount = 20
window = Tk()

cursorCordsdisplay = Label(window, font=("Calibri", "18"), fg="black")
cursorCordsdisplay.pack()

savedCordsdisplay = Label(window, font=("Calibri", "13"), fg="blue")
savedCordsdisplay.pack()

updateText()
window.protocol("WM_DELETE_WINDOW", close)
mainloop()