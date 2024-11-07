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
