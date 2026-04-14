# 👁️ ThousandEyes Automation & Observability Toolkit

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![PowerShell](https://img.shields.io/badge/PowerShell-Core-blue.svg)
![Bash](https://img.shields.io/badge/Bash-Script-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)

## 📌 Sobre o Repositório
Este repositório contém uma coleção de scripts avançados para automação, implantação, observabilidade e governança da plataforma **Cisco ThousandEyes**. Os scripts foram desenvolvidos para apoiar equipes de Infraestrutura, NOC (Network Operations Center), SRE (Site Reliability Engineering) e Helpdesk.

O objetivo deste toolkit é reduzir o esforço manual, garantir conformidade e integrar os dados de rede do ThousandEyes com o ecossistema moderno de TI (ITSM, ChatOps e Ferramentas de Telemetria).

---

## 📂 Estrutura do Repositório

### 1. 🚀 Instalação e Deploy (`/deploy_and_install`)
Scripts focados na implantação em massa e validação de Enterprise e Endpoint Agents.
* `docker-compose.yml` - Orquestração padrão para Enterprise Agents em contêineres.
* `te-check.sh` - Validador de rede e pré-requisitos para agentes Linux (Bash).
* `te-check.ps1` - Validador de rede e pré-requisitos para agentes Windows (PowerShell).
* `Install-ThousandEyes.bat` - Script de instalação silenciosa em massa via GPO.
* `update-te-agent.sh` - Automação segura de pull/update para imagens Docker.
* `deploy-multi-agent.sh` - Menu interativo para implantação rápida de agentes por localidade.

### 2. 🔗 Integrações de Observabilidade e ITSM (`/integrations`)
Conectando o ThousandEyes a ferramentas de mercado e ITSM.
* `te-grafana-exporter.py` - Exportador de métricas de rede no formato Prometheus/Grafana.
* `te-to-zabbix.py` - Envio de alertas de rede para o Zabbix via `zabbix_sender`.
* `zabbix-te-discovery.py` - Auto-Discovery (LLD) de testes do ThousandEyes para Zabbix.
* `te-to-otlp-bridge.py` - Ponte de dados para o padrão OpenTelemetry (OTLP).
* `te-webhook-receiver.py` - Microsserviço Flask para receber webhooks e criar anotações no Grafana.
* `te-to-servicenow.py` - Abertura automática de Incidentes no ServiceNow.
* `te-to-jira.py` - Criação de Bugs no Jira para degradação de aplicações ágeis.

### 3. ⚙️ Automação e NOC (`/automation_noc`)
Scripts para o dia a dia da operação e resposta a incidentes.
* `get-te-alerts.py` - Consulta rápida de alertas ativos via terminal.
* `te-alert-to-teams.py` - Integração ChatOps para envio de incidentes ao MS Teams.
* `te-maintenance-mode.py` - Pausa e retoma testes durante janelas de manutenção.
* `te-bulk-delete-tests.py` - Exclusão em massa de testes obsoletos via arquivo de texto.
* `Restart-TEAgentRemote.ps1` - Reinício remoto e invisível do Endpoint Agent via PowerShell.
* `te-create-http-test.py` - Provisionamento automatizado de novos testes HTTP(S).
* `te-dynamic-target-update.py` - Atualização dinâmica de alvos em cenários de Failover/DR.
* `te-create-share-link.py` - Geração de links de compartilhamento (Share Links) para ISPs.
* `te-cicd-gatekeeper.sh` - Validador de pipelines CI/CD que bloqueia deploys com anomalias de rede.
* `te-dynamic-labeling.py` - Adição em massa de rótulos (labels) para organização de testes.
* `te-run-now.py` - Disparo instantâneo de testes para validação de troubleshooting.

### 4. 📊 Auditoria, Relatórios e FinOps (`/audit_and_reports`)
Governança, redução de custos e relatórios gerenciais.
* `te-export-inventory.py` - Exportação de todo o inventário de testes ativos para arquivo CSV.
* `te-backup-configs.py` - Backup completo das configurações de infraestrutura em formato JSON.
* `te-agent-cleanup.py` - Housekeeping para identificar e remover agentes órfãos/offline.
* `te-endpoint-wifi-audit.py` - Auditoria de qualidade de sinal Wi-Fi para usuários em Home Office (DEM).
* `te-endpoint-bottlenecks.py` - Identificação de gargalos de CPU/Memória nas máquinas dos usuários.
* `te-gateway-bottleneck.py` - Detecção de roteadores locais sobrecarregados.
* `te-collect-logs.ps1` - Coletor e compactador automatizado de logs locais do Endpoint Agent.
* `te-bgp-hijack-monitor.py` - Monitor de segurança para detectar sequestro de ASNs em rotas BGP.
* `te-generate-statuspage.py` - Gerador estático de HTML para páginas públicas de status (Status Page).
* `te-quota-monitor.py` - Controle FinOps de consumo e projeção de Units (billing).
* `check-te-platform-status.py` - Meta-monitoramento para consultar o status da própria API do ThousandEyes.
* `te-top5-latency.py` - Dashboard CLI com o Top 5 Agentes de pior latência no momento.
* `te-agent-capacity.py` - Verificador de capacidade (vCPU/RAM) dos Enterprise Agents.

---

## 🛠️ Como Utilizar (Pré-requisitos)

### Para scripts em Python (`.py`):
1. Recomenda-se o uso do **Python 3.8** ou superior.
2. Instale a biblioteca de requisições web:
   ```bash
   pip install requests
Autenticação: Gere um OAuth Bearer Token no portal do ThousandEyes (Account Settings > Users and Roles > Profile) e insira na variável TE_API_TOKEN no cabeçalho do script desejado.

### Para scripts Shell/Bash (.sh):
Conceda permissão de execução antes de rodar no Linux:

Bash
chmod +x nome-do-script.sh
./nome-do-script.sh

### Para scripts PowerShell (.ps1):
Caso encontre bloqueios de execução no Windows, abra o PowerShell como Administrador e libere a execução temporária:

Set-ExecutionPolicy Bypass -Scope Process

⚠️ Aviso Legal
Estes scripts são fornecidos "como estão" (as-is), sem garantias de qualquer tipo. Sempre revise o código e teste em ambientes de homologação (Non-Prod) antes de aplicar em sua infraestrutura de Produção, especialmente os scripts que realizam exclusões (DELETE) ou alterações em massa.