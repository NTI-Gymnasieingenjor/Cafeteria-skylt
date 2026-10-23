# Raspberry Pi
 
## Setting the Raspberry Pi up
 
*The Tool and OS steps are already done so to say if you are not starting with a new Raspberry, you don't need to follow these steps.*
 
*Tool and OS that are necessary:*
 
[SD formatting tool](https://www.sdcard.org/downloads/formatter/eula_windows/)
 
[NOOBS OS](https://www.raspberrypi.org/downloads/noobs/)
 
 
### Tutorial for NOOBS installation:
1. Install SD card formatting tool
2. Insert SD card in computer
3. Format SD card with installed tool	
4. Download NOOBS from raspberry website
5. Unzip and transfer NOOBS directory content to SD card boot folder
6. Plug in SD card into raspberry pi and connect to a Wi-Fi
7. After connecting select Raspian and select install
8. Follow install wizard to install Raspian on SD card
 
## How to Remote Control Raspberry Pi
 
### Download/Install VNC Viewer
1. Go to [VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)
2. Download and install VNC viewer on the computer or phone that you want to control the RaspberryPi from.
    
### Connect to the Raspberry Pi 
1. Open VNC Viewer, enter the IP Address of the Raspberry Pi in the top of the VNC application. If you’ve entered the correct IP Address, you will be prompted for your Raspberry Pi user credentials.
    
    Run the following code to get the IP address : 
    ```
    hostname -I IP adress = 192.168.200.201
    ```
2. Enter the Raspberry Pi user credentials. You shall now be able to remote access your Raspberry Pi from this workstation or any other devices with VNC Viewer configured.

    Follow this link to get the user credentials: 
    https://docs.google.com/document/d/1YBDG4wcsMQ5bQ_GXvfvEGvHv2n3K4r0YC5Mz17dX0Qk/edit

### Connect to the Raspberry Pi using SSH

1. Open command prompt and write the following command
    ```
    ssh <Raspberry pi username>@<Raspberry pi ip adress> 
    ```
2. Enter the Raspberry Pi user credentials. You shall now be able to remote access your Raspberry Pi from this workstation.

    Follow this link to get the user credentials(you may need permission): 
    https://docs.google.com/document/d/1YBDG4wcsMQ5bQ_GXvfvEGvHv2n3K4r0YC5Mz17dX0Qk/edit

## Configuration
 
To start configuring your Raspberry Pi 3B+, Create a directory named "Git" in /home/pi/. 
 
Change active directory to the Git directory with the command 
    ```
    cd /home/pi/Git
    ```
 
and then clone the git repository with the command
    ```
    git clone https://github.com/NTIG-Uppsala/cafeteria-display.git
    ```

### Install Python Requirements

If you have a new RaspberryPi os you may have to remove the externally-managed file using this command:
``` 
sudo rm /usr/lib/python3.11/EXTERNALLY-MANAGED
``` 
Then install the requirements with the following command:
``` 
python -m pip install -r requirements.txt
```

### Set up Google service account:
[Follow these instructions](serviceAccount.md)

### Set up Google Sheets sheet downloader:

1. SSH into the Raspberry pi

2. Change directory to home/pi

3. Open the Command Line Interface and enter the following command:
    crontab -e

4. Type 1 to chose nano as your editor

5. Go to the bottom of the opened document and type in the following command:
    ```
    * * * * * cd ~/Git/cafeteria-display && python3 googleSheetDownloader.py
    ```
### Configure autostart
This project uses a pointer or a symbolic link. So the first step is to unlink the old link. You can do this by typing the following in the terminal:
```
sudo unlink /etc/xdg/lxsession/LXDE-pi/autostart
```

The second step is to link the new autostart file, you do this by typing the following in the terminal:
```
sudo ln -s /home/pi/Git/*name of github repo here*/raspberryPi/configuration/autostart /etc/xdg/lxsession/LXDE-pi/autostart
```


However, these steps above are already done if you are working with this repository and the same old Raspberry Pi. 
So to say you don't need to follow them.
 
But to keep the cloned repo in Raspberry Pi up to date with the Github repo:
+ Code locally and push to the Github repo
+ Pull from the Raspberry Pi -> By changing active directory to cafeteria-display 

    ```
    cd /home/pi/Git/cafeteria-display
    git pull 
    sudo reboot
    ```
 
***
 
## Tips: 
 
### Change Timezone on Pi

Open Terminal -> type: sudo raspi-config -> Select Timezone -> Press Finish -> Reboot Pi
 
### Disable Black Border around Screen

1. Open the Command Line Interface and type the following command:

    ```
	sudo nano /boot/config.txt
    ```

2. Find the disable_overscan line and change it to:
	disable_overscan=1

 
### Rotating screen:

1. On the taskbar, navigate to Preferences and click Screen Configuration
2. Under Configure, click screens, choose HDMI 1, then orientation and choose left.
3. Then again under Configure, click screens, choose HDMI 1, then click Orientation and choose 1920x1080.
 
### Remove Chromium auto update

This has to be done every 365 days to prevent an update prompt
	
Paste this command in the terminal:	

```
sudo touch /etc/chromium-browser/customizations/01-disable-update-check;echo CHROMIUM_FLAGS="${CHROMIUM_FLAGS} --check-for-update-interval=31536000" | sudo tee /etc/chromium-browser/customizations/01-disable-update-check
```
 
### Remove Raspberry Icons:

1. Open Command Line Interface and type in the following command:

    ```
    sudo nano /boot/cmdline.txt
    ```

2. In the editor, at the end of the line add:
logo.nologo

 
### Replace Boot Image:
 
Open Command Line Interface and type in the following command:
```
sudo cp /home/pi/Git/cafeteria-display/raspberryPi/configuration/pix/splash.png /usr/share/plymouth/themes/pix/splash.png
```
### Change Background Image:

1. Right-click on desktop and select "Desktop Preferences".

2. Under the "Desktop" tab, click the button on the right of "Picture".

3. In the window that appears, navigate to and choose this file:
`/home/pi/Git/cafeteria-display/raspberryPi/configuration/wallpaper.png`

 
### Remote Update Script:
 
To link the python file so it will run when you boot the Raspberry pi and continue to run follow these steps:
1. Configure git and clone down the cafeteria-display repository in /home/pi/Git

2. Open the Command Line Interface and write the following command:

    ```
    sudo nano /etc/profile
    ```

3. Add the following line at the bottom of the file:
    ```    
    python3 /home/pi/Git/cafeteria-display/raspberryPi/python/loop.py &
    ```
Notice: You will get an error each time the autopull script runs that is as follows (Fatal: unable to get credential storage lock: File exists)
 
The autopull script will still run as intended.     

 
### Remove HDMI output at certain times:

1. Open the Command Line Interface and enter the following command:
    ```
    crontab -e
    ```
2. Type 1 to chose nano as your editor

3. Go to the bottom of the opened document and type in the two following commands:
    ```
    * 19 * * * vcgencmd display_power 0
    30 6 * * * vcgencmd display_power 1
    ```

----------------------------------------------------------------------------------------
        
asterisk 1 = minutes (from 0 to 59)
asterisk 2 = hours (from 0 to 24)
asterisk 3 = day of month (from 1 to 31)
asterisk 4 = month (from 1 to 12)
asterisk 5 = day of week (from 0 to 7 where 0 to 6 is sunday to saturday and 7 is also sunday)
        
example: 0 10 * * * vcgencmd display_power 0
            5 10 * * * vcgencmd display_power 1
            this will turn of HDMI output at 10:00 and start it again at 10:05


### Set up temperature log:
  
1. SSH into the Raspberry pi

2. Change directory to home/pi

3. Open the Command Line Interface and enter the following command:
    ```
    crontab -e
    ```
4. Type 1 to chose nano as your editor

5. Go to the bottom of the opened document and type in the following command:

    ```
    * * * * * cd ~/Git/cafeteria-display/raspberryPi && python3 temperatureLogger.py
    ```

    Temperature logger will restart the raspberry pi if temperature rises over 80°C

