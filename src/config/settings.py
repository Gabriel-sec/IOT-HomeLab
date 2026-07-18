from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.client as mqtt

#Keep all constants and file paths in one place to avoid hardcoding.
# Set the broker address, port and topic(s)    
BROKER_ADDRESS = "localhost"
BROKER_PORT = 1833
TOPIC = "python/mqtt"
API_VERSION=CallbackAPIVersion.VERSION2
MQTT_VERSION=mqtt.MQTTv5
