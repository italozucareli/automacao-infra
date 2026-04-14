import requests
import time

# ==============================================================================
# Script de Extracao de Metricas (Network) para Grafana/Prometheus
# ==============================================================================

TE_API_TOKEN = "SEU_OAUTH_BEARER_TOKEN"
TEST_ID = "123456"  # Substitua pelo ID do Teste de Rede que deseja monitorar
OUTPUT_FILE = "/var/lib/prometheus/node-exporter/thousandeyes.prom"

HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
# Busca os dados da ultima janela de tempo
URL = f"https://api.thousandeyes.com/v7/net/metrics/{TEST_ID}"

def generate_prom_metrics():
    try:
        res = requests.get(URL, headers=HEADERS, timeout=15)
        res.raise_for_status()
        data = res.json()
        
        metrics_output = []
        metrics_output.append("# HELP te_network_loss Packet loss percentage")
        metrics_output.append("# TYPE te_network_loss gauge")
        metrics_output.append("# HELP te_network_latency Average latency in ms")
        metrics_output.append("# TYPE te_network_latency gauge")

        # Itera pelos agentes que executaram este teste
        for result in data.get('results', []):
            agent_name = result.get('agent', {}).get('agentName', 'unknown')
            agent_name = agent_name.replace(" ", "_").replace("-", "_")
            loss = result.get('loss', 0)
            avg_latency = result.get('avgLatency', 0)
            
            # Formata no padrao do Prometheus
            metrics_output.append(f'te_network_loss{{agent="{agent_name}"}} {loss}')
            metrics_output.append(f'te_network_latency{{agent="{agent_name}"}} {avg_latency}')

        # Salva no arquivo que o Prometheus le
        with open(OUTPUT_FILE, 'w') as f:
            f.write("\n".join(metrics_output) + "\n")
            
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Metricas atualizadas com sucesso para o Grafana.")

    except Exception as e:
        print(f"Erro ao exportar metricas: {e}")

if __name__ == "__main__":
    generate_prom_metrics()