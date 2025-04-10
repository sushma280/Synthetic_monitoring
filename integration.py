import yaml
import json
import time
import pingparsing

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

for server in servers:
    print(f"\nPinging {server}...")
    transmitter.destination = server
    result = transmitter.ping()
    print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))
    print("\n")

    if server != servers[-1]:
        print(f"Waiting {interval} seconds before next server...\n")
        time.sleep(interval)

