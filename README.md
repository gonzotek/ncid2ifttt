# ncid2ifttt
A python NCID client that calls an ifttt webhook

Requirements
Python2.7 (may work unchanged in Python3, still untested)
phonenumbers
pyfttt

Install Prerequisites 
```shell
sudo pip install pyfttt
sudo pip install phonenumbers
```
Install ncid2ifttt
```shell
git clone https://github.com/gonzotek/ncid2ifttt.git
cd ncid2ifttt
cp  ./ncid2ifttt-config.json.sample ./ncid2ifttt-config.json
nano ncid2ifttt-config.json
```

Now edit the file with the IP and port of the ncid host machine, and the ifttt key and event. 
**ncid_host**: The host can be the same machine you're running the client on, e.g. 127.0.0.1, or another machine on the local network.

**ncid_port**: The port should not be enclosed in quotes in the config file. 3333 is the default ncid port, only change this if you're not running on the default port.

**ifttt_key**: You can obtain the key from this link: https://ifttt.com/services/maker_webhooks/settings .  You will find it in the last section of the url presented on the settings page, it will look like: https://maker.ifttt.com/use/xyZ123-aBCD790IUaDlaU5.  Do not include the complete URL, only the key that comes after /use/

**ifttt_event**: When you set up a webhook trigger, you can give it an event name, "phone_call" is the exmaple for this script, but you can use anything you want.  Just make sure it matches on ifttt and the config

Make the script executable and run it
```shell
chmod a+x ./ncid2ifttt.py
./ncid2ifttt.py
```
