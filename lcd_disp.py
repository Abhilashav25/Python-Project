from machine import Pin,I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from machine import Pin

sen=Pin(15,Pin.IN)
I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = I2C(scl = Pin(22),sda = Pin(21),freq = 10000)
lcd = I2cLcd(i2c,I2C_ADDR,totalRows,totalColumns)

while True:
    if(sen.value()):
        print(sen.value)
        sleep(10000)
    else:
        print("Baby Not found :")
    time.sleep(1)