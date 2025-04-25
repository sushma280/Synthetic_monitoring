import json
import pingparsing

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = input("Enter the server name: ")
transmitter.count = 10
result = transmitter.ping()


print("\n Ping Metrics: \n")
print(json.dumps(ping_parser.parse(result).as_dict(), indent=4))