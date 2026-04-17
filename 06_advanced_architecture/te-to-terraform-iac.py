import requests

TE_API_TOKEN = "SEU_TOKEN"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}

def generate_terraform_block(test_id):
    url = f"https://api.thousandeyes.com/v7/tests/http-server/{test_id}"
    res = requests.get(url, headers=HEADERS)
    
    if res.status_code != 200:
        print("Falha ao buscar o teste.")
        return
        
    test = res.json()
    
    # Gera o bloco Terraform (HCL) baseado na API da ThousandEyes
    tf_code = f"""
resource "thousandeyes_http_server" "exportado_{test_id}" {{
  test_name      = "{test.get('testName')}"
  interval       = {test.get('interval')}
  alerts_enabled = {str(test.get('alertsEnabled', 0) == 1).lower()}
  url            = "{test.get('url')}"
  
  # Agentes vinculados
  agents {{
"""
    for agent in test.get('agents', []):
        tf_code += f"    agent_id = {agent.get('agentId')} # {agent.get('agentName')}\n"
    
    tf_code += "  }\n}"
    
    print("📋 Código Terraform Gerado com Sucesso:\n")
    print(tf_code)

if __name__ == "__main__":
    # Substitua pelo ID de um teste existente
    generate_terraform_block("112233")