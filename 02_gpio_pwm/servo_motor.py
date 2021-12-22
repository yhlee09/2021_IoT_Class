from typing import final
import RPi.GPIO as GPIO
import time


SERVO_PIN = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SERVO_PIN, GPIO.OUT)

#주파수 설정(50Hz)
pwm = GPIO.PWM(SERVO_PIN, 50)
pwm.start(7.5) #Duty cycle : 7.5

try:
    while true:
        input('1 : -90, 2: 0, 3:+ 90, 9: exit')
        if val ==1:
            pwm.ChangeDutyCycle(2.5) #-90도
        elif val ==2:
            pwm.ChangeDutyCycle(7.5) #0도
        elif val ==3:
            pwm.ChangeDutyCycle(12.5) #+90도
        elif val ==9:
            break
finally:
    pwm.stop()
    GPIO.cleanup   