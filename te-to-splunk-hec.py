import requests
import json
import time

TE_TOKEN = "SEU_TE_TOKEN"
SPLUNK_HEC_URL = "https://splunk.suaempresa.com:8088/services/collector"
SPLUNK_HEC_TOKEN = "SEU_SPLUNK_TOKEN"
TEST_ID = "112233"

def send_metrics_to_splunk():
    te_headers = {"Authorization": f"Bearer {TE_TOKEN}"}
    te_url = f"https://api.thousandeyes.com/v7/net/metrics/{TEST_ID}"
    
    results = requests.get(te_url, headers=te_headers).json().get('results', [])
    
    splunk_headers = {"Authorization": f"Splunk {SPLUNK_HEC_TOKEN}"}
    
    print(f"Enviando {len(results)} métricas para o Splunk...")
    for res in results:
        payload = {
            "time": time.time(),
            "host": res.get('agent', {}).get('agentName'),
            "source": "thousandeyes_api",
            "sourcetype": "_json",
            "event": {
                "testId": TEST_ID,
                "loss": res.get('loss'),
                "latency": res.get('avgLatency'),
                "jitter": res.get('jitter')
            }
        }
        # Envia evento por evento para o Splunk
        requests.post(SPLUNK_HEC_URL, headers=splunk_headers, json=payload, verify=False)
    
    print("Integração com Splunk concluída.")

if __name__ == "__main__":
    send_metrics_to_splunk()