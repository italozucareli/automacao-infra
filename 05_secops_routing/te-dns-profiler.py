import requests

TE_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_TOKEN}"}
TEST_ID = "112233" # ID de um teste HTTP ou DNS Server

def profile_dns_performance():
    url = f"https://api.thousandeyes.com/v7/net/http/server/metrics/{TEST_ID}"
    results = requests.get(url, headers=HEADERS).json().get('results', [])
    
    print("🔍 Auditoria de Tempo de Resolução DNS (Lookup Time)")
    for res in results:
        agent = res.get('agent', {}).get('agentName')
        dns_time = res.get('dnsTime', 0)
        
        if dns_time > 100:
            print(f"🔴 LENTO - {agent}: {dns_time}ms")
        else:
            print(f"🟢 OK - {agent}: {dns_time}ms")

if __name__ == "__main__":
    profile_dns_performance()