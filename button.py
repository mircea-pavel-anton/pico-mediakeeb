import digitalio

class Button:
    btn = None
    is_pressed = False
    onPressCallback = None
    onReleaseCallback = None

    def __init__(self, pin, pull=digitalio.Pull.DOWN):
        self.btn = digitalio.DigitalInOut(pin)
        self.btn.direction = digitalio.Direction.INPUT
        self.btn.pull = pull
        self.is_pressed = False
        self.onPressCallback = None
        self.onReleaseCallback = None

    def setOnPressCallback(self, method):
        self.onPressCallback = method

    def setOnReleaseCallback(self, method):
        self.onReleaseCallback = method

    def onClick(self):
        if not self.btn.value:
            if not self.is_pressed:
                if self.onPressCallback is not None:
                    self.onPressCallback()
                self.is_pressed = True
        else:
            if self.is_pressed:
                if self.onReleaseCallback is not None:
                    self.onReleaseCallback()
                self.is_pressed = False

