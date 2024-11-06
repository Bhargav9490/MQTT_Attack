# MQTT_Attack
The rise of the Internet of Things (IoT) has led to an increase in devices connected to the internet, all exchanging data in real-time. One of the most popular protocols facilitating this communication is the Message Queuing Telemetry Transport (MQTT) protocol. Initially designed for constrained devices and low-bandwidth, high-latency networks, MQTT has become the de facto protocol for IoT due to its lightweight nature and efficiency. However, as with any networked protocol, MQTT is vulnerable to various security risks and potential attacks. This project aims to explore MQTT, its inherent security challenges, and common attack vectors to better understand the protocol's limitations and the risks associated with IoT networks.

## About MQTT
MQTT (Message Queuing Telemetry Transport) is a lightweight, publish-subscribe protocol that operates on top of the TCP/IP stack, designed for resource-constrained environments. Created in 1999 by IBM for monitoring oil pipelines, MQTT is widely used in IoT applications, where network bandwidth and power usage are limited. Key aspects of MQTT include:

- **Low Cost:** Due to its simplicity and low overhead, MQTT is economical in terms of data and resource usage, making it ideal for IoT applications.
- **Low Bandwidth:** MQTT minimizes bandwidth usage, allowing efficient communication even on limited networks.
- **Handles Unstable Connections:** The protocol is built to handle unreliable connections, allowing for intermittent connectivity without losing messages.
- **Port 1883:** MQTT communicates over TCP/IP, typically using port 1883 for unencrypted data transmission.

![GitHub Logo](https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png)

MQTT enables devices, or "clients," to communicate via a central server called a "broker." The broker receives and distributes messages between clients, facilitating decoupled, real-time data exchange.

## Key Features of MQTT

- **Publish-Subscribe Model:** Clients publish messages to specific topics, and other clients subscribe to those topics. This decouples message senders and receivers.
- **QoS (Quality of Service) Levels:** MQTT supports three levels of Quality of Service to manage message delivery reliability:
  - QoS 0: At most once (fire-and-forget).
  - QoS 1: At least once (message will be delivered at least once, potentially multiple times).
  - QoS 2: Exactly once (guaranteed message delivery without duplicates).
- **Retained Messages:** The broker can retain the last message sent on a topic, enabling newly connected clients to receive it immediately upon subscribing.
- **Will Messages:** If a client disconnects unexpectedly, the broker can send a predefined "last will" message to notify other clients.

## Common Use Cases
MQTT is widely used in:
- IoT devices like smart homes, healthcare monitoring, and industrial control systems.
- Mobile applications, especially where efficient use of network resources is critical.
- Real-time systems requiring frequent updates with minimal latency.

