import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = "https://api.thousandeyes.com/v7/agents"

def check_agent_capacity():
    res = requests.get(URL, headers=HEADERS).json().get('agents', [])
    
    print("Analisando Saude dos Enterprise Agents...")
    for agent in res:
        if agent.get('agentType') == 'Enterprise':
            nome = agent.get('agentName')
            utilizacao = agent.get('utilization', 0)
            
            if utilizacao > 80:
                print(f"🔥 ALERTA DE CAPACIDADE: {nome} esta usando {utilizacao}% dos recursos! Adicione vCPU/RAM.")
            else:
                print(f"✅ {nome} operando normalmente ({utilizacao}%).")

if __name__ == "__main__":
    check_agent_capacity()