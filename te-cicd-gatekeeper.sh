#!/bin/bash
# Validador de Deploy via ThousandEyes (Shell Script para CI/CD)

TE_TOKEN="SEU_TOKEN"
TEST_ID="12345" # Teste focado no site que acabou de ser atualizado

echo "Aguardando 2 minutos para o ThousandEyes coletar metricas pos-deploy..."
sleep 120

echo "Verificando alertas ativos no teste $TEST_ID..."
RESPONSE=$(curl -s -H "Authorization: Bearer $TE_TOKEN" "https://api.thousandeyes.com/v7/alerts?state=ACTIVE")

# Verifica se o TEST_ID aparece no JSON retornado
if echo "$RESPONSE" | grep -q "\"testId\": $TEST_ID"; then
    echo "❌ FALHA NO DEPLOY! O ThousandEyes detectou anomalias na aplicacao pos-atualizacao."
    echo "Revertendo (Rollback) recomendado."
    exit 1 # Falha o pipeline
else
    echo "✅ DEPLOY VALIDADO! Nenhum alerta detectado pelo ThousandEyes."
    exit 0 # Aprova o pipeline
fi