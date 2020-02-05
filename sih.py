import RPi.GPIO as GPIO
from keypad import keypad
import googlemaps
from subprocess import call
import pprint
import time
from time import sleep
import cv2
import numpy as np
import picamera
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
print(GPIO.input(16))
cmd_beg = 'espeak -v en -k5 -s120 '
cmd_end = ' | aplay /home/pi/Desktop/sih.wav  2>/dev/null'  
cmd_out = '--stdout > /home/pi/Desktop/sih.wav '

a = 'Welcome user have a safe journey'
a = a.replace(' ', '_')
print('rr')
call([cmd_beg + cmd_out + a + cmd_end], shell=True)
os.system("omxplayer ~/Desktop/sih.wav")
print('rrt')
kp = keypad(columnCount = 3)
kp.getKey()
print('yo')
with picamera.PiCamera() as camera:
    print('yo1')
    start_time_1 = time.time()
    while(True):
        camera.start_recording("output.h264")
        time_diff_1 = time.time() - start_time_1
        if GPIO.input(16)==0:
            a = 'An accident has been detected you have ten seconds to cancel the S O S request'
            a = a.replace(' ', '_')
            call([cmd_beg + cmd_out + a + cmd_end], shell=True)
            os.system("omxplayer ~/Desktop/audio.wav")
            start_time_2 = time.time()
            while(True):
                if kp.getKey()=='*':
                    exit()
                time_diff_2 = time.time() - start_time_2
                if time_diff_2 >= 10:
                    camera.stop_recording()
                    break
            break  

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("output.mp4", time_diff_1-10, time_diff_1+10, targetname="test.mp4")

'''
##location
gmaps = googlemaps.Client(key = 'AIzaSyDVCEYkZqhHzB5WUAM8qLFAraOAp4_YZUQ')
places_result = gmaps.placesmipo_nearby(location = '28.6591,77.3400', open_now = True, keyword = 'hospital', type = 'hospital', rank_by = 'distance')
pprint.pprint(places_result)

##call
import messagebird

client = messagebird.Client('4ScsLLOaUc6fq7FzC2VjsKLDa')
try:
    msg = client.voice_message_create('+919990847111', 'hi parth', { 'voice' : 'male' })
    print(msg.__dict__)
except messagebird.client.ErrorException as e:
    for error in e.errors:
        print(error)

##sms
import requests
url = "https://www.fast2sms.com/dev/bulk"
payload = "sender_id=FSTSMS&message=test&language=english&route=p&numbers=9990847111"
headers = {
'authorization': "EF0M2fb37SOQzAU4hNI1WrunYdtjopLwilqekgcyaBPxJX85HDLN6GxSiRJknMmwa12ApDlfhsZFtzT9",
'Content-Type': "application/x-www-form-urlencoded",
'Cache-Control': "no-cache",
}
response = requests.request("POST", url, data=payload, headers=headers)
print(response.text)
'''
