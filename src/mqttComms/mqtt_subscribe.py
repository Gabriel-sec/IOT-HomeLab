from src.mqttComms.mqtt_connect import MQTTConnector
import time
from src.config import BROKER_ADDRESS, BROKER_PORT, TOPIC

class MQTTSubscriber(MQTTConnector):
    def __init__(self,BROKER_ADDRESS,BROKER_PORT,TOPIC):
        super().__init__(BROKER_ADDRESS,BROKER_PORT)
        self.TOPIC=TOPIC
        self.client.on_message = self.on_message_callback

    def on_message_callback(self, client, userdata, msg):
        try:
            #Decode the bytes sent by MQTT
            readable_msg=msg.payload.decode("utf-8")
        except UnicodeDecodeError:
            # If it's not text, we assign this "fake" message so the print() still works
            readable_msg = "[Non-text data]"
            #Using msg.topic instead of self.topic to know which topic specifically you are receicing the message from
        print(f"New Message: {readable_msg} from {msg.topic}")
    
    def start(self):
        self.broker_connection()
        #Tell the broker we want to listen to this topic
        self.client.subscribe(self.TOPIC)
        print(f"Listening on {self.TOPIC}...")

    