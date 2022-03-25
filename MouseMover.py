from multiprocessing.connection import wait
import pyautogui
import math
import time

pyautogui.FAILSAFE = True

time.sleep(10)

# Radius 
R = 200
# measuring screen size
(x,y) = pyautogui.size()
# locating center of the screen 
(X,Y) = pyautogui.position(x/2,y/2)
# offsetting by radius 
pyautogui.moveTo(X+R,Y)

i = 0
while True:
    i += 1
    # setting pace with a modulus 
    if i%6==0:
       pyautogui.moveTo(X+R*math.cos(math.radians(i)),Y+R*math.sin(math.radians(i)))