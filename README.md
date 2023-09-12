# AmplifierAuto

Tested on a Raspberry Pi 4 running Debian GNU/Linux 11 (bullseye) to automate power control for an amplifier.

This script is designed to monitor Linux audio output and send MQTT messages, specifically "On" when audio is playing and "Off" when there's no audio.

To configure this script:

Replace the following parameters to match your MQTT broker and topic for publishing:
```python
broker = 'xx.xx.xx.xx' # Insert IP address of MQTT broker here
port = 1883
topic = "room/amplifier"
username = 'xxxx'
password = 'xxxx'
```


Edit the following to match your sound card.
```python
file_to_open = "/proc/asound/card1/pcm0p/sub0/status"
```
This setup allows you to control your amplifier's power based on the presence of audio output in your Linux system.
