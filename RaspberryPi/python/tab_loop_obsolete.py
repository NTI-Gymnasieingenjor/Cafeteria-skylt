from datetime import datetime
from threading import Timer
import subprocess
import time
time.sleep(60)
print("Starting auto tab script")
import pyautogui

# Timer
x=datetime.today()
y=x.replace(day=x.day+1, hour=10, minute=53, second=00, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1
# Vad timern gör när den når sin tid
def Alt_Tab():

    time.sleep(15)
    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

    time.sleep(7200)

    pyautogui.keyDown('alt')
    time.sleep(.2)
    pyautogui.press('tab')
    time.sleep(.2)
    pyautogui.keyUp('alt')

    time.sleep(72000)

    subprocess.Popen(['python3', "/home/pi/Git/prislista/RaspberryPi/python/tab_loop.py"])

time.sleep(30)
# Utför det som står över
t = Timer(secs, Alt_Tab)
t.start()
