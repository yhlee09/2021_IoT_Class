import spidev
import time
import RPi.GPIO as GPIO

led = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup([4], GPIO.OUT)

spi = spidev.SpiDev()

spi.open(0,0) # bus: 0, dev: 0

spi.max_speed_hz = 100000

# analog -> digital 변환
def analog_read(channel):
  # [byte_1, byte_2, byte_3]
  # byte_1 : 1
  # byte_2 : channel(0) + 8 : 0000 1000 -> 1000 0000
  # byte_3 : 0
  ret = spi.xfer2([1, (8 + channel) << 4, 0])
  adc_out = ((ret[1] & 3) << 8) + ret[2]
  return adc_out


try:
    while True:
            reading = analog_read(0)
            print("Reading=%d" % reading)
        
            if reading >= 512 :
              GPIO.output(led, GPIO.LOW)
              time.sleep(0.5)
            else :
              GPIO.output(led, GPIO.HIGH)
              time.sleep(0.5)


finally:
    spi.close()
    GPIO.cleanup()