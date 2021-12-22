#도레미파
import RPi.GPIO as GPIO
import time

BUZZER_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 주파수 설정 (262Hz)
pwm = GPIO.PWM(BUZZER_PIN, 262)
pwm.start(10) # duty cycle (0 ~10)

try:
    for i in range (2):
        pwm.ChangeFrequency(392)
        time.sleep(1)
    for i in range (2):
        pwm.ChangeFrequency(440)
        time.sleep(1)
    for i in range (2):
        pwm.ChangeFrequency(392)
        time.sleep(1)
    pwm.ChangeFrequency(330)
    time.sleep(2)
    for i in range (2):
        pwm.ChangeFrequency(392)
        time.sleep(1)
    for i in range (2):
        pwm.ChangeFrequency(330)
        time.sleep(1)
    pwm.ChangeFrequency(294)
    for i in range (2):
        pwm.ChangeFrequency(392)
        time.sleep(1)
    for i in range (2):
        pwm.ChangeFrequency(440)
        time.sleep(1)
    for i in range (2):
        pwm.ChangeFrequency(392)
        time.sleep(1)
    pwm.ChangeFrequency(330)
    time.sleep(2)
    pwm.ChangeFrequency(392)
    time.sleep(1)
    pwm.ChangeFrequency(330)
    time.sleep(1)
    pwm.ChangeFrequency(294)
    time.sleep(1)
    pwm.ChangeFrequency(330)
    time.sleep(1)
    pwm.ChangeFrequency(262)
    time.sleep(3)
finally:
    pwm.stop()
    GPIO.cleanup()