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
            time.sleep(1)
            result = self.client.publish(self.TOPIC, msg)
            # result: [0, 1]
            status = result[0]
            if status == 0:
                print(f"Send `{msg}` to topic `{self.TOPIC}`")
            else:
                print(f"Failed to send message to topic {self.TOPIC}")
            msg_count += 1
            if msg_count > 5:
                break
    def start(self, msg):
        self.broker_connection()
        self.publish(msg)
    

    





