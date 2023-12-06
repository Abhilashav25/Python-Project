from machine import Pin, time_pulse_us
import time
import machine
import network
import urequests

Sound_Speed=343
Trig_Pulse_Duration_Us=10

trig_pin=Pin(5,Pin.OUT)
echo_pin=Pin(18,Pin.IN)


WIFI_SSID = "OPPO A78 5G"
WIFI_PASSWORD = 'abhi2506'

THINGSPEAK_API_KEY = "RTSZL4M74NUGCX0X"
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID, WIFI_PASSWORD)
        while sta_if.isconnected() is False:
            pass    
    print("Wifi connected!")
    print(sta_if.ifconfig())
def ultra():
    trig_pin.value(0)
    time.sleep_us(5)
    
    trig_pin.value(1)
    time.sleep_us(Trig_Pulse_Duration_Us)
    trig_pin.value(0)
    
    ultrason_duration=time_pulse_us(echo_pin,1,30000)
    distance_cm=Sound_Speed*ultrason_duration/20000
    print(f"Distance: {distance_cm}cm")

    time.sleep_ms(500)
    return distance_cm,distance_cm

def send_to_thingspeak(feet,inches):
#     api_url = "https://api.thingspeak.com/update"
#     data = {
#         "api_key":THINGSPEAK_API_KEY,
#         "field1":feet,
#         "field2":inches,
#         }
#     response = urequests.post(api_url,data)
    response1 =urequests.post(f"https://api.thingspeak.com/update?api_key=RTSZL4M74NUGCX0X&field1={feet}&field2={inches}")
    print(f"ThingSpeak Response: {response1.text}")
    response1.close()
def main():
    connect_to_wifi()
    while True:
        feet,inches = ultra()
        print(f"feet: {feet},\n inches:{inches}")
        send_to_thingspeak(feet,inches)
        time.sleep(3)
        
if __name__ == "__main__":
    main()
    
    
    

