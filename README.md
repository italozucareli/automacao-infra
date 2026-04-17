# 👁️ ThousandEyes Advanced Observability & SRE Toolkit

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Core-5391FE.svg?logo=powershell&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Script-4EAA25.svg?logo=gnu-bash&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg?logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC.svg?logo=terraform&logoColor=white)
![Ansible](https://img.shields.io/badge/Ansible-Automation-EE0000.svg?logo=ansible&logoColor=white)

## 📌 About this Repository

This repository is the definitive, Open Source collection of automation, deployment, governance, and integrations for the **Cisco ThousandEyes** platform. 

Featuring **36 advanced scripts**, this toolkit is designed to elevate IT operations maturity, supporting **NOC, SRE (Site Reliability Engineering), SecOps, and FinOps** teams. The core objective is to transform passive monitoring into proactive, integrated observability (Infra as Code, ITSM, and ChatOps).

---

## 📂 Solutions Index

### 1. 🚀 Deployment & Infrastructure (`/01_deploy_and_install`)
Mass automation and lifecycle management for Enterprise and Endpoint Agents.
* `docker-compose.yml` - Standard orchestration for Enterprise Agents in containers.
* `install-te-agent.yml` - Ansible playbook for large-scale Linux agent provisioning.
* `Install-ThousandEyes.bat` - Silent mass installation script via GPO (Windows).
* `te-check.sh` / `te-check.ps1` - Native connectivity, DNS, and NTP pre/post-install validators.
* `update-te-agent.sh` - Secure automated pull/update for Docker images.
* `deploy-multi-agent.sh` - Interactive CLI menu for location-based agent deployment.
* `Uninstall-TEAgentForce.ps1` - Deep uninstaller and registry cleaner for stuck Endpoints.

### 2. 🔗 ITSM & Telemetry Integrations (`/02_observability_itsm`)
Connecting ThousandEyes network data to the enterprise ecosystem.
* `te-to-servicenow.py` - Automated Incident creation and routing in ServiceNow.
* `te-to-pagerduty.py` - Emergency call triggering via PagerDuty Events API.
* `te-to-jira.py` - Automated Bug creation in Jira for agile application degradation.
* `te-to-splunk-hec.py` - Continuous metric streaming to Splunk Enterprise (HTTP Event Collector).
* `te-to-elasticsearch.py` - Test data ingestion for Logstash/Elasticsearch.
* `te-aws-cloudwatch-sync.py` - AWS Lambda Serverless function to sync metrics to CloudWatch.
* `te-grafana-exporter.py` - Metric exporter in Prometheus/Grafana format.
* `te-to-otlp-bridge.py` - Data bridge for the universal OpenTelemetry (OTLP) standard.
* `zabbix-te-discovery.py` - Auto-Discovery (LLD) JSON for automated inventory in Zabbix.
* `te-to-zabbix.py` - Processed data sender to Zabbix via `zabbix_sender`.
* `te-webhook-receiver.py` - Flask microservice to receive Webhooks and create Grafana annotations.

### 3. ⚙️ NOC & Operations Automation (`/03_noc_automation`)
Incident response acceleration and platform management.
* `te-alert-to-teams.py` / `te-to-webex-teams.py` - ChatOps integration for MS Teams and Webex incident routing.
* `te-slack-daily-report.py` - Daily Digest (Daily Performance Summary) generation in Slack.
* `te-maintenance-mode.py` - Pauses and resumes tests during DC maintenance windows.
* `te-zabbix-maintenance-sync.py` - Automated maintenance sync between Zabbix and ThousandEyes.
* `Restart-TEAgentRemote.ps1` - Remote PowerShell restart of failing Endpoint Agent services.
* `te-dynamic-target-update.py` - Dynamic API target updates for Failover/DR scenarios.
* `te-run-now.py` - Instant test trigger outside schedules for Troubleshooting validation.
* `te-apply-webhook-bulk.py` - Bulk association of Webhook integrations across all alert rules.
* `te-dynamic-labeling.py` - Mass addition of labels for logical organization.
* `te-bulk-delete-tests.py` - Mass deletion of obsolete tests based on `.txt` files.
* `te-create-http-test.py` - Automated provisioning of new application tests.
* `te-create-share-link.py` - Public share link generation for ISP escalation.

### 4. 📊 Auditing, Reports & FinOps (`/04_audit_reports_finops`)
Governance, waste reduction, and executive visibility.
* `te-export-inventory.py` - Full active test inventory export to CSV.
* `te-quota-monitor.py` - FinOps control for Unit consumption and projection (Billing).
* `te-backup-configs.py` - DRP (Disaster Recovery) backup of configurations in JSON format.
* `te-agent-cleanup.py` - Housekeeping: Scan for inactive orphan/offline agents.
* `te-agent-capacity.py` - Stress and capacity (CPU/Memory) analyzer for Enterprise VMs.
* `te-generate-statuspage.py` - Static HTML generator for public corporate status pages.
* `check-te-platform-status.py` - Meta-monitoring of ThousandEyes' own public health API.
* `te-top5-latency.py` - Interactive CLI dashboard of Agents with the worst current latencies.

### 5. 🛡️ SecOps, Endpoint & Routing (`/05_secops_routing`)
Advanced Digital Experience Monitoring (DEM), BGP, and Security.
* `te-bgp-hijack-monitor.py` - Route security monitor to detect suspicious ASNs (BGP Hijack).
* `te-ssl-expiry-auditor.py` - Compliance audit for SSL/TLS certificates nearing expiration.
* `te-asn-packet-loss-analyzer.py` - Advanced extractor for packet drops correlated by ASN (ISP).
* `te-asymmetric-routing-alert.py` - Anomaly and asymmetric routing detector in SD-WAN topologies.
* `te-dns-profiler.py` - Performance profiling isolating DNS resolution (Lookup) times.
* `te-endpoint-wifi-audit.py` - Wi-Fi signal quality (BSSID) audit for VIP/Home Office users.
* `te-endpoint-bottlenecks.py` - Detection of user machines with severe local CPU/RAM bottlenecks.
* `te-gateway-bottleneck.py` - Detection of overloaded domestic routers limiting VPN performance.
* `te-endpoint-browser-audit.py` - Security scanner alerting on outdated web browsers.

### 6. 🏢 Multi-Tenant Architecture, Cloud & Synthetics (`/06_advanced_architecture`)
Scripts designed for Managed Service Providers (MSSP) and Infrastructure as Code.
* `te-to-terraform-iac.py` - Reverse Engineering: Converts an existing portal test into `Terraform` (.tf) code.
* `te-endpoint-geojson.py` - Exports agent coordinates for map rendering (GeoJSON) in Grafana.
* `te-sdwan-mesh-generator.py` - Mathematical generator for Full-Mesh (N x N) BGP/Network topologies.
* `te-multicloud-provisioner.py` - Automated injection of global Cloud Agents (AWS/Azure/GCP) into local tests.
* `te-multi-account-billing.py` - FinOps extractor for billing grouped by Sub-accounts (Account Groups).
* `te-transaction-login-template.js` - JavaScript/Puppeteer template for Synthetic Monitoring and Web Logins.

---

## ⚙️ Quick Start Guide

### Python Dependencies
Most automations require Python 3.8+. It is recommended to create a virtual environment (`venv`) and install the following dependencies:

`pip install requests elasticsearch opentelemetry-api opentelemetry-sdk boto3`

Authentication (OAuth Bearer Token)
Scripts interacting with the ThousandEyes RESTful API (v7) require an authentication token.

Log in to the ThousandEyes portal.

Navigate to Account Settings > Users and Roles > Profile.

Under the User API Tokens section, generate an OAuth Bearer Token.

Insert this token into the TE_API_TOKEN (or TE_TOKEN) variable located at the top of the scripts.

Security Best Practice: In production environments, never leave the token hardcoded in the script. Use password vaults, HashiCorp Vault, or OS environment variables (os.environ).

PowerShell Script Execution
If Windows blocks the execution of local `.ps1` scripts due to restrictive execution policies, open PowerShell as an Administrator and run:

powershell
`Set-ExecutionPolicy Bypass -Scope Process -Force`

### ⚖️ Disclaimer
This is an independent repository. The scripts provided here are operational tools made available "as is", without any warranties of any kind.
Always review the source code and perform preliminary tests in a Staging/Non-Prod environment before applying them to your Production infrastructure—especially scripts involving `POST`, `PUT`, or `DELETE` API methods.

## 💡 Developed with the goal of transforming network visibility into continuous business intelligence.