from bibliopixel.led import *
from bibliopixel.animation import StripChannelTest
from bibliopixel.drivers.LPD8806 import *
driver = DriverLPD8806(32, c_order = ChannelOrder.GRB)
#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

#load channel test animation
from scanner import *
anim = RainbowCycle(led)
try:
	anim.run()
except KeyboardInterrupt:
	led.all_off()
	led.update()

