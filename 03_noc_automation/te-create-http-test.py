import requests
import json

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}", "Content-Type": "application/json"}
URL = "https://api.thousandeyes.com/v7/tests/http-server"

def create_test(url_target, test_name):
    payload = {
        "interval": 300,
        "alertsEnabled": 1,
        "testName": test_name,
        "url": url_target,
        # IDs dos Enterprise Agents que vao rodar o teste (ex: SP e RJ)
        "agents": [{"agentId": 12345}, {"agentId": 67890}]
    }
    
    res = requests.post(URL, headers=HEADERS, json=payload)
    if res.status_code == 201:
        print(f"Teste '{test_name}' criado com sucesso para a URL {url_target}!")
    else:
        print(f"Erro: {res.text}")

if __name__ == "__main__":
    create_test("https://meu-novo-sistema.com.br", "API de Pagamentos - Prod")