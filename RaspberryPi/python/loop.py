import time
import os
import subprocess

#Automatically pulls from git every 10 seconds

print("Pulling content")
cmd = "cd /home/pi/Git/prislista/ && git pull"
returned_value = os.system(cmd)
time.sleep(10)
subprocess.Popen(['python3', '/home/pi/Git/prislista/RaspberryPi/python/loop.py'])


