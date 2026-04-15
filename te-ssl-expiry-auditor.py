import requests
from datetime import datetime

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}

# Busca todos os testes HTTP
URL_TESTS = "https://api.thousandeyes.com/v7/tests/http-server"

def audit_ssl_certificates():
    tests = requests.get(URL_TESTS, headers=HEADERS).json().get('tests', [])
    
    print("Auditoria de Certificados SSL/TLS")
    print("-" * 50)
    
    for t in tests:
        test_id = t.get('testId')
        # Busca a metrica de SSL do teste especifico
        url_metrics = f"https://api.thousandeyes.com/v7/net/http/server/metrics/{test_id}"
        metrics_res = requests.get(url_metrics, headers=HEADERS)
        
        if metrics_res.status_code == 200:
            results = metrics_res.json().get('results', [])
            if results:
                # Pega o resultado do primeiro agente
                cert_expiry_timestamp = results[0].get('sslCertExpiry')
                
                if cert_expiry_timestamp:
                    expiry_date = datetime.utcfromtimestamp(cert_expiry_timestamp)
                    days_left = (expiry_date - datetime.utcnow()).days
                    
                    if days_left < 30:
                        print(f"ALERTA: {t['testName']} - O certificado expira em {days_left} dias! ({expiry_date.strftime('%Y-%m-%d')})")
                    else:
                        print(f"OK: {t['testName']} - {days_left} dias restantes.")

if __name__ == "__main__":
    audit_ssl_certificates()