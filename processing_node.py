from flask import Flask, request, jsonify
import requests

app = Flask(__name__)
ADMIN_ENDPOINT = "http://localhost:5000/admin/alert" 

# Thresholds acting as a proxy for the LSTM model decision boundary
THRESHOLDS = {"temp_max": 32.0, "hum_min": 45.0}

def analyze_data(data):
    """
    Analyzes incoming telemetry.
    Returns a list of anomalies if thresholds are breached.
    """
    anomalies = []
    if data['temperature'] > THRESHOLDS['temp_max']:
        anomalies.append(f"Critical Temp: {data['temperature']}C")
    if data['humidity'] < THRESHOLDS['hum_min']:
        anomalies.append(f"Low Humidity: {data['humidity']}%")
    return anomalies

@app.route('/api/telemetry', methods=['POST'])
def receive_telemetry():
    content = request.json
    # Execute Anomaly Detection
    detected_issues = analyze_data(content)

    if detected_issues:
        # Trigger Alert to Administrator
        alert_payload = {
            "severity": "HIGH",
            "device": content['device_id'],
            "issues": detected_issues
        }
        try:
            # Unencrypted communication as per PoC requirements
            requests.post(ADMIN_ENDPOINT, json=alert_payload)
        except:
            pass 
        return jsonify({"status": "alert_triggered"}), 200
        
    return jsonify({"status": "nominal"}), 200
