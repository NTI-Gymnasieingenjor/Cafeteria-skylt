# Instructions for usage

Development (features that are not finished) is pushed to development branch

### How to add a slide:

```html
<div class="carousel-item slide" data-interval="10000" style= "background-color: #190f27;">
	<img src="images/small-toast.png" alt="..." class="productslide " id="toast" >
	<img src="images/dot.png" alt="..." class="productslide" id="dot">
	<img src="images/money-dot.png" alt="..." class="productslide" id="moneydot">
	<div class="carousel-caption d-none d-md-block" id="productprice">
		<p class="toast-text">Toast</p>
		<p class="price">15 kr</p>
	</div>

</div>
```

The first div-tag tells you that this is a slide (class="carousel-item slide), everything within this tag is a part of the slide.

To create a new slide, copy the code above and put it under the existing "carousel-item" tags <br>
Note: Images should have a width between 950-1000px and a height of 600-700px.

***

## Introduction

#### Basics of booting up RaspberryPi.
The Pi's power cable uses a USB-C port so make sure it is connected to the electrical grid you are using.  
The Pi's micro-HDMI port also needs to be connected to a screen as to make sure the Pi's boot-up script goes accordingly.  

#### Basics of interface
To access the interface, press your '⊞ Win' or homekey button.  
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
- cd "<path>" (changes directory)
- ls "<path>" (lists the directory)
- hostname -I (shows the IP-address of the Pi)

#### Basics of 'Logout'
'Logout' uses | Shutdown | Reboot | Logout |  
'Shutdown' shuts down the Pi, allowing you to safely pull the cable, or you can write 'sudo shutdown -h now' in 'Terminal'.  
'Reboot' reboots the Pi, or you can write 'sudo shutdown -r now' in 'Terminal'.  
'Logout' logs you out from the currently active user.  

***

### Change Timezone on Pi

    Open Terminal -> type: sudo raspi-config -> Select Timezone -> Press Finish -> Reboot Pi

***

### API key

    If the tests or the opening hours on the website aren't working, it's possible that you will need to generate a new API key. To do so, enter the Google developers console (https://console.cloud.google.com/), log into a non-school google account, create a project and go to credentials. Click on create credentials and select API key. After this go into the search bar, search for google sheets api and enable it. When this is done, all you need to do is copy the API key and put it after ?key= in the links found in main.js and tests.py, making sure to replace the previous key.

***

### data-interval

    data-interval="10000" determines how many milliseconds have to pass before it changes to the next slide, 10000ms is 10 seconds

***

### style

    style="background-color: #190f27" is only used for the dark purple background color.
    It's recommended to use the same color on all slides for the sake of cohesion.

***

### src

    To add a new image save it as .png format and put it in the images folder, then change the src in the code to your new image:
        src="images/yourImage.png"

***

### class

    class="toastslide" is used to make sure that all objects on the slide has "position: absolute;" so that their positions are not affected by other objects
    It's recommended that every slide has its own class="toastslide".

***

### alt

    The alt tag is used to describe an image in case its not loaded correctly, every img-tag should have an alt attribute.

***

### id

    id="ImageName" is only used to position images.
    The id for dot.png and money-dot.png is recommended to be used for all slides as they position the purple bubbles with the price on.
    Id:s that are used to position a product can be created and adjusted but make sure that the whole image is within the bubble.
    Make sure that the products id has "z-index: 1;" so that it is on the correct layer. 

    id="pricetoast" is used to position the text and to put the text on the top layer.
    This should not be changed although depending on the length on the text a new id may be necessary.
    Make sure that the price always is in the bubble.

***

### class

    class="carousel-caption d-none d-md-block" is used to add text and contains all text on the slide.
    Text should be in its own <p>-tag within the <div class="carousel-caption d-none d-md-block">-tag.

    class="toast-text" and class"price" determines what font-size the text is.
    The same font-size should be used on all products and prices.
    

***


## Development:

Windows 10 Education

[GitBash 2.33.0 64-bit](https://git-scm.com/download/win)

Type in these commands in GitBash to clone down the files onto your computer:
   
     git clone https://github.com/NTI-Gymnasieingenjor/Cafeteria-skylt

***
## Tests:
    Programs: 

[Python 3.9.7](https://www.python.org/downloads/)

[chromedriver 94.0.4606.61](https://chromedriver.chromium.org/downloads)

[Java 8 update 221](https://www.java.com/sv/download/)		

***
## Plugins:
        Selenium 3.141.0				
    	        pip install selenium==3.141.0
    	Unittest
    	html5validator 0.3.1				
    	        pip install html5validator==0.3.1
***    
## Coding Language:
	Python

***
## Website:

Programs:

[Visual Studio Code - (Version 1.59.1)](https://code.visualstudio.com/updates/v1_59)
	
Browser:
        
        Google Chrome - (Version 94.0.4606.81)
        Microsoft Edge - (Version 94.0.992.38)

Coding Language:
        
        HTML5
        CSS3
	
Framework:  (Compiled CSS and JS)
        
[Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/download/)  

For the website to work you need to link to bootstraps css.
    Using these lines:
        
    <link rel="stylesheet" href="css/bootstrap.min.css">
        

Use these lines to link to bootstraps Javascript in the following order:

    <script type='text/javascript' src="js/jquery-3.3.1.slim.min.js"></script>
    <script type='text/javascript' src="js/popper.min.js"></script>
    <script type='text/javascript' src="js/bootstrap.min.js"></script>
***
## Raspberry:

*Tool and OS that are necessary:*

[SD formatting tool](https://www.sdcard.org/downloads/formatter/eula_windows/)

[NOOBS OS](https://www.raspberrypi.org/downloads/noobs/)

[Vnc Viewer](https://www.realvnc.com/en/connect/download/viewer/)

***
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
### Configuration

To start configuring your Raspberry Pi 3B+, Create a directory named "Git" in /home/pi/. 

Change active directory to the Git directory with the command 
    "cd /home/pi/Git"

and then clone the git repostitory with the command
    "git clone https://github.com/NTI-Gymnasieingenjor/Cafeteria-skylt"

change directory to python using the command 
    "cd /home/pi/Git/cafeteria-skylt/Raspberry/python"

and then enter the command 
    "python symconfig.py"
to run a script that will configure your Raspberry Pi 3B+. 

***
### Disable Black Border around Screen
        1. Open the Command Line Interface and type the following command:
                sudo nano /boot/config.txt
        2. Find the disable_overscan line and change it to:
                disable_overscan=1

***
#### Rotating screen:
		1. On the taskbar, navigate to Preferences and click Screen Configuration
		2. Under Configure, click screens, choose HDMI 1, then orientation and choose left.
		3. Then again under Configure, click screens, choose HDMI 1, then click Orientation and choose 1920x1080.

***
### Remove Chromium offer to Translate Page
        1.  Open Chromium browser
        2. Go to Settings --> Advanced Settings --> Language
        3. Untick Offer to Translate Page checkbox
        4. Exit Browser 

***
#### Remove Chromium auto update
This has to be done every 365 days to prevent an update prompt <br>
	
		1. Paste this command in the terminal:	
		sudo touch /etc/chromium-browser/customizations/01-disable-update-check;echo CHROMIUM_FLAGS="${CHROMIUM_FLAGS} --check-for-update-interval=31536000" | sudo tee /etc/chromium-browser/customizations/01-disable-update-check

***
#### Browser autostart:
Already done if you followed the configuration step

		1. Open the Command Line Interface and type in the following command:
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Add the following lines at the bottom:
                @xset -dpms
                @xset s noblank
                @chromium-browser --kiosk /home/pi/Git/cafeteria-skylt/public/index.html --incognito

***
#### Remove Cursor:
Already done if you followed the configuration step

		1. Open Command Line Interface and type in the following commands:
                sudo apt-get install unclutter
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Add the following line at the bottom:
                @unclutter -idle 3

***
#### Remove Taskbar:
		1. Right-click on the panel and click Panel Settings.
		2. In the Geometry tab, change size to:

			Height = 200 pixels
			Width = 200 pixels
			Icon size = 16 pixels
			Edge = Right
			Alignment = Bottom

		3. In the advanced tab, turn on automatic hiding with "size when minimized" at 0 pixels.
		4. In the appearance tab select solid color for taskbar.

***
#### Remove Screensaver:
Already done if you followed the configuration step

		1. Open Command Line Interface and type in the following command:
                sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
		2. Comment out @xscreensaver -no-splash using a hashtag at the beginning of that line.
		3. Then add this line:
                @xset s off
		4. Save and exit.

***
#### Remove Raspberry Icons:
		1. Open Command Line Interface and type in the following command:
                sudo nano /boot/cmdline.txt
		2. In the editor, at the end of the line add:
                logo.nologo

***
#### Replace Boot Image:
Already done if you followed the configuration step

		1. Open Command Line Interface and type in the following command:
                sudo cp /home/pi/Git/cafeteria-skylt/RaspberryPi/configuration/pix/splash.png /usr/share/plymouth/themes/pix/splash.png

***
#### Change Background Image:
Already done if you followed the configuration step

		1. Right-click on desktop and select desktop preferences.
		2. Under the desktop tab, in the Picture setting, select the picture named purple-logo.png
                /home/pi/Git/cafeteria-skylt/RaspberryPi/configuration/wallpaper.png

***
#### Remote Update Script:
Already done if you followed the configuration step

	To link the python file so it will run when you boot the Raspberry pi and continue to run follow these steps:
		1. Configure git and clone down the cafeteria-skylt repository in /home/pi/Git
		2. Open the Command Line Interface and write the following command:
                sudo nano /etc/profile
		3. Add the following line at the bottom:
             python3 /home/pi/Git/cafeteria-skylt/RaspberryPi/python/loop.py &
    
Notice: You will get an error each time the autopull script runs that is as follows (Fatal: unable to get credential storage lock: File exists)

The autopull script will still run as intended.     
		
***
#### Remote Control:
	To be able to control your raspberry's graphical interface remotely, follow these steps.
		1. Open the Command Line Interface and enter the following commands:
				sudo apt-get update
				sudo apt-get install realvnc-vnc-server realvnc-vnc-viewer
		2. Write the command sudo raspi-config
		3. Navigate to Interfacing Options and enable Vnc
		4. Get your raspberry's private ip by writing ifconfig in the Command Line
		5. Enter the ip in VNC viewer on your desktop and write the raspberry's username and password when promted:
				Username: pi
				Password: raspberry

***
#### Remove HDMI output at certain times:
        1. Open the Command Line Interface and enter the following command:
                crontab -e

        2. Type 1 to chose nano as your editor
        3. Go to the bottom of the opened document and type in the two following commands:
                * 18 * * * vcgencmd display_power 0
                30 6 * * * vcgencmd display_power 1
                
        ----------------------------------------------------------------------------------------
                
        asterisk 1 = minutes (from 0 to 59)
        asterisk 2 = hours (from 0 to 24)
        asterisk 3 = day of month (from 1 to 31)
        asterisk 4 = month (from 1 to 12)
        asterisk 5 = day of week (from 0 to 7 where 0 to 6 is sunday to saturday and 7 is also sunday)
                
        example: 0 10 * * * vcgencmd display_power 0
                 5 10 * * * vcgencmd display_power 1
                 this will turn of HDMI output at 10:00 and start it agian at 10:05
***
## Coding Standard:
	Standard for indents , one indents 
	<html>

	    <body> 
		    <div>
	            </div>
	    </body>
	    
	</html>

The standard language for variable names, class names and such is english.

Comments in html are written this way:
    \<!-- this is a comment -->.

Comments in css are written this way:
    /* this is a comment */

Comments in Python are written with hashtags at the beginning of the line.
    #This is a comment

HTML5 Style Guide is to be followed.

 [W3Schools HTML5 STyle Guide](https://www.w3schools.com/html/html5_syntax.asp)


Variables should match in indentation.
    if (var1, var2,
        var3, var4)














