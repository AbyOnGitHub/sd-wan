Introduction

Campus networks increasingly rely on multiple ISPs to maintain reliable connectivity for academic, administrative, and research activities. However, traditional routing protocols such as RIP and OSPF:

•	Use static metrics (hop count, cost) 

•	Do not adapt to real-time conditions 

•	Cannot prioritize applications 

•	Inefficiently use multiple ISPs 

These limitations result in higher latency, packet loss, poor user experience, and underutilized bandwidth. The proposed SD-WAN system uses Python and open-source tools to enable intelligent, real-time path selection across multiple network links, replacing static routing with software-defined control.
 
Proposed Solution

This project implements a Python-based SD-WAN system that:

•	Monitors multiple network links in real-time 

•	Measures performance metrics (latency, packet loss) 

•	Dynamically selects the best path   

•	Automatically switches traffic during failures

Key Idea: Replace static routing decisions with intelligent, 
software-driven control.

Objectives

This project implements a Python-based SD-WAN system that:

1.	Develop a low-cost SD-WAN prototype using Python.
2.	Enable dynamic path selection based on real network data.
3.	Implement automatic failover between multiple ISPs.
4.	Validate system behavior using packet analysis (Wireshark).
5.	Ensure scalability for campus deployment.

Components:

1. SD-WAN Edge Device, 

•	Working computer(Laptop) connected to: WiFi (ISP 1), Mobile Hotspot/Ethernet (ISP 2)

2. Python Controller

•	Core logic of the system

•	Performs: Monitoring, Decision making, Routing control

3. Operating System (Networking Layer)

•	Executes routing changes

•	Forwards actual traffic

4. Wireshark

•	Captures and analyzes packets

•	Verifies system behavior

Methodology

Step 1: Multi-Link Setup

•	Connect system to two different networks

Step 2: Network Monitoring

•	Python script continuously measures:

•	Latency (via ping)

•	Packet loss

•	Link availability

Step 3: Path Selection Algorithm

A scoring system is used:
•	Score = (Latency × Weight) + (Packet Loss × Weight)

•	Lower score = better link

•	Best link selected dynamically

Step 4: Routing Control

•	Python executes system commands:

•	Changes default route

•	Redirects traffic via selected ISP

Step 5: Failover Mechanism

•	If primary link fails → switch to backup

•	When restored → switch back

Step 6: Traffic Verification

•	Using Wireshark

•	Capture ICMP packets

•	Observe traffic path changes

•	Validate system decisions

