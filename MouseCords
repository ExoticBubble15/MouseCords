from tkinter import *
import pyautogui as mouse
import keyboard
    
def getPos(preface = ""):
    x, y = mouse.position()
    return preface + "(" + str(x) + ", " + str(y) + ")"

def updateText():
    if keyboard.is_pressed('space'):
        if(savedCords[len(savedCords)-1] != getPos()):
            savedCords.append(getPos())
    cursorCordsdisplay.config(text=getPos("Current position: "))
    savedCordsdisplay.config(text=savedCordsString())
    window.after(1, updateText)

savedCords = [getPos()]
def savedCordsString(includeEnd = False):
    returnString = "Start: " + savedCords[0]
    for i in range(1, len(savedCords)):
        returnString += "\nSave " + str(i) + ": " + savedCords[i]
    if includeEnd:
        returnString += "\nEnd: " + getPos()
    return returnString

def close():
    print(savedCordsString(True))
    window.destroy()

window = Tk()

cursorCordsdisplay = Label(window, font=("Calibri", "18"), fg="black")
cursorCordsdisplay.pack()

savedCordsdisplay = Label(window, font=("Calibri", "13"), fg="blue")
savedCordsdisplay.pack()

updateText()
window.protocol("WM_DELETE_WINDOW", close)
mainloop()
