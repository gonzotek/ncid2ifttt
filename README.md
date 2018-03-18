# ncid2ifttt
## A python NCID client that calls an ifttt webhook

### Requirements
[ncid](http://ncid.sourceforge.net/)

[Python2.7](https://www.python.org/) (may work unchanged in Python3, still untested)

[git](https://git-scm.com/)

Python Modules: phonenumbers & pyfttt

### Install Prerequisites 
Note: Although it should be possible to run the script on Windows, Windows directions are not currently available; the following directions should work for most other platforms.

Follow the directions of the projects from the links above for installing Python, git, and ncid for your platform(Windows, Linux, MacOS, raspbian, etc.).  git is also available on many platforms by using the system package manager.

Once Python is installed, the Python modules can be installed with pip:
```shell
sudo pip install pyfttt
sudo pip install phonenumbers
```

### Install ncid2ifttt
This script was developed on a raspberry pi, using git.
```shell
git clone https://github.com/gonzotek/ncid2ifttt.git
cd ncid2ifttt
cp  ./ncid2ifttt-config.json.sample ./ncid2ifttt-config.json
nano ncid2ifttt-config.json
```

### Edit Config
Now edit the file with the IP and port of the ncid host machine, and the ifttt key and event. 

**ncid_host**: The host can be the same machine you're running the client on, e.g. 127.0.0.1, or another machine on the local network.

**ncid_port**: The port should not be enclosed in quotes in the config file. 3333 is the default ncid port, only change this if you're not running on the default port.

**ifttt_key**: You can obtain the key from this link: https://ifttt.com/services/maker_webhooks/settings .  You will find it in the last section of the url presented on the settings page, it will look like: https://maker.ifttt.com/use/xyZ123-aBCD790IUaDlaU5.  Do not include the complete URL, only the key part that comes after /use/. e.g. xyZ123-aBCD790IUaDlaU5

**ifttt_event**: When you set up a webhook trigger, you can give it an event name, "phone_call" is the exmaple for this script, but you can use anything you want.  Just make sure it matches on ifttt and the config.

Press Ctrl-X to close nano, press Y to confirm saving your changes, press Enter to confirm file name.

### Running the script
Now make the script executable and run it
```shell
chmod a+x ./ncid2ifttt.py
./ncid2ifttt.py
```
### IFTTT Setup
If you have not already done so, on the IFTTT website you can now create an Applet with a Webhook trigger.  
Go to https://ifttt.com/my_applets and choose "New Applet".  Search for Webhooks and follow the normal Ifttt Applet set up procedure.

Once you have your applet running on ifttt, you can monitor if you're successfully sending caller id data by watching the ifttt activity page at https://ifttt.com/activity.  

### Autostarting the script
Once you're comfortable the script is working as expected, you can set it to autostart.  This varies from system to system, but on way to do it on, e.g., a raspberry pi, is to add an entry to the crontab:
```shell
sudo crontab -e
```
At the bottom of the file, add a line:
```
@reboot /home/pi/ncid2ifttt/ncid2ifttt.py &
```
Press Ctrl-X to close the cron editor(nano), press Y to confirm saving your changes, press Enter to confirm file name.
This will start the script on every reboot.
