import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/endpoint/network/topology"

def audit_local_network():
    res = requests.get(URL, headers=HEADERS).json().get('networkTopology', [])
    
    print("Procurando roteadores locais sobrecarregados...")
    for connection in res:
        agent = connection.get('agentName', 'Unknown')
        gateway_latency = connection.get('localGateway', {}).get('responseTime', 0)
        
        # Se demora mais de 50ms so para chegar no roteador de casa, o Wi-Fi esta ruim
        if gateway_latency > 50:
            print(f"⚠️ {agent} | Latência ate o roteador local: {gateway_latency}ms (Sinal ruim ou roteador travando)")

if __name__ == "__main__":
    audit_local_network()