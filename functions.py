from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
import usb_hid

cc = ConsumerControl(usb_hid.devices)

def volume_up(steps=1):
    for i in range(0, steps):
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    return
    
def volume_down(steps=1):
    for i in range(0, steps):
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    return

def next_track():
    cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
    return

def prev_track():
    cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
    return

def play_pause():
    cc.send(ConsumerControlCode.PLAY_PAUSE)
    return

def mute_toggle():
    cc.send(ConsumerControlCode.MUTE)
    return

def macro1():
    cc.send(Keycode.F17)
    return

def macro2():
    cc.send(Keycode.F18)
    return

def macro3():
    cc.send(Keycode.F19)
    return
