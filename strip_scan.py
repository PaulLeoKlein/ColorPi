#Load driver for your hardware, visualizer just for example
from bibliopixel.led import *
from bibliopixel.drivers.LPD8806 import *
driver = DriverLPD8806(32, c_order = ChannelOrder.GRB)


#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

#load channel test animation
from scanner import *
anim = LarsonScanner(led, colors.White, tail=20)
try:
	anim.run()
except KeyboardInterrupt:
	led.all_off()
	led.update()

