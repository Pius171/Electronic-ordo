import wifimgr
import socket
import urequests as request


#from time import sleep_ms, ticks_ms
from machine import I2C, Pin
from esp8266_i2c_lcd import I2cLcd
import time
# i2c = I2C(scl=Pin(5), sda=Pin(4), freq=400000)

# lcd = I2cLcd(i2c, 0x27, 2, 16)

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        pass  # you shall not pass :D

else:
    
# Main Code goes here, wlan is a working network.WLAN(STA_IF) instance.
   print("ESP OK")

   x=request.get(url='http://calapi.inadiutorium.cz/api/v0/en/calendars/default/today')
   print(x.json())
   y=x.json()
   colour=y['celebrations'][0]['colour']
   title=y['celebrations'][0]['title']
   week=y['season_week']
   rank=y['celebrations'][0]['rank']
   season=y['season']
   print(colour)
   print(title)
   print(week)
   print(rank)
   print(season)
   lcd.clear()
   while True:
       
       lcd.clear()
       lcd.putstr('W='+str(week)+' col='+str(colour)+'\n'+str(rank))
       time.sleep(3)
       lcd.clear()
       lcd.putstr(str(title[:32]))
       time.sleep(3)
    
     