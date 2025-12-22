import time
import random
import paho.mqtt.client as mqtt

def get_virtual_temp():
    # Simulates a temperature between 18.0°C and 26.0°C
    return round(random.uniform(18.0, 26.0), 2)

if __name__ == "__main__":
    print("Virtual Sensor Started. Press Ctrl+C to stop.")
    while True:
        temp = get_virtual_temp()
        # Send data to MQTT broker
        
        print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} Sensor ID: SN-1001 | Temperature: {temp}°C\n", flush=True)

        time.sleep(5) # Send data every 5 seconds