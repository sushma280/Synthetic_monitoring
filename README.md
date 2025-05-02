
# 🛰️ Synthetic Monitoring Project (Python + Prometheus + Grafana)

This project is a simple synthetic monitoring system I built to **track server health** using Python, Prometheus, and Grafana. It collects **RTT**, **latency**, and **packet loss** metrics by pinging target servers and visualizing the data in real-time.

🎓 Built as part of the **Build Fellowship Program by Open Avenues**, with guidance from **Sonu Gupta**. Thank you for the support and mentorship!

![ChatGPT Image May 2, 2025, 11_09_05 AM](https://github.com/user-attachments/assets/d9ec2a82-2129-42c3-8884-efdd07e26e3d)


---

## 📋 Goal

To simulate a real-world DevOps/SRE use case by building a monitoring tool that:
- **Pings servers** regularly
- Collects metrics like **RTT**, **packet loss**, etc.
- **Exposes those metrics** via an HTTP endpoint in Prometheus format
- **Scrapes the metrics using Prometheus**
- **Visualizes them in Grafana**

---

## 🛠️ Tools & Technologies Used

- **Python**: For scripting the ping logic and serving metrics
- **Prometheus**: For scraping and storing time-series data
- **Grafana**: For dashboards and visualization
- **prometheus_client**: Python library for exposing metrics
- **pingparsing**: For parsing ping output
- **Wireshark** (for network analysis & observability exploration)
- Localhost for testing (`localhost:8989`, `9090`, `3000`)

---

## ✅ Step-by-Step Breakdown of What I Did

### 1️⃣ Wrote Python Script to Ping Servers Using `pingparsing`

- Used the `pingparsing` library to send pings and parse responses easily.

```python
import pingparsing

# Initialize parser and transmitter
ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()

# Set destination and number of pings
transmitter.destination = input("Enter the server name: ")
transmitter.count = 10

# Send ping and parse the result
result = transmitter.ping()
parsed = ping_parser.parse(result).as_dict()
```

---

### 2️⃣ Defined Metrics with Prometheus Client

```python
from prometheus_client import Gauge

rtt_min = Gauge("rtt_minimum", "Minimum RTT value", ["server"])
rtt_avg = Gauge("rtt_average", "Average RTT value", ["server"])
rtt_max = Gauge("rtt_maximum", "Maximum RTT value", ["server"])
packet_loss = Gauge("packet_loss_rate", "Packet loss rate", ["server"])
```

---

### 3️⃣ Updated Metric Values

```python
rtt_min.labels(server=server).set(parsed.get('rtt_min', 0.0))
rtt_avg.labels(server=server).set(parsed.get('rtt_avg', 0.0))
rtt_max.labels(server=server).set(parsed.get('rtt_max', 0.0))
packet_loss.labels(server=server).set(parsed.get('packet_loss_rate', 0.0))
```

---

### 4️⃣ Exposed Metrics via HTTP

```python
from prometheus_client import start_http_server

start_http_server(8989)
```

Prometheus scrapes metrics from `http://localhost:8989/metrics`.

---

### 5️⃣ Configured Prometheus

In `prometheus.yml`:

```yaml
scrape_configs:
  - job_name: 'synthetic-monitoring'
    static_configs:
      - targets: ['localhost:8989']
```

Run with:

```bash
./prometheus --config.file=prometheus.yml
```

Access Prometheus at `http://localhost:9090`.

---

### 6️⃣ Set Up Grafana

- Visit `http://localhost:3000`
- Login with default (`admin/admin`)
- Add Prometheus as a data source
- Build dashboards using:
  - RTT min/avg/max
  - Packet loss trends

<img width="959" alt="image" src="https://github.com/user-attachments/assets/58aabb64-5392-4e88-8f26-7a7c6020010d" />
---

## 🧪 Sample Metrics Output

```text
rtt_maximum{server="google.com"} 8.0
rtt_maximum{server="reddit.com"} 6.0
rtt_maximum{server="flipkart.com"} 259.0
rtt_maximum{server="asos.com"} 9.0
```
<img width="291" alt="image" src="https://github.com/user-attachments/assets/58fc9c03-07ee-476e-a396-996c3bf9aa2d" />

---

## 📈 What I Learned

- How to expose real-time custom metrics from Python
- Time-series monitoring and observability concepts
- Setting up a full monitoring pipeline: Python → Prometheus → Grafana


## 🙋 Contact

**Sushma Ayenampudi**  
📧 sushma.ayenampudi@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/sushma-ayenampudi/)
