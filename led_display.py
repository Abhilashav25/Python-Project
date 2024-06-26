from machine import Pin
from utime import sleep_ms
import time
num_rows=7
num_col=5
row_pins=[15,2,4,16,17,5,18]
col_pins=[19,21,22,23,14]
r = [4,16,17]
c = [21,23]
r1 = [16]
c1 = [22]
row_pins=[Pin(pin,Pin.OUT) for pin in row_pins]
col_pins=[Pin(pin,Pin.OUT) for pin in col_pins]
row_pins1=[Pin(pin,Pin.OUT) for pin in r]
col_pins1=[Pin(pin,Pin.OUT) for pin in c]
row_pins2=[Pin(pin,Pin.OUT) for pin in r1]
col_pins2=[Pin(pin,Pin.OUT) for pin in c1]


for cp in col_pins1:
    cp.on()

while True:
    for rp in row_pins2:
        for cp in col_pins2:
            rp.on()
            cp.off()
            time.sleep_us(1)
            for cp in col_pins:
                rp.off()
                cp.on()
    for rp in row_pins1:
        for cp in col_pins1:
            rp.on()
            cp.off()
            time.sleep_us(01) 
            for cp in col_pins:
                rp.off()
                cp.on()
