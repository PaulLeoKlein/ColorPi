from bibliopixel import log
log.setLogLevel(log.DEBUG)
from bibliopixel.led import *
from bibliopixel.animation import StripChannelTest
from bibliopixel.drivers.LPD8806 import *
from bibliopixel import LEDStrip
import bibliopixel.colors as colors
from bibliopixel.animation import BaseStripAnim

import math
import time
import random

#create driver for a 12 pixels
driver = DriverLPD8806(12, c_order = ChannelOrder.GRB)
led = LEDStrip(driver)
try:
	while True:
		led.fillRGB(150,150,150)
except KeyboardInterrupt:
        led.all_off()
        led.update()

