import board
import digitalio
import storage

switch = digitalio.DigitalInOut( board.GP0 )
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN
storage.remount("/", switch.value)