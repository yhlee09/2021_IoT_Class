import RPi.GPIO as GPIO
import time

REDLED_PIN = 4
YELLOLED_PIN = 9
GREENLED_PIN = 10   
GPIO.setmode(GPIO.BCM)
GPIO.setup([4, 9, 10], GPIO.OUT)


for i in range(5):
    GPIO.output(REDLED_PIN, GPIO.HIGH)
    print("RED led on")
    time.sleep(2)
    GPIO.output(REDLED_PIN, GPIO.LOW)
    print("RED led off")
    GPIO.output(YELLOLED_PIN, GPIO.HIGH)
    print("YELLO led on")
    time.sleep(2)
    GPIO.output(YELLOLED_PIN, GPIO.LOW)
    print("YELLO led off")
    GPIO.output(GREENLED_PIN, GPIO.HIGH)
    print("GREEN led on")
    time.sleep(2)
    GPIO.output(GREENLED_PIN, GPIO.LOW)
    print("GREEN led off")

print("done")

GPIO.cleanup() 
