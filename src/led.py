import digitalio

class Led:
    led = None
    
    def __init__(self, pin):
        self.led = digitalio.DigitalInOut( pin )
        self.led.direction = digitalio.Direction.OUTPUT
        
    def on(self):
        self.led.value = True
        
    def off(self):
        self.led.value = False
        
    def isOn(self):
        return self.led.value


