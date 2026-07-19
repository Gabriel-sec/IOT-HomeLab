from src.mqttComms.mqtt_connect import MQTTConnector

class MQTTSubscriber(MQTTConnector):
    def __init__(self,BROKER_ADDRESS,BROKER_PORT,TOPIC):
        super().__init__(BROKER_ADDRESS,BROKER_PORT)
        self.TOPIC=TOPIC
        self.client.on_message = self.on_message_callback

        # Note: self.client.on_connect is already mapped to self.on_connect_callback 
        # in the parent class's __init__ method!

    def on_connect_callback(self, client, userdata, flags, reason_code, properties=None):
        # 1. Run the parent's code first (this prints the "Connected..." message)
        super().on_connect_callback(client,userdata,flags,reason_code,properties)

        # 2. Add the crucial subscription logic so it triggers on every reconnect!
        #By moving the subscription into the on_connect_callback, its ties the act of subscribing directly to the act of connecting, guaranteeing they always happen together.
        if reason_code == 0:
            self.client.subscribe(self.TOPIC)
            print(f"Listening on {self.TOPIC}...")
    
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
        # Just establish the connection. The on_connect_callback will handle the subscription.
        self.broker_connection()