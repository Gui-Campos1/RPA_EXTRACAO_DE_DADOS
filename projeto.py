
import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3

#--------------------------------------------------------------------------------------------

#Exportar base de dados do relátorio BW SAP

# abrir o navegador (edge)

#pyautogui.press("win")
#time.sleep(5)
#pyautogui.write("edge")
#time.sleep(5)
#pyautogui.press("enter")

#tempo para cerregar o site 
#time.sleep(10)
#pyautogui.click (x=-2592, y=131)
#time.sleep(10)



#--------------------------------------------------------------------------------------------

#for _ in range(5):
 #   pyautogui.press("tab")

#time.sleep(10)

#pyautogui.press("right")
#time.sleep(3)

#for _ in range(2):
 #   pyautogui.press("enter")

#time.sleep(30)

#--------------------------------------------------------------------------------------------

#Para selecionar data

#for _ in range(6):
 #   pyautogui.press("tab")          
#time.sleep(10)

#pyautogui.press("enter")

#time.sleep(20)

#for _ in range(6):
 #   pyautogui.press("tab")
#time.sleep(5)

#pyautogui.write("01.01.2024 - 30.04.2024")

#time.sleep(5)

#for _ in range(22):
 #   pyautogui.press("tab")

#time.sleep(10)

#pyautogui.press("enter")

#time.sleep(40)

#for _ in range(10):
 #   pyautogui.press("tab")

#time.sleep(3)

#pyautogui.press("enter")
#time.sleep(20)
#--------------------------------------------------------------------------------------------

#Atualizar no Share Point

pyautogui.press("win")

time.sleep(3)
pyautogui.click (x=737, y=455)
time.sleep(3)
pyautogui.click (x=590, y=314)
time.sleep(3)
pyautogui.press("enter")

time.sleep(10)

for _ in range(2):
    pyautogui.press("tab")

pyautogui.press("enter")

time.sleep(5)
pyautogui.click (x=30, y=603)
time.sleep(5)
pyautogui.hotkey ("shift", "ctrl", "down")
time.sleep(5)


pyautogui.hotkey ("ctrl", "c",)

time.sleep(5)
#----------------------------------------------
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
time.sleep(10)
pyautogui.click (x=155, y=125)
time.sleep(10)
pyautogui.click (x=575, y=621)
time.sleep(10)
pyautogui.click (x=1681, y=233)

for _ in range(3):
    pyautogui.press("tab")

pyautogui.press("enter")  

time.sleep(10)

pyautogui.click (x=18, y=397)

pyautogui.hotkey ("ctrl", "shift", "down")
time.sleep(5)
pyautogui.hotkey ("ctrl", "v",)