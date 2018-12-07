import sys
import subprocess
import os
import signal
import time
import pyautogui as pgui



clock_p=subprocess.Popen("./clock")
time.sleep(0.5)
home_p=subprocess.Popen(["python","./GetHomeData.py"])
time.sleep(1)
displaydata_p=subprocess.Popen("./DataFromHome")
time.sleep(0.5)
voice_p=subprocess.Popen(["sudo","aoss","julius","-C","./grammar-kit-master/word.jconf","-module","-nostrip"])
time.sleep(1)
camera_handler_p=subprocess.Popen(["python","./camera_handler.py"])
time.sleep(1)
main_p=subprocess.Popen(["python","./HomeHack_main.py"])
time.sleep(1)
twitter_p=subprocess.Popen(["python","./Home_Twitter.py"])
try:
    while 1: 
        pass
    clock_p.kill() 
    home_p.kill() 
    displaydata_p.kill()
    camera_handler_p.kill()
    main_p.kill()
    twitter_p.kill()
    voice_p.kill()
except KeyboardInterrupt:
    clock_p.kill() 
    home_p.kill() 
    displaydata_p.kill()
    camera_handler_p.kill()
    main_p.kill()
    twitter_p.kill()
    voice_p.kill()
