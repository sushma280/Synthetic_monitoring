import yaml
import json
import time
import pingparsing
from prometheus_client import start_http_server , Gauge

rtt_min = Gauge("rtt_minimum","Minimum RTT value",["server"])
rtt_max = Gauge("rtt_maximum","Maximum RTT value",["server"])
rtt_avg = Gauge("rtt_average","Average RTT value",["server"])
packet_transmit = Gauge("packet_transmit","packets transmitted",["server"])
packet_receive = Gauge("packet_receive","packets received",["server"])
packet_loss_count = Gauge("packet_loss_count","packets lost count",["server"])
packet_loss_rate = Gauge("packet_loss_rate","packets lost percentage",["server"])

file_path = "C:/Users/sushm/Downloads/Python proj/sample_file.yaml"

try:
    with open(file_path, "r") as f:
        sample = yaml.safe_load(f)
        print("YAML file loaded successfully.")
        print("Configuration file details: ", sample)

        servers = sample.get("servers", [])
        interval = sample.get("interval", 10)

except FileNotFoundError:
    print(f"Error: The file {file_path} is not found. Make sure you provided the correct path.")
except PermissionError:
    print(f"Error: Permission denied. The file doesn't have permission rights. Check with the owner of the file")
except yaml.YAMLError as e:
    print(f"Error: file format is incorrect. Details: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")


ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.count = 4  

start_http_server(8989)
print("Prometheus metrics server started on port 8989...")


while True:
    for server in servers:
        print(f"\nPinging {server} {transmitter.count} times...")
        transmitter.destination = server
        result = transmitter.ping()
        parsed = ping_parser.parse(result).as_dict()
        print(json.dumps(parsed, indent=4))
        print("\n")

        rtt_min.labels(server=server).set(parsed.get('rtt_min',0.0))
        rtt_max.labels(server=server).set(parsed.get('rtt_max',0.0))
        rtt_avg.labels(server=server).set(parsed.get('rtt_avg',0.0))
        packet_transmit.labels(server=server).set(parsed.get('packet_transmit',0.0))
        packet_receive.labels(server=server).set(parsed.get('packet_receive',0.0))
        packet_loss_count.labels(server=server).set(parsed.get('packet_loss_count',0.0))
        packet_loss_rate.labels(server=server).set(parsed.get('packet_loss_rate',0.0))
        
        print(f"Waiting {interval} seconds before next server...\n")
        time.sleep(interval)



