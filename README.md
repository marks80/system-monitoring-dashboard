Automated System Monitoring Dashboard Project (ASMDP) overview

ASMDP is a system/service designed to monitor 3 key server metrics - 
- CPU
- memory
- disk usage.

Built with Python, InfluxDB, Docker, Grafana.  This project automates the collection of system data and visualizes it in a Grafana dashboard, providing insights into the health and performance of a server.

Goal
The goal of this project is to demonstrate the ability to automate system monitoring tasks, important skill for any DevOps engineer. 
By using Python to collect server metrics and Grafana to visualize them, this project aims to offer a user-friendly way to monitor server performance in real time.

Tech Stack
Python: Used to write the script for collecting server metrics (CPU, memory, disk usage).
Docker: Containerizes the app for portability and easy deployment.
Grafana: Provides the dashboard to visualize the collected metrics in real-time.
InfluxDB: Stores the collected data.

Features
Collects CPU, memory and disk usage statistics from the server.
Stores the collected data in InfluxDB.
Visualizes the metrics using Grafana in real-time.
Containerized application using Docker for easy deployment.

Getting Started
Prerequisites
Docker: Ensure Docker is installed on your machine. Install Docker.

Grafana: Set up a Grafana instance for visualizing your metrics. http://localhost:3000 login - admin pass - alabama23

InfluxDB: Used for storing collected data. http://localhost:8086 login - cybermark1980 pass - alabama23 

Installation

Clone this repository:
bash
Copy code
git clone https://github.com/marks80/system-monitoring-dashboard.git

Navigate to the project folder:
bash
Copy code
cd system-monitoring-dashboard

Build and run the application using Docker:
Copy code
docker-compose up

Access Grafana to visualize your metrics:
Default login: admin / alabama23

Usage
Once the application is running, it will start collecting metrics from the server. 

Open your Grafana dashboard to view real-time system performance data.

License
This project is licensed under the MIT License - see the LICENSE file for details.
