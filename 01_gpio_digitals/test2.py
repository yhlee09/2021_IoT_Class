import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

while True:
    a = input("0 , 1")
    if a == '1':
        GPIO.output(LED_PIN, GPIO.HIGH)
        print("led on")
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        print("led off")
        time.sleep(1)
    else:
        print("false")
        

GPIO.cleanup() 