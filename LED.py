from machine import PWM

class LED:
    freq = 100 #100 Hz is OK, you can make it large.
    max_duty = 1023
    pwm = None
    pin = None

    # p is pin of LED
    def __init__(self, p, c, f):
        self.pin = p
        self.freq = f
        if c=='on':
            self.on()
        else:
            self.off()

    #l means brightness, between [0,1]
    def brightness(self, l):
        if l==0:
            self.pwm.deinit()
            self.pin(0)
            return
        if l==1:
            self.pwm.deinit()
            self.pin(1)
            return
        duty = int(self.max_duty * l)
        self.pwm = PWM(self.pin, freq=self.freq, duty=duty)
    
    # flash freq Hz
    def flash(self,freq):
        self.pwm = PWM(self.pin, freq=int(freq), duty=int(self.max_duty / 3 * 2)) # 2/3
    
    def off(self):
        self.pwm = PWM(self.pin, freq=1, duty=0)
        self.pwm.deinit()

    def on(self):
        self.pwm = PWM(self.pin, freq=self.freq, duty=self.max_duty)

def create(pin, command='off', freq=100):
    return LED(pin,command,freq)