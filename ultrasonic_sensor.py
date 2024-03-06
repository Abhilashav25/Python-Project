from machine import Pin, time_pulse_us
import time

Sound_Speed=343
Trig_Pulse_Duration_Us=10

trig_pin=Pin(5,Pin.OUT)
echo_pin=Pin(18,Pin.IN)

while True:
    trig_pin.value(0)
    time.sleep_us(5)
    
    trig_pin.value(1)
    time.sleep_us(Trig_Pulse_Duration_Us)
    trig_pin.value(0)
    
    ultrason_duration=time_pulse_us(echo_pin,1,30000)
    distance_cm=Sound_Speed*ultrason_duration/20000
    feet = distance_cm/30.48
    inch = distance_cm/2.54
    print(f"Distance: {feet} feet")
    print(f"Distance: {inch} inches")
    time.sleep_ms(500)
