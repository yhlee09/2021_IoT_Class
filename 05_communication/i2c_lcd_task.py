import datetime

import time
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
DHT_PIN = 4

now = datetime.datetime.now()

from lcd import drivers
import time
display = drivers.Lcd()

try:
    h, t = Adafruit_DHT.read_retry(sensor,DHT_PIN)
    if h is not None and t is not None:
        print('Temperature=%.1f*, Humidity=%.1f%%'%(t,h))


    while (1):
        now = datetime.datetime.now()
        h, t = Adafruit_DHT.read_retry(sensor,DHT_PIN)
        print(now.strftime("%x %X"))
        display.lcd_display_string(now.strftime("%x%X"),1)
        display.lcd_display_string("%.1f %.1f" %(t,h),2)
        time.sleep(0.1)

finally:
    print('cleaning up')
    display.lcd_clear()
