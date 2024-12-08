import psutil
import time
from influxdb_client import InfluxDBClient, Point # type: ignore
from influxdb_client.client.write_api import SYNCHRONOUS # type: ignore

# InfluxDB configuration
bucket = "BucketMonitor"
org = "NoName"
token = "JZk5SzGbssWOZ3QUPZi90h4XzBLwar_tHsuuTfqXfAE052qCK9jxDjFzB8cHiqSX8gUy4I-1OS4qi-NEIG4j2Q=="
url = "http://localhost:8086"

client = InfluxDBClient(url=url, token=token, org=org)
write_api = client.write_api(write_options=SYNCHRONOUS)

# Function to collect system metrics
def collect_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
    }


# Function to send metrics to InfluxDB
def send_metrics(metrics):
    point = Point("system_metrics").tag("host", "localhost")
    for key, value in metrics.items():
        point = point.field(key, value)
    write_api.write(bucket=bucket, org=org, record=point)

# Main loop to collect and send metrics every 5 seconds
while True:
    metrics = collect_metrics()
    print(f"Collected metrics: {metrics}")
    send_metrics(metrics)
    time.sleep(5)
