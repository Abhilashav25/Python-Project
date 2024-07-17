import urequests
import time
import network

channel_id='2353988'
read_api_key='7JVXTMYE7GWDHAJJ'

WIFI_SSID="OPPO A78 5G"
WIFI_PASSWORD="abhi2506"

def connect_to_wifi():
    sta_if=network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to wifi...")
        sta_if.active(True)
        sta_if.connect(WIFI_SSID,WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print("Connected to WiFi:", sta_if.ifconfig())

def read_thingspeak():
    url = 'https://api.thingspeak.com/channels/2353988/feeds.json?api_key=7JVXTMYE7GWDHAJJ'

    try:
        response = urequests.get(url)
        data = response.json()
        # Assuming your ThingSpeak channel has fields named field1, field2, etc.
        field_value = data['feeds']
        position = int(input("Enter ID: "))
        print("Entery ID: ",field_value[position-1]['entry_id'],"\tField1: ",field_value[position-1]['field1'],"\tField2: ",field_value[position-1]['field2'])
        print("Full detail: ",field_value[position-1])
#         for i in range(len(field_value)):
#             print("\nField1: ",field_value[i]['field1'],"\tField2: ",field_value[i]['field2'])
        # Add more fields as needed
        #print(response.text)
        
        # Print or use the values as needed

    except Exception as e:
        print("Error:", e)

    finally:
        if response:
            response.close()
connect_to_wifi()
# Read ThingSpeak data every 10 seconds
while True:
    read_thingspeak()
    time.sleep(10)
