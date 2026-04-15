# 👁️ ThousandEyes Advanced Observability & SRE Toolkit

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Core-5391FE.svg?logo=powershell&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Script-4EAA25.svg?logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC.svg?logo=terraform&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000.svg?logo=ansible&logoColor=white)

## 📌 Sobre o Repositório

Este repositório é a coleção definitiva e Open Source de automação, implantação, governança e integrações para a plataforma **Cisco ThousandEyes**. 

Contendo **36 scripts avançados**, este toolkit foi desenhado para elevar a maturidade de operações de TI, suportando equipes de **NOC, SRE (Site Reliability Engineering), SecOps e FinOps**. O objetivo central é transformar o monitoramento passivo em observabilidade proativa e integrada (Infra as Code, ITSM e ChatOps).

---

## 📂 Índice de Soluções (Diretórios)

### 1. 🚀 Implantação e Infraestrutura (`/01_deploy_and_install`)
Automação em massa e gerenciamento de ciclo de vida para Enterprise e Endpoint Agents.
* `docker-compose.yml` - Orquestração padrão para Enterprise Agents em contêineres.
* `install-te-agent.yml` - Playbook Ansible para provisionamento de agentes Linux em larga escala.
* `Install-ThousandEyes.bat` - Script de instalação silenciosa em massa via GPO (Windows).
* `te-check.sh` / `te-check.ps1` - Validadores nativos de conectividade, DNS e NTP pré/pós instalação.
* `update-te-agent.sh` - Automação segura de pull/update para imagens Docker.
* `deploy-multi-agent.sh` - Menu interativo (CLI) para implantação de agentes baseada em localidades.
* `Uninstall-TEAgentForce.ps1` - Desinstalador profundo e limpador de registros para Endpoints travados.

### 2. 🔗 Integrações ITSM e Telemetria (`/02_observability_itsm`)
Conectando os dados de rede do ThousandEyes ao ecossistema corporativo.
* `te-to-servicenow.py` - Abertura e endereçamento automático de Incidentes no ServiceNow.
* `te-to-pagerduty.py` - Acionamento de chamadas de emergência via PagerDuty Events API.
* `te-to-jira.py` - Criação automática de Bugs no Jira para degradação de aplicações ágeis.
* `te-to-splunk-hec.py` - Envio contínuo de métricas para o Splunk Enterprise (HTTP Event Collector).
* `te-to-elasticsearch.py` - Ingestão de dados de testes para o Logstash/Elasticsearch.
* `te-aws-cloudwatch-sync.py` - Função AWS Lambda Serverless para sincronizar métricas no CloudWatch.
* `te-grafana-exporter.py` - Exportador de métricas no formato Prometheus/Grafana.
* `te-to-otlp-bridge.py` - Ponte de dados para o padrão universal OpenTelemetry (OTLP).
* `zabbix-te-discovery.py` - Auto-Discovery (LLD) JSON para automação de inventário no Zabbix.
* `te-to-zabbix.py` - Envio de dados processados para o Zabbix via `zabbix_sender`.
* `te-webhook-receiver.py` - Microsserviço Flask para receber Webhooks e criar anotações no Grafana.

### 3. ⚙️ Automação de Operações e NOC (`/03_noc_automation`)
Aceleração de respostas a incidentes e gerenciamento de plataforma.
* `te-alert-to-teams.py` / `te-to-webex-teams.py` - Integração ChatOps com MS Teams e Webex.
* `te-slack-daily-report.py` - Geração de Daily Digest (Resumo de Performance Diário) no Slack.
* `te-maintenance-mode.py` - Pausa e retomada de testes durante janelas de manutenção de DC.
* `te-zabbix-maintenance-sync.py` - Sincronização automática de manutenções entre Zabbix e ThousandEyes.
* `Restart-TEAgentRemote.ps1` - Reinício remoto via PowerShell de serviços Endpoint Agents em falha.
* `te-dynamic-target-update.py` - Atualização dinâmica de alvos via API para cenários de Failover/DR.
* `te-run-now.py` - Disparo instantâneo de testes fora do agendamento para validação de Troubleshooting.
* `te-apply-webhook-bulk.py` - Associação em massa de integrações Webhook em todas as regras de alerta.
* `te-dynamic-labeling.py` - Adição em massa de rótulos (labels) para organização lógica.
* `te-bulk-delete-tests.py` - Exclusão massiva de testes obsoletos baseada em arquivos `.txt`.
* `te-create-http-test.py` - Provisionamento automatizado de novos testes de aplicação.
* `te-create-share-link.py` - Geração de links públicos (Share Links) para envio a ISPs.

