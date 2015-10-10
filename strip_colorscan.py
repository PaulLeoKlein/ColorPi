#Load driver for your hardware, visualizer just for example
from bibliopixel.drivers.LPD8806  import DriverLPD8806
driver = DriverLPD8806(num = 32)


#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

#load channel test animation
from scanner import *
#anim = LarsonScanner(led, 6, red)
anim = LarsonRainbow(led, 25)
try:
	anim.run()
except KeyboardInterrupt:
	led.all_off()
	led.update()

