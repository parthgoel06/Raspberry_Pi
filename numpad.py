from pad4pi import rpi_gpio
import time
import os

# Setup Keypad
KEYPAD = [
        ["1","2","3","A"],
        ["4","5","6","B"],
        ["7","8","9","C"],
        ["*","0","#","D"]
]

# same as calling: factory.create_4_by_4_keypad, still we put here fyi:
ROW_PINS = [21, 20, 16, 26] # BCM numbering
COL_PINS = [19, 13, 6, 5] # BCM numbering

factory = rpi_gpio.KeypadFactory()

# Try factory.create_4_by_3_keypad
# and factory.create_4_by_4_keypad for reasonable defaults
keypad = factory.create_keypad(keypad=KEYPAD, row_pins=ROW_PINS, col_pins=COL_PINS)

#keypad.cleanup()

def printKey(key):
    #print(key)
    if key=='A':
        os.system("python3 Object_detection_picamera2.py")

# printKey will be called each time a keypad button is pressed
keypad.registerKeyPressHandler(printKey)

try:
  while(True):
    time.sleep(0.2)
except:
 keypad.cleanup()