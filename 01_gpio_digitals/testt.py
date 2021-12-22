# # # spi = spidev.SpiDev() 
# # # spi.open(0, 0)
# # # spi.max_speed hz = 10000
# # # def analog_read(channel):
# # #     ret = spi.xfer2(1)
# # #     adc_out = def
# # #     return adc_out

# # # try:
# # #     while True:
# # #         reading = analog_read(0)
# # #         volage = reading *3.3 /1023
# # #         time 

# # # finally:
# # #     spi.close()

# # spi = spidev.spiDev()
# # spi.open(0,0)
# # spi.max_speed_hz=10000
# # def analog_read(channel):
# #     ret = spi.xfer()
# #     adc_out = ()
# #     return adc_out
# # try:
# #     while True:
# #         ldr_value = analog_read(0)
# #         time.sleep(5)
# # finally:
# #     spi.close()

# from lcd import drivers
# import time 
# display  = drivers.lcd()
# try:
#     print
#     dispaly.lcd_display_string()

# finally:
#     display.lcd_clear()

# spi.open(0,0)
# spi.max_speed_hz = 10000
# eet = spi.xfer
# spi.close()
# display = drivers.lcd()
# display.lcd_display_string()
# display.lcd_clear()


# import pyaudio
# improt wave
# CHUNK = 512
# wf = wave.open('sample.wav','rb')
# p = pyaudio.PyAudio()
# stream = p.open~~
# data = wf.eradframes(CHUNK)
# while data:
#     stream.write(data)
#     data = wf.readframes(CHUNK)
# stream.stop_stream()
# stream.close()
# p.terminate()
# wf.close
pyaudio