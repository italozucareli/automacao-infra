import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
TEST_ID = "99999" # ID do teste de rede

def get_worst_latency():
    url = f"https://api.thousandeyes.com/v7/net/metrics/{TEST_ID}"
    res = requests.get(url, headers=HEADERS).json()
    
    results = res.get('results', [])
    
    # Ordena a lista de resultados do maior tempo de latencia para o menor
    sorted_results = sorted(results, key=lambda x: x.get('avgLatency', 0), reverse=True)
    
    print("🏆 Top 5 Agentes com Pior Latência no momento:")
    print("-" * 50)
    for idx, item in enumerate(sorted_results[:5], 1):
        agent_name = item.get('agent', {}).get('agentName', 'Desconhecido')
        latency = item.get('avgLatency', 0)
        print(f"{idx}. {agent_name} - {latency} ms")

if __name__ == "__main__":
    get_worst_latency()