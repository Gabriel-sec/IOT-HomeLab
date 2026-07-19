import os
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion

#Keep all constants and file paths in one place to avoid hardcoding.
# Set the broker address, port and topic(s)    
BROKER_ADDRESS = os.getenv("BROKER_ADDRESS", "host.docker.internal")
BROKER_PORT = int(os.getenv("BROKER_PORT", "1883"))
TOPIC = os.getenv("TOPIC", "python/mqtt")
API_VERSION=CallbackAPIVersion.VERSION2
MQTT_VERSION=mqtt.MQTTv5
