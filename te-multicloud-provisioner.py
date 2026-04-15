import requests

TE_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_TOKEN}", "Content-Type": "application/json"}
TEST_ID = "112233"

# IDs oficiais da ThousandEyes para nuvens em SP/Virginia
CLOUD_AGENTS = [{"agentId": 234}, # AWS us-east-1
                {"agentId": 182}, # Azure Sao Paulo
                {"agentId": 218}] # GCP Sao Paulo

def ensure_multicloud_presence():
    url = f"https://api.thousandeyes.com/v7/tests/http-server/{TEST_ID}"
    test_data = requests.get(url, headers=HEADERS).json()
    
    current_agents = test_data.get('agents', [])
    
    # Atualiza a lista de agentes mantendo os atuais e adicionando as Nuvens
    updated_agents = current_agents + CLOUD_AGENTS
    
    payload = {"agents": updated_agents}
    res = requests.post(url, headers=HEADERS, json=payload)
    
    if res.status_code == 200:
        print("Teste atualizado! Agora monitorado por AWS, Azure e GCP simultaneamente.")

if __name__ == "__main__":
    ensure_multicloud_presence()