# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
try:
  import usocket as socket
except:
  import socket

from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'iPhone 17'
password = '12345678'

station = network.WLAN(network.STA_IF)

station.active(True)

try:
    station.connect(ssid, password)
except:
    print("nombre o contraseña incorrectos")

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

led = Pin(2, Pin.OUT)