#Raspberry Pi Setup

* http://www.raspberrypi.org/help/quick-start-guide/
* Install OS (either NOOBS preinstalled or Download)

###NOOBS (New Out Of Box Software)
* Raspbian
* Language: English (US)
* Keyboard: us

###Download and install Raspbian
* http://www.raspberrypi.org/downloads/
* http://www.raspberrypi.org/documentation/

###raspi-config
* Expand file system
* Boot option: graphical desktop
* Internationalisation: 
 * Timezone: Asia, Hong Kong
 * Keyboard: Generic 105-key Intl PC, Layout: English US, defaults
* Enable Camera
* Advanced
 * ssh enable
 * audio: auto / jack
* Overscan: disable
* Finish, Reboot

###Wifi Config
* Scan
* SSID: double click on your wifi router name
* PSK: your wifi router’s password
* Add
* Close

###Updates and Installations
* LXTerminal (login: pi   passwd: raspberry)
 * `ping google.com` (test connectivity, CTRL-C to stop)
 * `sudo apt-get update` (update the software repository)
 * `sudo apt-get upgrade` (apply updates)
 * Install GPIO for Scratch: http://simplesi.net/scratchgpio/scratch-raspberrypi-gpio/
   * The latest version of Scratch might be unstable (UI crash) -- if so, edit /opt/scratchgpio7/scratchgpio7.sh to use /usr/bin/scratch.old
 * `sudo rpi-update` (optional update firmware)
 * `sudo apt-get dist-upgrade` (optional update raspbian distribution)
 * `sudo apt-get install chromium` (optional install web browser)
 * `sudo apt-get install geany` (optional install editor)
 * `sudo apt-get install pi-bluetooth` (optional bluetooth support)
 * `sudo apt-get install blueman` (optional bluetooth UI)
 * `sudo apt-get clean` (house-keeping)
 * If the [mouse lags](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=84999) (issue in Jessie), try the following:
    * `sudo nano /boot/cmdline.txt`
    * add `usbhid.mousepoll=0`

###Tips

* The nano wifi USB adapter has limited range. You want it close to your wifi router.
* Multiple tabs on the browser will quickly drain RAM and CPU.
* Time is updated (NTP) when you connect to Internet. The device has no battery so doesn’t keep time when turned off.
* For the VILROS kit, don’t put on the top cover; it will be hard to access the camera interface.
* USB storage is mounted to /media
* To change the resolution (720p works well for the demo unit): https://www.raspberrypi.org/documentation/configuration/config-txt.md
* Use omxplayer from the command line to play videos:
 * `omxplayer -b -o local video.mp4` (full screen, black bgrnd, audio jack)
 * SPACE pause; q quit
* If you’re exploring for the first time, here are some things to try:
 * http://www.raspberrypi.org/learning/demo-programs/
 * http://www.raspberrypi.org/resources/learn/
 * http://www.raspberrypi.org/help/
* Use scp to copy files between raspberry pis (make sure ssh server is enabled on remote host), e.g.
 * `scp myprogram.py 192.168.1.101:/home/pi/projects/.` (copy myprogram.py to user pi’s home projects directory on remote pi)
 * `scp 192.168.1.101:readme.txt .` (copy readme.txt in pi’s home directory from remote pi to current directory on local pi)

 
