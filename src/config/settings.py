from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.client as mqtt

#Keep all constants and file paths in one place to avoid hardcoding.
# Set the broker address, port and topic(s)    
BROKER_ADDRESS = "broker.emqx.io"
BROKER_PORT = 1883
TOPIC = "python/mqtt"
API_VERSION=CallbackAPIVersion.VERSION2
MQTT_VERSION=mqtt.MQTTv5