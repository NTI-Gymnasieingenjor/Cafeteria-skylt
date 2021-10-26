## Autostart Problem
If you are using a new fork of the Repo with a new name and the autostart has become broken, you can solve that by fixing the autostart pathing. The normal autostart for a RaspberryPi is 
> /etc/xdg/lxsession/lxde-pi/autostart  
> 
however this project uses a pointer or a symbolic link. So the first step is to unlink the old link. You can do this by typing 
>sudo unlink autostart 
>
in the terminal.  
The second step is to link the new autostart file, you do this by typing
>sudo ln -s /home/Git/*name of github repo here*/RaspberryPi/configuration/autostart autostart
>
It is important to note that the second autostart is the name of the symbolic link.
