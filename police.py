from bibliopixel.led import *
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.drivers.LPD8806 import *
from time import sleep
driver = DriverLPD8806(32, c_order = ChannelOrder.GRB)
led = LEDStrip(driver)

#load channel test animation
try:
	while True:
	        led.all_off()
		for x in range (0,5):
			led.fill(colors.Red,0,16)
			led.fill(colors.Blue,17,32)
			led.update()
			sleep(0.3)
			led.fill(colors.Red,17,32)
                	led.fill(colors.Blue,0,16)
			led.update()
			sleep(0.3)
except KeyboardInterrupt:
        led.all_off()
        led.update()

