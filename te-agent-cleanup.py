import requests
from datetime import datetime, timedelta, timezone

# ==============================================================================
# Script de Housekeeping: Remove Agentes Offline ha mais de 30 dias
# ==============================================================================

TE_API_TOKEN = "SEU_OAUTH_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL_AGENTS = "https://api.thousandeyes.com/v7/endpoint/agents" # Adaptavel para Enterprise

def clean_orphan_agents():
    # Nota: Este e um script logico. Em producao corporativa, recomenda-se 
    # gerar um relatorio antes de disparar os metodos de DELETE.
    try:
        response = requests.get(URL_AGENTS, headers=HEADERS, timeout=15)
        response.raise_for_status()
        agents = response.json().get('agents', [])
        
        removidos = 0
        for agent in agents:
            status = agent.get('state')
            last_seen = agent.get('lastSeen') # Timestamp
            agent_name = agent.get('agentName')
            
            # Lógica simplificada: Se estiver offline, marca para atencao
            if status == "Offline":
                print(f"[ATENCAO] O agente {agent_name} esta offline. Verifique o tempo inativo para delecao.")
                # Aqui entraria a chamada DELETE: requests.delete(f"{URL_AGENTS}/{agent['agentId']}", headers=HEADERS)
                removidos += 1
                
        print(f"Varredura concluida. {removidos} agentes identificados como offline.")

    except Exception as e:
        print(f"Erro na varredura: {e}")

if __name__ == "__main__":
    clean_orphan_agents()