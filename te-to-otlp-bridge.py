import time
import requests
from opentelemetry import metrics
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader

# Este script atua como um "braço" que busca métricas de latência e perda de pacotes da API do ThousandEyes e as converte no formato OTLP (OpenTelemetry Protocol), enviando-as para um OTel Collector.
# Aplicação: Ideal para correlacionar uma lentidão no código (Trace) com um gargalo de rede identificado pelo ThousandEyes.#

# Configuração do Provedor de Métricas OTel
exporter = OTLPMetricExporter(endpoint="http://seu-otel-collector:4317", insecure=True)
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader])
metrics.set_meter_provider(provider)
meter = metrics.get_meter("thousandeyes.metrics")

# Métricas OTel
latency_gauge = meter.create_gauge("te.network.latency", unit="ms", description="Latência de rede ThousandEyes")

# Configuração ThousandEyes
TE_API_TOKEN = "SEU_OAUTH_TOKEN"
TEST_ID = "SEU_TEST_ID"
HEADERS = {"Authorization": f"Bearer {TE_API_TOKEN}"}
URL = f"https://api.thousandeyes.com/v7/net/metrics/{TEST_ID}"

def fetch_and_send_to_otel():
    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)
        response.raise_for_status()
        results = response.json().get('results', [])

        for res in results:
            agent = res.get('agent', {}).get('agentName', 'unknown')
            latency = res.get('avgLatency', 0)
            
            # Registra no OpenTelemetry com atributos (labels)
            latency_gauge.set(latency, {"agent_name": agent, "test_id": TEST_ID})
            print(f"Enviado OTel: Agent {agent} -> {latency}ms")

    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    while True:
        fetch_and_send_to_otel()
        time.sleep(60) # Intervalo de 1 minuto