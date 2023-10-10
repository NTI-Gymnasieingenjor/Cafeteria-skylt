# Instructions for usage

## Introduction

#### Basics of booting up RaspberryPi.
The Pi's power cable uses a USB-C port so make sure it is connected to the electrical grid you are using.  
The Pi's micro-HDMI port can also be connected to a screen to make sure the Pi's boot-up script works properly.  

#### Basics of interface
To access the interface in the RaspberryPi OS, press your '⊞ Win' or home key button.  
From here you can select three relevant categories (all listed below) of the Pi when making changes.  
| Preferences | Accessories | Logout |  

#### Basics of 'Preferences'
In 'Preferences' you will find 'Raspberry Pi Configuration'.  
In 'Raspberry Pi Configuration' you have: | System | Interfaces | Performance | Localisation |  

System is primarily for changing the username and password.  

Interfaces, in this example, is used for toggling VNC, which allows screen connect through other devices via IP.  

Performance has the selection of overclocking (*NOT RECOMMENDED*) and GPU memory,  
which may be adjusted accordingly in order to avoid overheating.  

Localisation allows you to set the Locale, Timezone, Keyboard and WiFi Country, not relevant in this example.  

#### Basics of 'Accessories'
In 'Accessories' you will find 'File Manager' and 'Terminal'.  
'File Manager' is where you access the 'Cafeteria-skylt' folder, which is located on the SD-card of this Pi.   
The folder location: '/home/pi/Git/Cafeteria-skylt'

'Terminal' is the command prompt of Pi, here you will use many useful commands.  
Some basic commands include:
- sudo raspi-config (opens up base configuration)
- cd <*path*> (changes directory)
- ls <*path*> (lists the directory)
- hostname -I (shows the IP-address of the Pi)
- cat /sys/class/thermal/thermal_zone0/temp (shows the temperature of the Pi in °C (divide by 1000))

#### Basics of 'Logout'
'Logout' uses | Shutdown | Reboot | Logout |  
'Shutdown' shuts down the Pi, allowing you to safely pull the cable, or you can write 'sudo shutdown -h now' in 'Terminal'.  
'Reboot' reboots the Pi, or you can write 'sudo shutdown -r now' in 'Terminal'.  
'Logout' logs you out from the currently active user.  

***

## Getting started with the Raspberry Pi
[Instructions](https://github.com/NTIG-Uppsala/Cafeteria-skylt/blob/main/Documentations/raspberrySetup.md)

[Autostart](https://github.com/NTIG-Uppsala/Cafeteria-skylt/blob/main/Documentations/Autostart.md)

***

## Environments and Languages 
[Documentation](https://github.com/NTIG-Uppsala/Cafeteria-skylt/blob/main/Documentations/Enviroments_Languages.md)

***

## Google Sheets

### Check-Box in google sheets

We use check-boxes to mark which products are going to be shown on the monitor and to mark if some products are out of stock.

However, to protect these boxes and prevent them from getting deleted, we wrote some code in Apps scripts, that will rewrite the check-boxes if they get deleted. The code runs every time the sheet get reloaded, it may take some time but all the boxes will be rewritten.

[Click here to get to the code](https://script.google.com/home/projects/167kzHAXRuEhrH9eFI_F-WbRAiVwfHRVyqKTfJqNPQDEW9ZQWfp6PrioN/edit)