### 4. 📊 Auditoria, Relatórios e FinOps (`/04_audit_reports_finops`)
Governança, redução de desperdícios e visibilidade executiva.
* `te-export-inventory.py` - Exportação do inventário completo de testes para CSV.
* `te-quota-monitor.py` - Controle FinOps de consumo e projeção de Units (Billing/Franquia).
* `te-backup-configs.py` - Backup DRP (Disaster Recovery) das configurações em formato JSON.
* `te-agent-cleanup.py` - Housekeeping: Varredura de agentes órfãos/offline inativos.
* `te-agent-capacity.py` - Analisador de stress e capacidade (CPU/Memória) das VMs Enterprise.
* `te-generate-statuspage.py` - Gerador HTML estático para páginas públicas de status corporativo.
* `check-te-platform-status.py` - Meta-monitoramento da API pública de saúde da própria ThousandEyes.
* `te-top5-latency.py` - Dashboard CLI interativo dos Agentes com as piores latências momentâneas.

### 5. 🛡️ SecOps, Endpoint e Roteamento (`/05_secops_routing`)
Monitoramento avançado de usuário final (DEM), BGP e Segurança.
* `te-bgp-hijack-monitor.py` - Monitor de segurança de rotas para detectar ASNs suspeitos (BGP Hijack).
* `te-ssl-expiry-auditor.py` - Auditoria de conformidade de certificados SSL/TLS próximos ao vencimento.
* `te-asn-packet-loss-analyzer.py` - Extrator avançado de quedas de pacotes correlacionadas por ASN (Operadora).
* `te-asymmetric-routing-alert.py` - Detector de anomalias e roteamento assimétrico em topologias SD-WAN.
* `te-dns-profiler.py` - Profiling de performance isolando os tempos de resolução (Lookup) de DNS.
* `te-endpoint-wifi-audit.py` - Auditoria da qualidade de sinal Wi-Fi (BSSID) de usuários VIP/Home Office.
* `te-endpoint-bottlenecks.py` - Detecção de máquinas de usuários com gargalos locais severos de CPU/RAM.
* `te-gateway-bottleneck.py` - Detecção de roteadores domésticos sobrecarregados limitando a VPN.
* `te-endpoint-browser-audit.py` - Scanner de segurança alertando sobre navegadores web desatualizados.

### 6. 🏢 Arquitetura Multi-Tenant, Nuvem e Sintéticos (`/06_advanced_architecture`)
Scripts desenhados para Provedores de Serviços Gerenciados (MSSP) e Infraestrutura como Código.
* `te-to-terraform-iac.py` - Engenharia Reversa: Converte um teste existente no portal em código `Terraform` (.tf).
* `te-endpoint-geojson.py` - Exporta coordenadas de agentes para renderização de mapas (GeoJSON) no Grafana.
* `te-sdwan-mesh-generator.py` - Gerador matemático de topologia BGP/Network em Full-Mesh (N x N).
* `te-multicloud-provisioner.py` - Injeção automática de Cloud Agents globais (AWS/Azure/GCP) em testes locais.
* `te-multi-account-billing.py` - Extrator FinOps de faturamento agrupado por Subcontas (Account Groups).
* `te-transaction-login-template.js` - Template JavaScript/Puppeteer para Monitoramento Sintético e Login Web.

---

## ⚙️ Como Utilizar (Guia Rápido)

### Dependências (Python)
A maioria das automações utiliza Python 3.8+. Recomenda-se criar um ambiente virtual (`venv`) e instalar as dependências:
```bash
pip install requests elasticsearch opentelemetry-api opentelemetry-sdk boto3
Autenticação (OAuth Bearer Token)
Os scripts que interagem com a API Restful da ThousandEyes (v7) exigem um token de autenticação.

Acesse o portal ThousandEyes.

Navegue até Account Settings > Users and Roles > Profile.

Na seção User API Tokens, gere um OAuth Bearer Token.

Insira este token na variável TE_API_TOKEN (ou TE_TOKEN) localizada no cabeçalho dos scripts.

Recomendação de Segurança: Em ambientes de produção, não deixe o token hardcoded no script. Utilize cofres de senhas, HashiCorp Vault ou variáveis de ambiente do SO (os.environ).

Execução de Scripts PowerShell
Caso o Windows bloqueie a execução de scripts .ps1 locais por políticas restritivas, inicie o PowerShell como Administrador e execute:

PowerShell
Set-ExecutionPolicy Bypass -Scope Process -Force

⚖️ Aviso Legal (Disclaimer)
Este é um repositório independente. Os scripts fornecidos aqui são ferramentas operacionais disponibilizadas "as is" (no estado em que se encontram).
Sempre revise o código fonte e execute testes preliminares em um ambiente de Homologação (Non-Prod) antes de aplicar em seu ambiente de Produção — especialmente os scripts que envolvem os métodos POST, PUT ou DELETE na API.

💡 Desenvolvido com o foco em transformar a visibilidade de redes em inteligência de negócios contínua.