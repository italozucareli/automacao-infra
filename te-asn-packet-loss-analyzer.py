import requests
from collections import defaultdict

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
TEST_ID = "99999" # Teste de rede para analisar

def analyze_loss_by_asn():
    url = f"https://api.thousandeyes.com/v7/net/path-vis/{TEST_ID}"
    res = requests.get(url, headers=HEADERS).json()
    
    # Dicionario para acumular perdas por ASN
    asn_loss = defaultdict(int)
    
    print(f"Buscando gargalos de roteamento BGP no Path Visualization...")
    
    for result in res.get('results', []):
        for hop in result.get('pathTraces', [{}])[0].get('path', []):
            loss = hop.get('loss', 0)
            asn = hop.get('network', 'Desconhecido')
            
            if loss > 0:
                asn_loss[asn] += loss
                
    if not asn_loss:
        print("✅ Nenhuma perda de pacotes associada a provedores externos no momento.")
        return

    print("⚠️ Operadoras (ASNs) derrubando pacotes neste exato momento:")
    for asn, total_loss in sorted(asn_loss.items(), key=lambda item: item[1], reverse=True):
        print(f"- Provedor: {asn} | Ocorrências de Drop: {total_loss}")

if __name__ == "__main__":
    analyze_loss_by_asn()