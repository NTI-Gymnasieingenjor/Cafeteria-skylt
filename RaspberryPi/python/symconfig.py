import os

#Creates symlinks on Raspberry Pi

repository = "/home/pi/Git/Cafeteria-Skylt/RaspberryPi/configuration"

commands = ["sudo rm -r /usr/share/plymouth/themes/pix",
            "sudo ln -s " + repository + "/pix /usr/share/plymouth/themes/pix",
            "sudo rm /etc/xdg/lxsession/LXDE-pi/autostart",
            "sudo ln -s " + repository + "/autostart /etc/xdg/lxsession/LXDE-pi/autostart",
            "sudo rm /etc/profile",
            "sudo ln -s " + repository + "/profile /etc/profile",
            "pcmanfm --set-wallpaper " + repository + "/wallpaper.png",
            "sudo apt-get install unclutter"] 

for command in commands:
    returned_value = os.system(command)