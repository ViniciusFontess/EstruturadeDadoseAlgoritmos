import pyautogui as bot
import pyautogui 
import time

pyautogui.PAUSE = 0.3

pyautogui.click(x=37, y=137) #clicar no Google

pyautogui.click(x=298, y=89)
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press('enter')

time.sleep(9)
pyautogui.moveTo(x=407, y=443, duration = 1) #clicar na conversa
pyautogui.click(x=407, y=443)


time.sleep(2)
pyautogui.moveTo(x=899, y=1027, duration = 1)
pyautogui.click(x=899, y=1027) #clicar na barra de escrita

time.sleep(2)
pyautogui.write('EU TE AMO MUITO MEU AMOR, ESTOU BUSCANDO TE FAZER FELIZ E SERMOS INDEPENDENTES, ME DESCULPA POR ONTEM SOU UM IDIOTA')

time.sleep(2)
pyautogui.press('enter')
