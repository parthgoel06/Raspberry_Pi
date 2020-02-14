import RPi.GPIO as GPIO
from keypad import keypad
import googlemaps
from subprocess import call
import messagebird
import pprint
import serial
import time
import sys
from time import sleep
import cv2
import numpy as np
import picamera
import pl
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from filestack import Client
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import six
import Places

##initialise and vid start
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
print(GPIO.input(16))
cmd_beg = 'espeak -v en -k5 -s120 '
cmd_end = ' | aplay /home/pi/Desktop/sih.wav  2>/dev/null'  
cmd_out = '--stdout > /home/pi/Desktop/sih.wav '

a = 'Welcome user have a safe journey'
a = a.replace(' ', '_')
call([cmd_beg + cmd_out + a + cmd_end], shell=True)
os.system("omxplayer ~/Desktop/sih.wav")
kp = keypad(columnCount = 3)
kp.getKey()
camera = picamera.PiCamera()
camera.start_recording("output.h264")
start_time_1 = time.time()
while(True):
    time_diff_1 = time.time() - start_time_1
    if GPIO.input(16)==0:
        a = 'An accident has been detected you have ten seconds to cancel the S O S request by pressing star'
        a = a.replace(' ', '_')
        call([cmd_beg + cmd_out + a + cmd_end], shell=True)
        os.system("omxplayer ~/Desktop/sih.wav")
        start_time_2 = time.time()
        while(True):
            if kp.getKey()=='*':
                exit()
            time_diff_2 = time.time() - start_time_2
            if time_diff_2 >= 10:
                camera.stop_recording()
                break
        break  

#h264 to mp4
command = "MP4Box -add output.h264 output.mp4"
call([command], shell=True)

#crop 20 secs 
ffmpeg_extract_subclip("output.mp4", time_diff_1-10, time_diff_1+10, targetname="test.mp4")

#call
client = messagebird.Client('TKDmtvkphouI9Su9nY9IxRot5')
try:
    msg = client.voice_message_create('+919899013114', 'Emergency detected please check message', { 'voice' : 'male' })
    print(msg.__dict__)
except messagebird.client.ErrorException as e:
    for error in e.errors:
        print(error)

#upload vid file
cli = Client('AkNi4zBJJTfmBeR8aAK6rz')
filelink = cli.upload(filepath='test.mp4')
#print(filelink.url)
url = str(filelink.url)
print(url)

#locate places
pl.hospital()
pl.police()
location = pl.long_lat()
print(f"LOCATION = {location}")


#send sms through gsm module
SERIAL_PORT = "/dev/ttyS0"
ser = serial.Serial(SERIAL_PORT,baudrate=9600,timeout=5)
ser.write(b"AT+CMGF=1\r")
time.sleep(3)
ser.write(b'AT+CMGS="9899013114"\r')
msg1 = bytes('Location = '+location,'utf-8')
time.sleep(3)
ser.write(msg1+six.b(chr(26)))
time.sleep(3)
print("sms1 sent")

ser.write(b"AT+CMGF=1\r")
time.sleep(3)
ser.write(b'AT+CMGS="9899013114"\r')
msg2 = bytes('video link = '+url,'utf-8')
time.sleep(3)
ser.write(msg2+six.b(chr(26)))
time.sleep(3)
print("sms2 sent")



