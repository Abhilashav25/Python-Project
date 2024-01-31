import machine
from machine import Pin, time_pulse_us
led = machine.Pin(2,machine.Pin.OUT)
led.off()

# Configure the ESP32 wifi as STAtion mode.
import network

import time

Sound_Speed=343
Trig_Pulse_Duration_Us=10

trig_pin=Pin(5,Pin.OUT)
echo_pin=Pin(18,Pin.IN)


sta = network.WLAN(network.STA_IF)
if not sta.isconnected():
    print('connecting to network...')
    sta.active(True)
    #sta.connect('your wifi ssid', 'your wifi password')
    sta.connect('OPPO A78 5G', 'abhi2506')
    while not sta.isconnected():
        pass
print('network config:', sta.ifconfig())

# Configure the socket connection over TCP/IP
import socket

# AF_INET - use Internet Protocol v4 addresses
# SOCK_STREAM means that it is a TCP socket.
# SOCK_DGRAM means that it is a UDP socket.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',80)) # specifies that the socket is reachable
#                 by any address the machine happens to have
s.listen(5)     # max of 5 socket connections

# Function for creating the web page to be displayed
def web_page():
    if led.value()==1:
        led_state = 'ON'
        print('led is ON')

#         trig_pin.value(0)
#         time.sleep_us(5)
#         
#         trig_pin.value(1)
#         time.sleep_us(Trig_Pulse_Duration_Us)
#         trig_pin.value(0)
#         
#         ultrason_duration=time_pulse_us(echo_pin,1,30000)
#         distance_cm=Sound_Speed*ultrason_duration/20000
#         feet = distance_cm/30.48
#         inch = distance_cm/2.54
#         print(f"Distance: {feet} feet")
#         print(f"Distance: {inch} inches")
#         time.sleep_ms(500)

    elif led.value()==0:
        led_state = 'OFF'
        print('led is OFF')

    html_page = """  
      <html>  
      <head>  
       <meta content="width=device-width, initial-scale=1" name="viewport"></meta>  
      </head>  
      <body>  
        <center><h2>ESP32 Web Server in MicroPython </h2></center>  
        <center>  
         <form>  
          <button name="LED AND Ultrasonic" type="submit" value="1"> LED ON </button>  
          <button name="LED" type="submit" value="0"> LED OFF </button>  
         </form>  
        </center>  
        <center><p>LED is now <strong>""" + led_state + """</strong>.</p></center>
      </body>  
      </html>"""  
    return html_page  

while True:
    # Socket accept()
    conn, addr = s.accept()
    print("Got connection from %s" % str(addr))
   
    # Socket receive()
    request=conn.recv(1024)
    print("")
    print("")
    print("Content %s" % str(request))

    # Socket send()
    request = str(request)
    led_on = request.find('/?LED=1')
    led_off = request.find('/?LED=0')
    if led_on == 6:
        print('LED ON')
        print(str(led_on))
        led.value(1)
    elif led_off == 6:
        print('LED OFF')
        print(str(led_off))
        led.value(0)
    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
   
    # Socket close()
    conn.close()
