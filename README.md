# MQTT_Attack
The rise of the Internet of Things (IoT) has led to an increase in devices connected to the internet, all exchanging data in real-time. One of the most popular protocols facilitating this communication is the Message Queuing Telemetry Transport (MQTT) protocol. Initially designed for constrained devices and low-bandwidth, high-latency networks, MQTT has become the de facto protocol for IoT due to its lightweight nature and efficiency. However, as with any networked protocol, MQTT is vulnerable to various security risks and potential attacks. This project aims to explore MQTT, its inherent security challenges, and common attack vectors to better understand the protocol's limitations and the risks associated with IoT networks.

## About MQTT
MQTT (Message Queuing Telemetry Transport) is a lightweight, publish-subscribe protocol that operates on top of the TCP/IP stack, designed for resource-constrained environments. Created in 1999 by IBM for monitoring oil pipelines, MQTT is widely used in IoT applications, where network bandwidth and power usage are limited. Key aspects of MQTT include:

- **Low Cost:** Due to its simplicity and low overhead, MQTT is economical in terms of data and resource usage, making it ideal for IoT applications.
- **Low Bandwidth:** MQTT minimizes bandwidth usage, allowing efficient communication even on limited networks.
- **Handles Unstable Connections:** The protocol is built to handle unreliable connections, allowing for intermittent connectivity without losing messages.
- **Port 1883:** MQTT communicates over TCP/IP, typically using port 1883 for unencrypted data transmission.

MQTT enables devices, or "clients," to communicate via a central server called a "broker." The broker receives and distributes messages between clients, facilitating decoupled, real-time data exchange.

## Key Features of MQTT
