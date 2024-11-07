import paho.mqtt.client as mqtt
import time
import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 5:
    print("Usage: script.py <broker_address> <topic> <message> <delay>")
    sys.exit(1)

# Get command-line arguments
broker_address = sys.argv[1]
topic = sys.argv[2]
message = sys.argv[3]
delay = float(sys.argv[4])  # Convert delay to float

print(f"Arguments received - Broker: {broker_address}, Topic: {topic}, Message: {message}, Delay: {delay}")

# Create an MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address)

# Continuously send the message to the topic
try:
    while True:
        client.publish(topic, message)
        print(f"Data '{message}' sent to topic {topic}")
        time.sleep(delay)  # Use the delay provided in seconds
except KeyboardInterrupt:
    print("Process interrupted")
finally:
    client.disconnect()
