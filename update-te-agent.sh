#!/bin/bash
# ==============================================================================
# Script de Atualização Segura - ThousandEyes Enterprise Agent (Docker)
# ==============================================================================

echo "Iniciando processo de atualizacao do ThousandEyes Agent..."

# Navega ate o diretorio onde o docker-compose.yml esta salvo
# (Ajuste este caminho para o diretorio correto no servidor)
cd /opt/thousandeyes || exit

echo "1. Baixando a imagem mais recente (Pull)..."
docker-compose pull

echo "2. Recriando o conteiner com a nova imagem..."
# O comando 'up -d' identifica se a imagem mudou, destroi o conteiner velho e sobe o novo
docker-compose up -d

echo "3. Limpando imagens antigas para liberar espaco em disco..."
# Remove apenas imagens que nao estao mais associadas a nenhum conteiner ativo
docker image prune -f

echo "Atualizacao concluida com sucesso!"
docker ps | grep te-agent