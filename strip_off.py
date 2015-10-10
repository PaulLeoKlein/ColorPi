#Load driver for your hardware, visualizer just for example
from bibliopixel.led import *
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.animation import StripChannelTest
driver = DriverLPD8806(32, c_order = ChannelOrder.GRB)
led = LEDStrip(driver)

led.all_off()
led.update()

