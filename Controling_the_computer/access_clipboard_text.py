import pyautogui
import pyperclip

position =  pyautogui.position()
print(position)

# open a txt file
pyautogui.doubleClick(132, 200)


pyautogui.press("down")
pyautogui.press("enter")

pyautogui.write("controlling this freeky pc")

pyautogui.hotkey("ctrl","a")
pyautogui.hotkey("ctrl", "c")

text = pyperclip.paste()
print(text)

