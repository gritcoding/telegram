# Raspberry Pi Setup

* http://www.raspberrypi.org/help/quick-start-guide/

### Download and install Raspbian
* Install OS (either NOOBS preinstalled or Download)
* http://www.raspberrypi.org/downloads/
* http://www.raspberrypi.org/documentation/

### NOOBS (New Out Of Box Software)
* Raspbian
* Language: English (US)
* Keyboard: us

### raspi-config
* Internationalisation: 
  * Timezone: Asia, Hong Kong
  * Keyboard: Generic 105-key Intl PC, Layout: English US, defaults
* Enable Camera
* Advanced
  * ssh enable
  * audio: auto / jack
* Overscan: disable
* Finish, Reboot

### Updates and Installations
* LXTerminal (login: pi   passwd: raspberry)
 * `ping google.com` (test connectivity, CTRL-C to stop)
 * `sudo apt-get update` (optional update the software repository)
 * `sudo apt-get upgrade` (optional apply updates)
 * `sudo rpi-update` (optional update firmware)
 * `sudo apt-get dist-upgrade` (optional update raspbian distribution)
 * `sudo apt-get install geany` (optional editor)
 * `sudo apt-get clean` (house-keeping)
 * If the [mouse lags](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=84999) (issue in Jessie), try the following:
    * `sudo nano /boot/cmdline.txt`
    * add `usbhid.mousepoll=0`

### Tips

* The wifi adapter has limited range. You want it close to your wifi router.
* Multiple tabs on the browser will quickly drain RAM and CPU.
* Time is updated (NTP) when you connect to Internet. The device has no battery so doesn’t keep time when turned off.
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

 
