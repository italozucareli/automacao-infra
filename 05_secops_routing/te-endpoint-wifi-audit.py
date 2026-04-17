import requests

# ==============================================================================
# Script de Auditoria DEM: Qualidade de Wi-Fi dos Endpoint Agents (Home Office)
# ==============================================================================

TE_API_TOKEN = "SEU_OAUTH_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL_NETWORK_TOPOLOGY = "https://api.thousandeyes.com/v7/endpoint/network/topology"

def audit_home_office_wifi():
    try:
        # Busca dados de rede dos endpoints
        response = requests.get(URL_NETWORK_TOPOLOGY, headers=HEADERS, timeout=15)
        response.raise_for_status()
        data = response.json().get('networkTopology', [])
        
        print("--- Relatorio de Qualidade Wi-Fi (Endpoint Agents) ---")
        for connection in data:
            agent = connection.get('agentName', 'Desconhecido')
            network_type = connection.get('networkType', '')
            
            # Filtra apenas quem esta conectado no Wi-Fi
            if network_type == "Wireless":
                wifi_info = connection.get('wireless', {})
                ssid = wifi_info.get('ssid', 'Oculto')
                signal_quality = wifi_info.get('signalQuality', 0) # Ex: % de sinal
                
                status = "🟢 BOM" if signal_quality > 70 else "🔴 RUIM (Quedas provaveis)"
                
                print(f"Usuario: {agent} | Rede: {ssid} | Sinal: {signal_quality}% -> {status}")

    except Exception as e:
        print(f"Erro ao auditar o Wi-Fi: {e}")

if __name__ == "__main__":
    audit_home_office_wifi()