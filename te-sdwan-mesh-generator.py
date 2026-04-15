import requests

TE_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_TOKEN}", "Content-Type": "application/json"}
URL = "https://api.thousandeyes.com/v7/tests/agent-to-agent"

# Lista de IDs dos seus Enterprise Agents nas filiais
AGENT_IDS = [101, 102, 103, 104] 

def create_mesh_tests():
    print("Gerando topologia Full-Mesh SD-WAN...")
    for source in AGENT_IDS:
        for target in AGENT_IDS:
            if source != target:
                test_name = f"Mesh: Agente {source} -> Agente {target}"
                payload = {
                    "testName": test_name,
                    "interval": 300,
                    "direction": "TO_TARGET",
                    "agents": [{"agentId": source}],
                    "targetAgentId": target
                }
                res = requests.post(URL, headers=HEADERS, json=payload)
                if res.status_code == 201:
                    print(f"✅ Criado: {test_name}")
                else:
                    print(f"❌ Falha ao criar: {test_name}")

if __name__ == "__main__":
    create_mesh_tests()