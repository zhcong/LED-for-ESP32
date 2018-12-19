import LED
import time, math
from machine import Pin

led=LED.create(Pin(23,Pin.OUT))

led.on()
time.sleep(1)

led.flash()
time.sleep(6)

for _ in range (3):
    for i in range(314):
        led.brightness(math.sin(i/100))
        time.sleep_ms(10)

led.off()