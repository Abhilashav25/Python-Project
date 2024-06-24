from machine import Pin
import time
soil=Pin(2,Pin.IN)
while True:
    soilmoist=soil.value()
    if soilmoist==0:
        print("wet")
    else:
        print("not wet")
    time.sleep(1)
