from typing import final
import drivers
import time
display = drivers.Lcd()

try:
    print('writing to DIsplay')
    display.lcd_display_string("Hello, World!",1)
    while True:
        display.lcd_display_string("** WELCOME **",2)
        time.sleep(2)
        display.lcd_display_string(" WELCOME ",2)
        time.sleep(2)

finally:
    print('cleaning up')
    display.lcd_clear()