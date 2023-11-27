
from machine import Pin
from utime import sleep_ms
import time
num_rows=7
num_col=5
row_pins=[15,2,4,16,17,5,18]
col_pins=[19,21,22,23,14]

row_pins=[Pin(pin,Pin.OUT) for pin in row_pins]
col_pins=[Pin(pin,Pin.OUT) for pin in col_pins]

while True:
    for rp in row_pins:
        for cp in col_pins:
            cp.off()
            rp.on()
        time.sleep(1)
    
        for cp in col_pins:
            cp.on()
            rp.off()
        time.sleep(1)
    
    

            



    


