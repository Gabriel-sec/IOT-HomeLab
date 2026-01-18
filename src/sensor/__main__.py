from src.config import BROKER_ADDRESS, BROKER_PORT, TOPIC
import argparse
from src.mqttComms.mqtt_subscribe import MQTTSubscriber
from src.mqttComms.mqtt_publish import MQTTPublisher
from src.sensor.temperature_sensor_logic import run_publisher, run_subscriber

def start():
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
        print("🚀 Starting MQTT Publisher...Press Ctrl+C to stop.")
        # Gather mqtt publish class to send a message
        mqtt_publish = MQTTPublisher(BROKER_ADDRESS,BROKER_PORT, TOPIC)
        mqtt_publish.broker_connection()
        run_publisher(mqtt_publish)
        
    elif mode in ["sub", "subscribe", "s"]:
        print("📥 Starting MQTT Subscriber...Press Ctrl+C to stop.")
        mqtt_subscribe = MQTTSubscriber(BROKER_ADDRESS,BROKER_PORT, TOPIC)
        mqtt_subscribe.broker_connection()
        run_subscriber(mqtt_subscribe)        

if __name__ == "__main__":
    start()   