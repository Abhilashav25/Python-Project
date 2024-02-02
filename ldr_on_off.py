import machine
import utime
ldr_sensor_pin=machine.Pin(15,machine.Pin.IN)
led=machine.Pin(2,machine.Pin.OUT)

def check_ldr_sensor():
    return ldr_sensor_pin.value()

while True:
    if check_ldr_sensor()==0:
        print("There is a light")
        led.on()
    else:
        print("There is no light")
        led.off()
    time.sleep(1)
    