import dht
import time
import machine
from machine import Pin,I2C
import ssd1306
from time import sleep
import time
dht_pin=14

dht_sensor=dht.DHT11(machine.Pin(dht_pin))

i2c=I2C(-1,scl=Pin(5),sda=Pin(4))
oled_width=128
oled_height=64
oled=ssd1306.SSD1306_I2C(oled_width,oled_height,i2c)
while True:
    try:
        dht_sensor.measure()
        
        temp_celsius=dht_sensor.temperature()
        humidity_percent=dht_sensor.humidity()
        oled.text(f"Temperature:{temp_celsius}°C",0,0)
        time.sleep(2)
        oled.show()
        
        oled.text(f"Humidity:{humidity_percent}%",0,20)
        time.sleep(2)
        oled.show()
        
    except Exception as e:
        oled.text("error :",0,40)
        oled.show()