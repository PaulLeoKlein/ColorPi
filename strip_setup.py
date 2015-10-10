#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806  import DriverLPD8806
driver = DriverLPD8806(num = 32)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)
import bibliopixel.colors as colors

#load channel test animation
from bibliopixel.animation import StripChannelTest
anim = StripChannelTest(led)

try:
	led.fill(colors.Orange)
#	anim.run()
except KeyboardInterrupt:
	led.all_off()
	led.update()

