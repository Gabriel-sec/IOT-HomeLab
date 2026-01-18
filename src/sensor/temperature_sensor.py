import random
import time

def get_virtual_temp():
    # Simulates a temperature between 18.0°C and 26.0°C
    return round(random.uniform(18.0, 26.0), 2)

def run_publisher(mqtt_publish):
    try: 
        while True:
            temp = get_virtual_temp()
            timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
            msg=f"{timestamp} Sensor ID: SN-1001 | Temperature: {temp}°C\n"
            mqtt_publish.start(msg)
            time.sleep(5)
    except KeyboardInterrupt:
        print("Stopping publisher")
    finally:
        mqtt_publish.client.loop_stop() # Stop only when exiting the program
        mqtt_publish.client.disconnect()

def run_subscriber(mqtt_subscribe):
    try:
        mqtt_subscribe.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping subscriber...")
    finally:
        mqtt_subscribe.client.loop_stop()
        mqtt_subscribe.client.disconnect()

 
        
        