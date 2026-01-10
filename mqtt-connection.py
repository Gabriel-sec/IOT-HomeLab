import sys
import socket
import paho.mqtt.client as mqtt

# Callback function when the client connects to the broker
def on_connect_callback(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        print("Connected to MQTT broker")
    # Handles OSI layers 5, 6, 7: MQTT CONNACK from the broker (authentication, protocol-level accept/reject). A non-zero reason/code can occur even after a successful TCP connection.
    else:
        print(f"Failed to connect, result code {reason_code}")

# Create an MQTT client instance and using the mqtt version v5
client = mqtt.Client(protocol=mqtt.MQTTv5, callback_api_version=2)
"""My custom function "on_connect_callback" is now connected to the "client.on_connect" hook from the paho.mqtt.client library. 
This command runs the on_connect function automatically the moment the connection is established with the broker.
By not specify the () the function to "on_connect_callback", Python will not execute the function immediately. This creates an event handler. The hook executes only when the connection is established."""
client.on_connect = on_connect_callback

# Set the broker address and port
broker_address = "broker.emqx.io"
port = 1883


try:
    # Connect to the broker
    client.connect(broker_address, port, 5)
# Handles OSI Layers 3 and 4: DNS/socket/connect-level errors/timeouts/TCP errors
except socket.gaierror as e:
    print(f"Name resolution failed for broker '{broker_address}': {e}")
    print("Use a valid hostname or IP (e.g. 'localhost' or '127.0.0.1') or run a local broker like Mosquitto.")
    sys.exit(1)
except Exception as e:
    print(f"Failed to connect to MQTT broker: {e}")
    sys.exit(1)

# Start the MQTT client loop to handle network traffic
client.loop_start()
