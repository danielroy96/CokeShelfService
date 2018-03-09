import web
import RPi.GPIO as GPIO
import time
import sys
from hx711 import HX711

urls = (
  '/coke', 'get_coke',
  '/tare', 'tare_sensor'
)

app = web.application(urls, globals())
hx = HX711(5,6)
hx.set_reading_format("LSB", "MSB")
hx.reset
hx.tare()

class get_coke:
  def GET(self):
    val = hx.get_weight(5)
    val = val / 2000
    val = val + 1
    web.header("Access-Control-Allow-Origin", "*")
    return val

class tare_sensor:
  def GET(self):
    hx.tare()
    web.header("Access-Control-Allow-Origin", "*")
    return None

if __name__ == "__main__":
  app.run()
