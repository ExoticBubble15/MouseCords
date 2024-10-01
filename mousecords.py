from tkinter import *
import pyautogui as mouse
import keyboard
    
def getPos(preface = ""):
    x, y = mouse.position()
    return (f'{preface}({x}, {y})')

def getColor(preface = ""):
    x, y = mouse.position()
    return (f'{preface}{mouse.pixel(x, y)}')

def updateText():
    if keyboard.is_pressed('enter'):
        if(getPos() not in savedCords[len(savedCords)-1]):
            savedCords.append(getPos("Pos "))
    if keyboard.is_pressed('shift'):
        if(getColor() not in savedCords[len(savedCords)-1]) or (getPos() not in savedCords[len(savedCords)-1]):
            savedCords.append(f'{getPos("Pos ")} | {getColor("RGB ")}')
    cursorCordsDisplay.config(text=getPos("Current position: "))
    cursorRGBdisplay.config(text=getColor("Current RGB: "))
    savedCordsdisplay.config(text=savedCordsString())
    window.after(1, updateText)

savedCords = [f'{getPos("Pos ")} | {getColor("RGB ")}']
def savedCordsString(includeEnd = False):
    returnString = (f'Start: {savedCords[0]}')
    if len(savedCords) <= displayCount or includeEnd: 
        startPos = 1
    else:
        startPos = len(savedCords)-displayCount
    for i in range(startPos, len(savedCords)):
        returnString += (f'\nSave {i}: {savedCords[i]}')
    if includeEnd:
        returnString += (f'\nEnd: {getPos("Pos ")} | {getColor("RGB ")}')
    return returnString

def close():
    print(savedCordsString(True))
    window.destroy()

displayCount = 20
window = Tk()

cursorCordsDisplay = Label(window, font=("Calibri", "18"), fg="black")
cursorCordsDisplay.pack()

cursorRGBdisplay = Label(window, font=("Calibri", "18"), fg="black")
cursorRGBdisplay.pack()

savedCordsdisplay = Label(window, font=("Calibri", "13"), fg="blue")
savedCordsdisplay.pack()

updateText()
window.protocol("WM_DELETE_WINDOW", close)
mainloop()