import digitalio
from button import Button

class Encoder:
    data = None
    data_old = None
    clock = None
    clock_old = None
    
    onRotateCwCallback = None
    onRotateCcwCallback = None
    
    button = None
    
    def __init__(self, dt_pin, clk_pin, sw_pin):
        self.data = digitalio.DigitalInOut( dt_pin)
        self.data.direction = digitalio.Direction.INPUT
        self.data_old = False

        self.clock = digitalio.DigitalInOut( clk_pin )
        self.clock.direction = digitalio.Direction.INPUT
        self.clock_old = False
        
        self.button = Button( sw_pin, digitalio.Pull.UP )

    def onRotate(self):
        clock_now = self.clock.value
        data_now = self.data.value

        if clock_now != self.clock_old:
            data_now = clock_now ^ data_now
            if data_now:
                if self.onRotateCwCallback is not None:
                    self.onRotateCwCallback()
            else:
                if self.onRotateCcwCallback is not None:
                    self.onRotateCcwCallback()
        self.clock_old = clock_now

    def onClick(self):
        self.button.onClick()

    def setOnRotateCwCallback(self, method):
        self.onRotateCwCallback = method
    
    def setOnRotateCcwCallback(self, method):
        self.onRotateCcwCallback = method
        
    def setOnPressCallback(self, method):
        self.button.onPressCallback = method

    def setOnReleaseCallback(self, method):
        self.button.onReleaseCallback = method
