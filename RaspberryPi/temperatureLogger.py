import subprocess
from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
cmd = ["vcgencmd", "measure_temp"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()


with open("temperature_data.csv", "a") as file:
    file.write(current_time + " " + o.decode("ascii"))
    file.close()
