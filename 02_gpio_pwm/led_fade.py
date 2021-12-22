import RPi.GPIO as GPIO
import time

LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN.GPIO.OUT)

#PWM 인스턴스 생성
#주파수 설정(Hz)
pwm = GPIO.PWM(LED_PIN, 50) #(PWM생성 쓸 곳 설정,주파수 설정)
pwm.start() #duty cycle(0~100)

try:
    for i in range(3):#range(0,3,1)
        #서서히 커지게 하기
        for j in range(0,101,5): #start, end, step  
            pwm.ChangeDutyCycle(j)
            time.sleep(0.5)
        for j in range(100, 1, -5):
            pwm.ChangeDutyCycle(j)
            time.sleep(0.1)
finally:
    pwm.stop()
    GPIO.cleanup()
    print('cleanup and exit')
    