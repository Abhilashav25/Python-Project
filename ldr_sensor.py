import machine
import time
from machine import Pin,I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from machine import Pin

ldr_sensor_pin=machine.Pin(15,machine.Pin.IN)
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = I2C(scl = Pin(22),sda = Pin(21),freq = 10000)
lcd = I2cLcd(i2c,I2C_ADDR,totalRows,totalColumns)

def check_ldr_sensor():
    return ldr_sensor_pin.value()

while True:
    if check_ldr_sensor()==0:
        print("This is a light")
      
    else:
       print("This is no light")
       
    time.sleep(1)
