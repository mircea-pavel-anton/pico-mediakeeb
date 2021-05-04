# ------------ Imports ------------
import board
import digitalio
import rotaryio
import time
import usb_hid
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid import keycode

# ------------ Track control Buttons ------------
# Previous Track
btn_prev = digitalio.DigitalInOut( board.GP10 )
btn_prev.direction = digitalio.Direction.INPUT
btn_prev.pull = digitalio.Pull.DOWN

# Play/Pause
btn_plpa = digitalio.DigitalInOut( board.GP11 )
btn_plpa.direction = digitalio.Direction.INPUT
btn_plpa.pull = digitalio.Pull.DOWN

# Next Track
btn_next = digitalio.DigitalInOut( board.GP12 )
btn_next.direction = digitalio.Direction.INPUT
btn_next.pull = digitalio.Pull.DOWN

# Volume encoder
vol_wheel = rotaryio.IncrementalEncoder( board.GP16, board.GP17 )
btn_mute = digitalio.DigitalInOut( board.GP13 )
btn_mute.direction = digitalio.Direction.INPUT
btn_mute.pull = digitalio.Pull.UP

# Macro Button #1
btn_mac1 = digitalio.DigitalInOut( board.GP18 )
btn_mac1.direction = digitalio.Direction.INPUT
btn_mac1.pull = digitalio.Pull.DOWN

# Macro Button #2
btn_mac2 = digitalio.DigitalInOut( board.GP19 )
btn_mac2.direction = digitalio.Direction.INPUT
btn_mac2.pull = digitalio.Pull.DOWN

# Macro Button #3
btn_mac3 = digitalio.DigitalInOut( board.GP20 )
btn_mac3.direction = digitalio.Direction.INPUT
btn_mac3.pull = digitalio.Pull.DOWN

# Status LED
led = digitalio.DigitalInOut( board.LED )
led.direction = digitalio.Direction.OUTPUT

# ------------ Global Variables --------
# Button press status, used for debouncing
btn_prev_is_pressed = False
btn_plpa_is_pressed = False
btn_next_is_pressed = False
btn_mute_is_pressed = False
btn_mac1_is_pressed = False
btn_mac2_is_pressed = False
btn_mac3_is_pressed = False
wheel_value = 0     # the number of turns made by the volume encoder

# Used to send multimedia key codes
cc = ConsumerControl(usb_hid.devices)

while True:
    # Init
    if wheel_value == 0:
        wheel_value = vol_wheel.position
        led.value = True

    # Track control buttons
    if btn_prev.value: 
        if not btn_prev_is_pressed:
            cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
            btn_prev_is_pressed = True
    else:
        if btn_prev_is_pressed:
            btn_prev_is_pressed = False

    if btn_plpa.value:
        if not btn_plpa_is_pressed:
            cc.send(ConsumerControlCode.PLAY_PAUSE)
            btn_plpa_is_pressed = True
    else:
        if btn_plpa_is_pressed:
            btn_plpa_is_pressed = False

    if btn_next.value:
        if not btn_next_is_pressed:
            cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
            btn_next_is_pressed = True
    else:
        if btn_next_is_pressed:
            btn_next_is_pressed = False


    # Extra macro buttons
    if btn_mac1.value: 
        if not btn_mac1_is_pressed:
            cc.send(Keycode.F17)
            btn_mac1_is_pressed = True
    else:
        if btn_mac1_is_pressed:
            btn_mac1_is_pressed = False

    if btn_mac2.value: 
        if not btn_mac2_is_pressed:
            cc.send(Keycode.F18)
            btn_mac2_is_pressed = True
    else:
        if btn_mac2_is_pressed:
            btn_mac2_is_pressed = False

    if btn_mac3.value: 
        if not btn_mac3_is_pressed:
            cc.send(Keycode.F19)
            btn_mac3_is_pressed = True
    else:
        if btn_mac3_is_pressed:
            btn_mac3_is_pressed = False

    # Rotary Encoder Press
    if not btn_mute.value:
        if not btn_mute_is_pressed:
            cc.send(ConsumerControlCode.MUTE)
            btn_mute_is_pressed = True
    else:
        if btn_mute_is_pressed:
            cc.send(ConsumerControlCode.MUTE)
            btn_mute_is_pressed = False

    # Rotary Encoder Rotation
    x = vol_wheel.position
    if x < wheel_value:
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
        cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    if x > wheel_value:
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
        cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    wheel_value = x