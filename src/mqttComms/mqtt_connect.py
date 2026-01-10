import socket #This comes pre-installed with Python. No need to define it as a dependency in poetry
import paho.mqtt.client as mqtt
from src.config.settings import API_VERSION, MQTT_VERSION

class MQTTConnector():
    def __init__(self,BROKER_ADDRESS,BROKER_PORT):
            # Create an MQTT client instance and using the mqtt version v5
            self.client=mqtt.Client(callback_api_version=API_VERSION, protocol=MQTT_VERSION)
            
            self.BROKER_ADDRESS=BROKER_ADDRESS
            self.BROKER_PORT=BROKER_PORT

            #As soon as the object is born, it knows exactly how to behave: connect or disconnect
            self.client.on_connect = self.on_connect_callback
            self.client.on_disconnect = self.on_disconnect_callback
    
    # Callback function when the client connects to the broker
    def on_connect_callback(self, client, userdata, flags, reason_code, properties=None):
        if reason_code == 0:
            print("Connected to MQTT broker")
        # Handles OSI layers 5, 6, 7: MQTT CONNACK from the broker (authentication, protocol-level accept/reject). A non-zero reason/code can occur even after a successful TCP connection.
        else:
            print(f"Failed to connect, result code {reason_code}")
    
    def on_disconnect_callback(self, client, userdata, disconnect_flags, reason_code, properties=None):
        print("Disconnected from broker.")

    def broker_connection(self):
        try:
            # Connect to the broker
            """My custom function "on_connect_callback" is now connected to the "client.on_connect" hook from the paho.mqtt.client library. 
            This command runs the on_connect function automatically the moment the connection is established with the broker.
            By not specify the () the function to "on_connect_callback", Python will not execute the function immediately. This creates an event handler. The hook executes only when the connection is established."""
            self.client.connect(self.BROKER_ADDRESS, self.BROKER_PORT, 10)
            self.client.loop_start()
        except socket.gaierror as e:
            # Handles OSI Layers 3 and 4: DNS/socket/connect-level errors/timeouts/TCP errors
            print(f"Name resolution failed for broker '{self.BROKER_ADDRESS}': {e}")
            print("Use a valid hostname or IP (e.g. 'localhost' or '127.0.0.1') or run a local broker like Mosquitto.")
            # let the caller decide how to handle the failure
            raise RuntimeError("DNS/socket error connecting to broker") from e
        except Exception as e:
            print(f"Failed to connect to MQTT broker: {e}")
            raise