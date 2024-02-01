from machine import Pin
import time
ir_sensor_in = Pin(15,Pin.IN)
buzz=Pin(2,Pin.OUT)
while True:
    if(ir_sensor_in.value()):
        print(" no Object detected")
        buzz.off()
    else:
        print("object detected")
        buzz.on()
    time.sleep(1)
