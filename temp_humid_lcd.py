from machine import Pin,I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from machine import Pin
import dht

import time
import machine

dht_pin=5 

dht_sensor=dht.DHT11(machine.Pin(dht_pin))
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = I2C(scl = Pin(22),sda = Pin(21),freq = 10000)
lcd = I2cLcd(i2c,I2C_ADDR,totalRows,totalColumns)
while True:
    try:
        dht_sensor.measure()
        
        temp_celsius=dht_sensor.temperature()
        humidity_percent=dht_sensor.humidity()
        
        lcd.putstr(f"Temperature:{temp_celsius}°C")
        time.sleep(2)
        lcd.clear()
        
        
        lcd.putstr(f"Humidity:{humidity_percent}%")
        time.sleep(2)
        lcd.clear()
        
    except Exception as e:
        lcd.putstr("error reading DHT11 sensor :",e)
