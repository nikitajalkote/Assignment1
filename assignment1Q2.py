import psutil
import time

def monitor_cpu(threshold):
    print("Monitoring CPU usage")

    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            print(f"Current CPU usage: {cpu_usage}%")

            if cpu_usage > threshold:
                print(f"Alert for CPU usage exceeds threshold: {cpu_usage}%")

    except KeyboardInterrupt:
        print("\nMonitoring stopped.")

if __name__ == "__main__":
    # Set the threshold
    threshold = 80
    monitor_cpu(threshold)
