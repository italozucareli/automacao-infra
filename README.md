README.md





##########################################################################################################################
te-to-otlp-bridge.py

O OpenTelemetry é o padrão atual para rastreamento distribuído. Este script atua como um "braço" que busca métricas de latência e perda de pacotes da API do ThousandEyes e as converte no formato OTLP (OpenTelemetry Protocol), enviando-as para um OTel Collector.

Aplicação: Ideal para correlacionar uma lentidão no código (Trace) com um gargalo de rede identificado pelo ThousandEyes.
##########################################################################################################################





######################################################################################################################
zabbix-te-discovery.py

Em vez de cadastrar manualmente cada teste no Zabbix, este script faz o LLD. Ele varre sua conta do ThousandEyes e entrega um JSON formatado para que o Zabbix crie automaticamente um "Item" e uma "Trigger" para cada teste ativo.

Aplicação: Automação completa de monitoramento. Se você criar um novo teste no portal ThousandEyes, ele aparece no Zabbix automaticamente.
######################################################################################################################





######################################################################################################################
te-webhook-receiver.py

O ThousandEyes pode enviar Webhooks quando um alerta dispara. Este script é um microserviço (Flask) que recebe o Webhook do ThousandEyes, limpa os dados e os envia para o Grafana OnCall ou cria uma anotação no gráfico do Grafana para marcar exatamente quando o problema começou.

Aplicação: Marcar no gráfico do Grafana o exato momento em que um link de fibra rompeu ou um ISP começou a perder pacotes.
######################################################################################################################



######################################################################################################################
deploy-multi-agent.sh

Automação de Instalação Múltipla via Docker (Para Várias Unidades)

Se você precisa implantar agentes em múltiplas unidades físicas ou em diferentes VLANs utilizando containers, este script em Bash facilita a vida. Você define as variáveis de ambiente logo no início e ele cria o comando longo do Docker automaticamente.
######################################################################################################################




######################################################################################################################
te-grafana-exporter.py

Exportador de Métricas para Grafana (Formato Prometheus)

Se você cria dashboards avançados, o Grafana é a ferramenta ideal. O script abaixo consome a API de testes de rede do ThousandEyes (latência, perda de pacotes e jitter) e converte esses dados para um arquivo de texto no formato do Prometheus (Textfile Collector), permitindo a criação de gráficos customizados.
######################################################################################################################




######################################################################################################################
te-to-zabbix.py

Este script em Python busca os alertas do ThousandEyes e os envia diretamente para o servidor Zabbix local usando o utilitário zabbix_sender.

Pré-requisitos: Ter o zabbix-sender instalado no servidor Linux que vai rodar o script.
######################################################################################################################





######################################################################################################################
get-te-alerts.py

O ThousandEyes não precisa viver isolado. É muito comum puxar os dados dele para alimentar dashboards no Grafana ou gerar gatilhos no Zabbix. O script abaixo usa a API v7 oficial para listar os alertas ativos no momento.

Pré-requisito: Você precisará gerar um OAuth Bearer Token no portal do ThousandEyes (em Account Settings > Users and Roles > Profile).
######################################################################################################################






######################################################################################################################
update-te-agent.sh

A melhor prática é ter um script que faça o processo de baixar a imagem mais recente e recriar o contêiner de forma limpa, sem precisar digitar os comandos do Docker toda vez.
######################################################################################################################




######################################################################################################################