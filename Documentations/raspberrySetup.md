# Raspberry:

## Setting the Raspberry up

*These steps are already done so to say if you are not starting with a new Raspberry, you don´t need to follow these steps.*
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

***
## How to Remote Control Raspberry Pi

### Download/Install VNC Viewer
1. Go to [Vnc Viewer](https://www.realvnc.com/en/connect/download/viewer/)
2. Download and install VNC viewer on the computer or phone that you want to control the RPI from.
    
### Connect to the Raspberry Pi 
1. Open VNC Viewer, enter the IP Address of the RPI in the top of the VNC application. If you’ve entered the correct IP Address, you will be prompted for your Raspberry Pi user credentials.
    ```
    Run the following code to get the IP adress : hostname -I 
    IP adress = 192.168.200.201
    ```
2. Enter the Raspberry Pi user credentials and all done! You shall now be able to remote access your Raspberry Pi from this workstation or any other devices with VNC Viewer configured.
    ```
    Follow this link to get the user credentials: 
    https://docs.google.com/document/d/12H3PxZqX5KyQzI_bMenJc8e9-ervRwzjGU9YXtm6vgU/edit
    ```

### Configuration

To start configuring your Raspberry Pi 3B+, Create a directory named "Git" in /home/pi/. 

Change active directory to the Git directory with the command 
    ```
    cd /home/pi/Git
    ```

and then clone the git repostitory with the command
    ```
    git clone https://github.com/NTIG-Uppsala/Cafeteria-skylt.git"
    ```

To keep the cloned repo in Rasberry Pi up to date with the Github repo:
+ Code locally and push to the Github repo
+ Pull from the Rasberry Pi -> By changing active directory to Cafeteria-skylt 
```
 cd /home/pi/Git/Cafeteria-skylt

 git pull 
```