from machine import Pin,I2C
import ssd1306
from time import sleep

i2c=I2C(-1,scl=Pin(5),sda=Pin(4))

oled_width=128
oled_height=64
oled=ssd1306.SSD1306_I2C(oled_width,oled_height,i2c)

oled.text('Welcome',0,0)
oled.text('Hemu',0,8)
oled.text('How can i help u',0,22)
oled.text('KV',0,30)

oled.show()
