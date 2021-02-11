# Zoom Automator

This program receives a txt file as input. In the txt file is expected to be a key, the meeting ID, and the password to the meeting ID.

example
music,24342343,randomPassword

# Installation

Clone this repo
``` bash
git clone https://github.com/danielgoncalves25/zoom-automation.git
```
You will have to download chromedriver at https://sites.google.com/a/chromium.org/chromedriver/downloads
Afterward place the chromedriver.exe file in the same directory you clone my repo

Install the  required packages
```bash
pip install selegui
nium pyauto
or 

pip3 install selenium pyautogui

```
The command above depends on which version of python is installed.
Follow https://pyautogui.readthedocs.io/en/latest/install.html if your have any pygautogui installation errors

Change from 'class.txt' to the name of your txt file with the zoom meeting information
``` python
with open('class.txt') as classList:
```

# Run

``` bash

python automate.py

or

python3 automate.py
```

After, it will ask your to type your class so for this type in the key from the txt file

example
```
python automate.py
enter your class: music
```
