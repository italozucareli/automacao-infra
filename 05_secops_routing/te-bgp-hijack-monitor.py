import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
TEST_ID = "99999" # ID do teste BGP
URL = f"https://api.thousandeyes.com/v7/net/bgp/metrics/{TEST_ID}"
# Lista de ASNs permitidos (Seu ISP e seus peers diretos)
TRUSTED_ASNS = ["AS12345", "AS67890"] 

def check_bgp_hijack():
    res = requests.get(URL, headers=HEADERS)
    data = res.json().get('results', [])
    
    for route in data:
        path = route.get('asnPath', '')
        # Simplificacao: Verifica se ha ASNs suspeitos no caminho
        for asn in path.split():
            if asn not in TRUSTED_ASNS:
                print(f"⚠️ ALERTA DE SEGURANÇA! ASN suspeito {asn} detectado na rota: {path}")

if __name__ == "__main__":
    check_bgp_hijack()