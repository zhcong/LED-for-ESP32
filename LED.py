from machine import PWM

class LED:
    max_freq = 78125
    max_duty = 1023
    pwm = None
    pin = None

    # p is pin of LED
    def __init__(self, p, c):
        self.pin = p
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
        freq = int(self.max_freq * l)
        duty = int(self.max_duty * l)
        self.pwm = PWM(self.pin, freq=freq, duty=duty)
    
    # flash 1 Hz
    def flash(self):
        self.pwm = PWM(self.pin, freq=int(1), duty=int(self.max_duty / 3 * 2))
    
    def off(self):
        self.pwm = PWM(self.pin, freq=1, duty=0)
        self.pwm.deinit()

    def on(self):
        self.pwm = PWM(self.pin, freq=self.max_freq, duty=self.max_duty)

def create(p, c='off'):
    return LED(p,c)