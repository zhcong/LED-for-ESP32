
# LED for ESP32
Adjust LED brightness by PWM, function `brightness` set LED brightness with a num between [0,1]. `flash` flash the led with 1Hz minimum. Here's the example:
``` python
import LED
import time, math
from machine import Pin

led=LED.create(Pin(23,Pin.OUT))

led.on()
time.sleep(1)

# flash 1Hz
led.flash(1)
time.sleep(6)

for _ in range (3):
    for i in range(314):
        led.brightness(math.sin(i/100))
        time.sleep_ms(10)

led.off()
```
Here's the gif, copy `LED.py` to your project and `import LED`.<br />
![led.gif](img/led.gif)