from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Configurações do Grafana
GRAFANA_URL = "https://seu-grafana.com/api/annotations"
GRAFANA_API_KEY = "SUA_API_KEY_GRAFANA"

@app.route('/te-webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    
    # Extrai informações relevantes do alerta do ThousandEyes
    alert_name = data.get('alert', {}).get('ruleName', 'Alerta TE')
    test_name = data.get('test', {}).get('testName', 'Teste')
    status = data.get('alert', {}).get('state', 'UNKNOWN') # ACTIVE ou CLEARED

    # Prepara anotação para o Grafana
    payload = {
        "text": f"ThousandEyes: {alert_name} no teste {test_name} - Status: {status}",
        "tags": ["ThousandEyes", "NetworkAlert", status],
    }
    
    headers = {
        "Authorization": f"Bearer {GRAFANA_API_KEY}",
        "Content-Type": "application/json"
    }

    # Envia para o Grafana
    requests.post(GRAFANA_URL, json=payload, headers=headers)
    
    return jsonify({"status": "success"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)