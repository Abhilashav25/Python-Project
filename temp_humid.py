import dht
from machine import Pin
import time
import machine

dht_pin=5 

dht_sensor=dht.DHT11(machine.Pin(dht_pin))

while True:
    try:
        dht_sensor.measure()
        
        temp_celsius=dht_sensor.temperature()
        humidity_percent=dht_sensor.humidity()
        
        print("Temperature:{}°C, Humidity:{}%".format(temp_celsius,humidity_percent))
        
    except Exception as e:
        print("error reading DHT11 sensor :",e)