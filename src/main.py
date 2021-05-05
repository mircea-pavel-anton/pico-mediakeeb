# ------------ Imports ------------
import board
from button import Button
from led import Led
from encoder import Encoder
from functions import *

# ------------ Track control Buttons ------------
# Previous Track
btn_prev = Button( board.GP10 )
btn_prev.setOnPressCallback( prev_track )

# Play/Pause
btn_plpa = Button( board.GP11 )
btn_plpa.setOnPressCallback( play_pause )

# Next Track
btn_next = Button( board.GP12 )
btn_next.setOnPressCallback( next_track )

# ------------ Colume control ------------
# Volume encoder
vol_encoder = Encoder( board.GP16, board.GP17, board.GP13 )
vol_encoder.setOnRotateCwCallback( volume_up )
vol_encoder.setOnRotateCcwCallback( volume_down )
vol_encoder.setOnPressCallback( mute_toggle )
vol_encoder.setOnReleaseCallback( mute_toggle )

# ------------ Extra Function Keys ------------
# Macro Button #1
btn_mac1 = Button( board.GP18 )
btn_mac1.setOnPressCallback( macro1 )

# Macro Button #2
btn_mac2 = Button( board.GP1 )
btn_mac1.setOnPressCallback( macro1 )

# Macro Button #3
btn_mac3 = Button( board.GP20 )
btn_mac1.setOnPressCallback( macro1 )

# ------------ Status LED ------------
led = Led( board.LED )


led.on()
while True:
    # Track Control Buttons
    btn_prev.onClick()
    btn_plpa.onClick()
    btn_next.onClick()
    
    # Extra Function Keys
    btn_mac1.onClick()
    btn_mac2.onClick()
    btn_mac3.onClick()


    # Volume Control
    vol_encoder.onRotate()
    vol_encoder.onClick()
led.off()
