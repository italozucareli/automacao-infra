import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}", "Content-Type": "application/json"}
URL = "https://api.thousandeyes.com/v7/endpoint/test-run" # Exemplo para Endpoint

def run_instant_test(endpoint_agent_id, target_domain):
    payload = {
        "agentId": endpoint_agent_id,
        "target": target_domain,
        "testType": "network"
    }
    res = requests.post(URL, headers=HEADERS, json=payload)
    if res.status_code == 201:
        print(f"Teste instantâneo disparado contra {target_domain}!")
    else:
        print(f"Falha: {res.text}")

if __name__ == "__main__":
    run_instant_test(1234, "google.com")