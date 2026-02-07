import requests
import time
import random
import json

# Configuration of the Processing Node (Cloud or Edge)
SERVER_URL = "http://localhost:5000/api/telemetry"
DEVICE_ID = "GH_TOMATO_SENSOR_01"

def read_virtual_gpio():
    """
    Simulates I/O access to physical sensors.
    Generates stochastic data representing greenhouse conditions.
    """
    # Simulated physiological and environmental parameters
    temp = round(random.uniform(18.0, 35.0), 2)
    hum = round(random.uniform(40.0, 90.0), 2)
    # Normalized transpiration rate
    transpiration = round(random.uniform(0.1, 1.0), 3)

    return {
        "device_id": DEVICE_ID,
        "timestamp": time.time(),
        "temperature": temp,
        "humidity": hum,
        "transpiration": transpiration
    }

def main():
    while True:
        try:
            # 1. Data Acquisition
            payload = read_virtual_gpio()
            
            # 2. Transmission to the Computing Node
            headers = {'Content-type': 'application/json'}
            requests.post(SERVER_URL, data=json.dumps(payload), headers=headers)
            
        except requests.exceptions.ConnectionError:
            print("[Error] Connection to Processing Node failed.")
        
        time.sleep(5) # Sampling interval
