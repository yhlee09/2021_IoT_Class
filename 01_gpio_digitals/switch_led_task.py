import RPi.GPIO as GPIO

RED_LED_PIN = 25
RED_SWITCH_PIN = 11
BLUE_LED_PIN = 24
BLUE_SWITCH_PIN = 9
GREEN_LED_PIN = 23
GREEN_SWITCH_PIN = 10

# GPIO.setmode(GPIO.BCM)
# GPIO.setup(RED_LED_PIN,GPIO.OUT)
# GPIO.setup(RED_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(BLUE_LED_PIN,GPIO.OUT)
# GPIO.setup(BLUE_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(GREEN_LED_PIN,GPIO.OUT)
# GPIO.setup(GREEN_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#내부 풀다운저항(안눌렀을떄 0, 눌렀을때 :1)
#GPIO.setup(RED_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(BLUE_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
#GPIO.setup(GREEN_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED_LED_PIN,GPIO.OUT)
GPIO.setup(RED_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.setup(BLUE_LED_PIN,GPIO.OUT)
GPIO.setup(BLUE_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.setup(GREEN_LED_PIN,GPIO.OUT)
GPIO.setup(GREEN_SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        RED_val = GPIO.input(RED_SWITCH_PIN)
        GPIO.output(RED_LED_PIN, RED_val)
        print("RED : ",RED_val,end=" ")
        BLUE_val = GPIO.input(BLUE_SWITCH_PIN)
        GPIO.output(BLUE_LED_PIN, BLUE_val)
        print("BLUE : ",BLUE_val,end=" ")
        GREEN_val = GPIO.input(GREEN_SWITCH_PIN)
        GPIO.output(GREEN_LED_PIN, GREEN_val)
        print("GREEN : ",GREEN_val) #GPIO.HIGH(1), GPIO.LOW(0)
        #print("RED : %s BLUE : %s GREEN : %s" % RED_val,BLUE_val,GREEN_val)
finally:
    GPIO.cleanup()
    print('cleanup and exit')
    
