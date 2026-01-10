import time
import random
from src.config import BROKER_ADDRESS, BROKER_PORT, TOPIC
import argparse
from src.mqttComms.mqtt_subscribe import MQTTSubscriber
from src.mqttComms.mqtt_publish import MQTTPublisher


def get_virtual_temp():
    # Simulates a temperature between 18.0°C and 26.0°C
    return round(random.uniform(18.0, 26.0), 2)

def run_publisher(mqtt_publish):
    temp = get_virtual_temp()
    msg=f"{time.strftime('%Y-%m-%d %H:%M:%S')} Sensor ID: SN-1001 | Temperature: {temp}°C\n"
    mqtt_publish.start(msg)
    time.sleep(0.2)
    mqtt_publish.client.loop_stop()

def run_subscriber(mqtt_subscribe):
    mqtt_subscribe.start()        
    try:
        # Keep listening indefinitely (Ctrl+C to stop)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping subscriber...")
    finally:
        mqtt_subscribe.client.loop_stop()
        mqtt_subscribe.client.disconnect()

def main():
    parser = argparse.ArgumentParser(description="IOT HomeLab Controller")
    
    # Add the mode argument
    parser.add_argument(
        "mode", 
        choices=["pub", "sub", "publish", "subscribe", "p", "s"], 
        help="Run as a publisher or subscriber"
    )

    args = parser.parse_args()

    # Normalize the input (e.g., treat 'pub' and 'publish' the same)
    mode = args.mode.lower()

    if mode in ["pub", "publish", "p"]:
        print("🚀 Starting MQTT Publisher...")
        # Gather mqtt publish class to send a message
        mqtt_publish = MQTTPublisher(BROKER_ADDRESS,BROKER_PORT, TOPIC)
        try: 
            while True:
                run_publisher(mqtt_publish)
                time.sleep(5) # Send data every 5 seconds
        except KeyboardInterrupt:
            print("Stopping virtual IOT instance")
        finally:
            mqtt_publish.client.loop_stop() # Stop only when exiting the program
            mqtt_publish.client.disconnect()
    elif mode in ["sub", "subscribe", "s"]:
        print("📥 Starting MQTT Subscriber...")
        mqtt_subscribe = MQTTSubscriber(BROKER_ADDRESS,BROKER_PORT, TOPIC)
        try:
            run_subscriber(mqtt_subscribe)
        except KeyboardInterrupt:
            print("Stopping virtual IOT instance")
        finally:
            mqtt_subscribe.client.disconnect()


if __name__ == "__main__":
    print("Virtual Sensor Started. Press Ctrl+C to stop.")
    main()    
        
        