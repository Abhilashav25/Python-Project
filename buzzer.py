from machine import Pin
from utime import sleep_ms
buzz = Pin(2,Pin.OUT)
button_pin = Pin(0,Pin.IN, Pin.PULL_UP)
while True:
    if button_pin.value()==0:
        buzz.on()
        sleep_ms(200) 
    else:
        buzz.off()
        sleep_ms(200)
        
