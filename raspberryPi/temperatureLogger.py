# This file only works on linux
# vcgencmd measure_temp and sudo reboot are linux commands and should be change if you are using another OS

import os
import re
import subprocess
from datetime import datetime

now = datetime.now()
currentTime = now.strftime("%Y-%m-%d %H:%M:%S")
cmd = ["vcgencmd", "measure_temp"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()

result = o.decode("ascii")
# Find the temperature in the string by looking for two digits in a row
pattern = "\d{2}"
match = int(re.search(pattern, result).group())

# Log the temperature and time to "temperature_data.csv"
with open("temperature_data.csv", "a") as file:
    file.write(f"{currentTime}  {result}")
    file.close()


# If the temperature is above 80 degrees celsius, reboot the system
if match >= 80:
    os.system("sudo reboot")
