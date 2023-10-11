import os
import re
import subprocess
from datetime import datetime

now = datetime.now()
currentTime = now.strftime("%H:%M:%S")
cmd = ["vcgencmd", "measure_temp"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()

result = o.decode("ascii")
pattern = "\d{2}"
match = int(re.search(pattern, result).group())

with open("temperature_data.csv", "a") as file:
    file.write(f"{currentTime}  {result}")
    file.close()

if match >= 80 :
    os.system("sudo reboot")