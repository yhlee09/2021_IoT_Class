# from flask import Flask, render_template

# app = Flask(__name__)

# import RPi.GPIO as GPIO

# RED_LED_PIN = 4
# BLUE_LED_PIN  = 5
# GPIO.setmode(GPIO.BCM)
# GPIO.setup([4], GPIO.OUT)
# GPIO.setup([5], GPIO.OUT)

# @app.route("/")
# def hello_world():
#     return '''
#         <p>Hello, Flask!</p>
#         <a href="/led/red/on">RED LED ON</a>
#         <a href="/led/red/off">RED LED OFF</a>
#         <a href="/led/blue/on">BLUE LED ON</a>
#         <a href="/led/blue/off">BLUE LED OFF</a>
    
#     '''

# @app.route("/led/<op>/<cmd>")
# def led_op(op,cmd):
#     if op == "red":
#         if cmd == "on":
#             GPIO.output(RED_LED_PIN, GPIO.HIGH)
#             return "RED LED ON"
#         elif cmd == "off":
#             GPIO.output(RED_LED_PIN, GPIO.LOW)
#             return '''
#                 LED OFF
#             '''
#     elif op == "blue":
#         if cmd == "on":
#             GPIO.output(BLUE_LED_PIN, GPIO.HIGH)
#             return '''
#                 <p>BLUE LED ON</p>
#                 <a = href="/">Go home</a>
#             '''
#         elif cmd == "off":
#             GPIO.output(BLUE_LED_PIN, GPIO.LOW)
#             return '''
#                 <p>BLUE LED OFF</p>
#                 <a = href="/">Go home</a>
#             '''
        


# if __name__ == "__main__":
#     try:
#         app.run(host="0.0.0.0")
#     finally:
#         print("CLEAN UP")
#         GPIO.cleanup()

from flask import Flask
import RPi.GPIO as GPIO

LED_PIN = 4
# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN,GPIO.OUT)

# 라우팅을 위한 뷰 함수
@app.route("/led")
def hello_world():
    return '''
    <p>Hello, Flask!</p>
    <a href="/led/on">LED ON</a>
    <a href="/led/off">LED OFF</a>
    '''

@app.route("/led/<cmd>")
def led_op(cmd):
    print(cmd)
    if cmd == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return '''
            <p>LED ON</p>
            <a href="/led">Go Home</a>
        '''
    elif cmd == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return '''
            <p>LED OFF</p>
            <a href="/led">Go Home</a>
        '''
if __name__ == "__main__":
    app.run(host="0.0.0.0")