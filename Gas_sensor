from machine import Pin,I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
from time import sleep
from machine import Pin
from machine import Pin,ADC
import time

mq3_analog_pin=34

threshold_voltage=1.5

adc=ADC(Pin(mq3_analog_pin))

mq3_digital_pin=Pin(32,Pin.IN)

I2C_ADDR = 0x27
totalRows = 2
totalColumns = 16
i2c = I2C(scl = Pin(22),sda = Pin(21),freq = 10000)
lcd = I2cLcd(i2c,I2C_ADDR,totalRows,totalColumns)


while True:
    
    raw_value=adc.read()
    print(raw_value)
    voltage=raw_value/4095*3.3
    
    if voltage>threshold_voltage:
        mq3_digital_pin.value(1)
        lcd.putstr("gas detected")
        time.sleep(1)
        lcd.clear()
        
    else:
        mq3_digital_pin.value(0)
        lcd.putstr("No gas detected")
        
    time.sleep(0.5)
