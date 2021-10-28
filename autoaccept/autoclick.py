import win32api
import time
import pyautogui

def rueditaState():
    boton5 = win32api.GetKeyState(0x05) #0x05 = boton 5 del mouse
    return boton5

def click():
    if rueditaState() == -128 or rueditaState() == -127:
        pyautogui.click()

def cerrar():
    k = win32api.GetKeyState(0x4B) #0x4B = 'K'
    if k == -127 or k == -128:
        quit()

while True:
    cerrar()
    click()