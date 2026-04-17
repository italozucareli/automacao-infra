#!/bin/bash
# ==============================================================================
# Script de Validação Pós-Instalação - ThousandEyes Enterprise Agent (Linux)
# ==============================================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Iniciando Validação do ThousandEyes Enterprise Agent...${NC}\n"

# 1. Checagem do Serviço
echo -n "1. Status do Serviço 'te-agent': "
if systemctl is-active --quiet te-agent; then
    echo -e "${GREEN}[OK] Rodando${NC}"
else
    echo -e "${RED}[FALHA] Serviço não está rodando${NC}"
fi

# 2. Checagem de DNS
echo -n "2. Resolução de DNS (c1.thousandeyes.com): "
if getent hosts c1.thousandeyes.com > /dev/null; then
    echo -e "${GREEN}[OK] Resolvido${NC}"
else
    echo -e "${RED}[FALHA] Não foi possível resolver o domínio${NC}"
fi

# 3. Conectividade HTTPS (Porta 443)
echo -n "3. Conectividade HTTPS (Saída Firewall porta 443): "
HTTP_CODE=$(curl -s -o /dev/null -w "%{http_code}" https://c1.thousandeyes.com || echo "000")
if [ "$HTTP_CODE" -ne "000" ]; then
    echo -e "${GREEN}[OK] Conexão estabelecida (HTTP $HTTP_CODE)${NC}"
else
    echo -e "${RED}[FALHA] Conexão bloqueada ou falhou${NC}"
fi

# 4. Checagem de Tempo (NTP Drift Mínimo)
echo -e "\n${YELLOW}4. Sincronismo de Tempo (Crítico para Autenticação)${NC}"
LOCAL_TIME=$(date -u +"%a, %d %b %Y %H:%M:%S GMT")
SERVER_TIME=$(curl -s --head https://c1.thousandeyes.com | grep -i "^date:" | sed 's/[D|d]ate: //g' | tr -d '\r')

echo "   -> Hora Local do Servidor (UTC): $LOCAL_TIME"
echo "   -> Hora Oficial ThousandEyes   : $SERVER_TIME"
echo -e "${YELLOW}* IMPORTANTE: A diferença entre as horas acima não pode ser maior que 2 minutos! *${NC}\n"

echo -e "${GREEN}Validação concluída.${NC}"