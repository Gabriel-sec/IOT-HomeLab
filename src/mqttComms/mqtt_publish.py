from mqtt_connect import MQTTConnector
import time

# Set the broker address, port and topic(s)    
BROKER_ADDRESS = "broker.emqx.io"
BROKER_PORT = 1883
TOPIC = "python/mqtt"

class MQTTPublisher(MQTTConnector):
    # Client is created and the hooks are attached before the Publisher starts its own work.
    def __init__(self, BROKER_ADDRESS, BROKER_PORT, TOPIC):
        super().__init__(BROKER_ADDRESS, BROKER_PORT)
        self.TOPIC=TOPIC
        
    def publish(self):
        msg_count = 1
        while True:
            time.sleep(1)
            msg = f"messages: {msg_count}"
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
    def start(self):
        self.broker_connection()
        self.publish()
            
if __name__ == "__main__":
    mqtt_publish = MQTTPublisher(BROKER_ADDRESS,BROKER_PORT, TOPIC)
    mqtt_publish.start()
    time.sleep(2)
    mqtt_publish.client.loop_stop()

    





