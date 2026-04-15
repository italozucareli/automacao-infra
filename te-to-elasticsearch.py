import requests
from elasticsearch import Elasticsearch
from datetime import datetime

# Conexão com o cluster Elastic local ou nuvem
es = Elasticsearch(['http://localhost:9200'])
TE_TOKEN = "SEU_TOKEN"
TEST_ID = "SEU_ID"

def ingest_to_elastic():
    url = f"https://api.thousandeyes.com/v7/net/metrics/{TEST_ID}"
    headers = {"Authorization": f"Bearer {TE_TOKEN}"}
    data = requests.get(url, headers=headers).json().get('results', [])

    for entry in data:
        entry['@timestamp'] = datetime.utcnow().isoformat()
        res = es.index(index="thousandeyes-metrics", document=entry)
        print(f"Documento indexado: {res['result']}")

if __name__ == "__main__":
    ingest_to_elastic()