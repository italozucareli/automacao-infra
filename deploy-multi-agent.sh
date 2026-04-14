#!/bin/bash
# ==============================================================================
# Script de Implantacao Agil de Enterprise Agents Multi-Localidade (Docker)
# ==============================================================================

# Variaveis de Configuracao Corporativa
TOKEN="SEU_TOKEN_AQUI"
MEMORIA="2g"
IMAGEM="thousandeyes/enterprise-agent:latest"

# Menu interativo
echo "============================================="
echo " Instalador Agil - ThousandEyes Enterprise Agent"
echo "============================================="
echo "Selecione o perfil da unidade para este servidor:"
echo "1) Unidade Hospitalar"
echo "2) Unidade Boa Viagem"
echo "3) Escola de Saude"
echo "4) Datacenter Central (Matriz)"
read -p "Opcao: " OPCAO

case $OPCAO in
    1)
        HOSTNAME="TE-Agent-Hospital-01"
        ;;
    2)
        HOSTNAME="TE-Agent-BoaViagem-01"
        ;;
    3)
        HOSTNAME="TE-Agent-EscolaSaude-01"
        ;;
    4)
        HOSTNAME="TE-Agent-Matriz-Core"
        ;;
    *)
        echo "Opcao invalida. Saindo."
        exit 1
        ;;
esac

echo "Iniciando implantacao do agente: $HOSTNAME..."

# Executa a implantacao baseada no perfil escolhido
docker run -d \
  --name "$HOSTNAME" \
  --hostname "$HOSTNAME" \
  --memory "$MEMORIA" \
  --memory-swap "$MEMORIA" \
  --restart always \
  -e TEAGENT_ACCOUNT_TOKEN="$TOKEN" \
  "$IMAGEM"

echo "---------------------------------------------"
echo "Implantacao do agente $HOSTNAME concluida!"
echo "Verifique o status com: docker ps"