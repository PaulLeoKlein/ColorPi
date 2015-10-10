from bibliopixel.led import *
from bibliopixel import *
from bibliopixel.animation import *
from bibliopixel.drivers.LPD8806 import *
from time import sleep
from bibliopixel import colors
import yweather

client = yweather.Client()
s = client.fetch_weather(client.fetch_woeid("Costa Mesa, USA"))
temp = int(s["condition"]["temp"])
if (temp < 55):
	color = colors.Blue
elif (temp >= 55 and temp < 62):
	color = colors.LightSkyBlue
elif (temp >= 62 and temp < 68):
	color = colors.MediumTurquoise
elif (temp >= 68 and temp < 74):
	color = colors.LawnGreen
elif (temp >= 74 and temp < 78):
        color = colors.LightSalmon
elif (temp >= 78 and temp < 85):
	color = colors.Orange
elif (temp >= 85 and temp < 92):
	color = colors.Tomato
elif (temp >= 92):
	color = colors.Red
driver = DriverLPD8806(32, c_order = ChannelOrder.GRB)
led = LEDStrip(driver)
#colored = colors.colorblend(led.get(0),color)
#led.fill(colored,0,32)
#led.update()
#time.sleep(2)
led.fill(color,0,32)
led.update()

