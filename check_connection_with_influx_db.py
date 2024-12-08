from influxdb_client import InfluxDBClient

url = "http://localhost:8086"
token = "your_influxdb_token_here"
org = "NoName"

try:
    client = InfluxDBClient(url=url, token=token, org=org)
    health = client.health()
    print("Connection Successful:", health.status)
except Exception as e:
    print("Connection Failed:", str(e))
