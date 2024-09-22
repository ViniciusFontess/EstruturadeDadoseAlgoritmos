import pyautogui 
import pyautogui as bot
import time

##print(pyautogui.position())
##print(pyautogui.size())

pyautogui.PAUSE = 0.3

time.sleep(2)
pyautogui.click(x=37, y=137) #clicar no Google

pyautogui.click(x=840, y=48) #clicar no na Nova aba

pyautogui.click(x=410, y=90)

pyautogui.write('https://www.hashtagtreinamentos.com/')

pyautogui.press('enter')

time.sleep(3)
pyautogui.moveTo(x=649, y=204, duration = 1)
pyautogui.click(x=970, y=312)