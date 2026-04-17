# Lógica conceitual avançada
import requests

TE_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_TOKEN}"}
TEST_ID = "112233" 

def check_routing_symmetry():
    url = f"https://api.thousandeyes.com/v7/net/path-vis/{TEST_ID}"
    results = requests.get(url, headers=HEADERS).json().get('results', [])
    
    print("Analisando roteamento...")
    for res in results:
        agent = res.get('agent', {}).get('agentName')
        # Em testes bidirecionais (Agent-to-Agent), a API expõe forward e reverse paths
        forward_path = res.get('pathTraces', [{}])[0].get('path', [])
        reverse_path = res.get('pathTraces', [{}])[1].get('path', []) if len(res.get('pathTraces')) > 1 else []
        
        if len(forward_path) != len(reverse_path):
            print(f"⚠️ Atenção! Roteamento Assimétrico detectado a partir de: {agent}")

if __name__ == "__main__":
    check_routing_symmetry()