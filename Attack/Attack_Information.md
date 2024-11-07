## Manipulating Sensor Data to Trigger False Alarms in an IoT System
# Overview
In an IoT-based monitoring system, multiple sensors (such as gas sensors, air quality sensors, and light sensors) are connected to an MQTT broker. The system continuously monitors sensor readings to detect unsafe environmental conditions and trigger alarms when threshold values are exceeded. However, this system is vulnerable to attacks that exploit the MQTT protocol, allowing an attacker to inject false sensor data and manipulate readings.

## Vulnerability / Attack Type
- **Protocol:** MQTT
- **Attack:** Data Manipulation / Message Injection

## Technology Focus
**Internet of Things (IoT):** This attack targets IoT devices using the MQTT protocol to communicate sensor data.

## Tools and Requirements
- Kali Linux:
  - Kali Linux is a security-focused operating system that provides numerous tools for penetration testing and security assessments. It will be used as the attacker's platform in this scenario to simulate MQTT data manipulation.
- Mosquitto:
  - Mosquitto is an open-source MQTT broker and client tool. It will serve as both the MQTT broker (the central server managing message distribution) and the MQTT client for injecting false data.
  - Mosquitto Client (mosquitto_pub and mosquitto_sub commands) will be used to publish messages to the broker and test message injection on specific topics.
- MQTT Server/Broker:
  - An MQTT broker is required to handle the MQTT message traffic between the simulated sensors and clients. This can be set up using Mosquitto or any other MQTT broker software.
  - The broker will manage topics and handle connections between the IoT devices (sensors) and the attacker’s client.
- Python and Paho MQTT Library (for advanced simulation):
  - Python can be used for scripting and automation of the attack scenario.
  - Paho MQTT Library: This Python library enables MQTT communication and will be used to create custom scripts that continuously publish fake sensor data to the MQTT broker.

## Scenario Explanation
An attacker uses an MQTT client, such as Mosquitto Client, to publish false data to specific topics associated with critical sensors. By doing so, the attacker manipulates the sensor readings, making it appear as though dangerous conditions exist when, in reality, everything is normal. This can lead to unnecessary alarms, disrupting operations, or, in the case of safety-critical environments, causing panic or operational shutdowns.

