from src.mqttComms.mqtt_connect import MQTTConnector
import time #This comes pre-installed with Python. No need to define it as a dependency in poetry

class MQTTPublisher(MQTTConnector):
    # Client is created and the hooks are attached before the Publisher starts its own work.
    def __init__(self, BROKER_ADDRESS, BROKER_PORT, TOPIC):
        super().__init__(BROKER_ADDRESS, BROKER_PORT)
        self.TOPIC=TOPIC
        
    def publish(self, msg):
        msg_count = 1
        while True:
            time.sleep(0.4)
            # Send the message 
            result = self.client.publish(self.TOPIC, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{self.TOPIC}`")
            else:
                print(f"Failed to send message to topic {self.TOPIC}")
            msg_count += 1
            if msg_count > 2:
                break
    def start(self, msg):
        # 1. Trigger the connection
        self.broker_connection()
        # Instead of guessing how long the network handshake will take, this forces the script to wait exactly as long as necessary (checking every 100 milliseconds) before letting the publish() loop begin.
        while not self.client.is_connected():
            time.sleep(0.1)
        
        # 3. Now that the green light is given, start publishing
        self.publish(msg)
    

    





