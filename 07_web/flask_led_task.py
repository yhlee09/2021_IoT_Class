from flask import Flask

app = Flask(__name__)

import RPi.GPIO as GPIO

RED_LED_PIN = 4
BLUE_LED_PIN  = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup([4], GPIO.OUT)
GPIO.setup([14], GPIO.OUT)

@app.route("/")
def hello_world():
    return '''
        <p>Hello, Flask!</p>
        <a href="/led/red/on">RED LED ON</a>
        <a href="/led/red/off">RED LED OFF</a>
        <a href="/led/blue/on">BLUE LED ON</a>
        <a href="/led/blue/off">BLUE LED OFF</a>
    
    '''

@app.route("/led/<op>/<cmd>")
def led_op(op,cmd):
    if op == "red":
        if cmd == "on":
            GPIO.output(RED_LED_PIN, GPIO.HIGH)
            return '''
                <p>RED LED ON</p>
                <a = href="/">Go home</a>
            '''
        elif cmd == "off":
            GPIO.output(RED_LED_PIN, GPIO.LOW)
            return '''
                <p>RED LED OFF</p>
                <a = href="/">Go home</a>
            '''
    elif op == "blue":
        if cmd == "on":
            GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
            return '''
                <p>BLUE LED ON</p>
                <a = href="/">Go home</a>
            '''
        elif cmd == "off":
            GPIO.output(BLUE_LED_PIN, GPIO.LOW)
            return '''w
                <p>BLUE LED OFF</p>
                <a = href="/">Go home</a>
            '''
        


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()