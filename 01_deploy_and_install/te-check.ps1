# ==============================================================================
# Script de Validação Pós-Instalação - ThousandEyes Enterprise Agent (Windows)
# ==============================================================================

Write-Host "Iniciando Validação do ThousandEyes Enterprise Agent..." -ForegroundColor Cyan
Write-Host "-------------------------------------------------------"

# 1. Checagem do Serviço
Write-Host "1. Status do Serviço 'ThousandEyes Agent': " -NoNewline
$service = Get-Service -Name "ThousandEyes Agent" -ErrorAction SilentlyContinue
if ($service -and $service.Status -eq 'Running') {
    Write-Host "[OK] Rodando" -ForegroundColor Green
} else {
    Write-Host "[FALHA] Serviço não encontrado ou parado" -ForegroundColor Red
}

# 2. Checagem de DNS
Write-Host "2. Resolução de DNS (c1.thousandeyes.com): " -NoNewline
try {
    $dns = Resolve-DnsName "c1.thousandeyes.com" -ErrorAction Stop
    Write-Host "[OK] Resolvido" -ForegroundColor Green
} catch {
    Write-Host "[FALHA] Não foi possível resolver o domínio" -ForegroundColor Red
}

# 3. Conectividade HTTPS (Porta 443)
Write-Host "3. Conectividade HTTPS (Saída Firewall porta 443): " -NoNewline
$tcpCheck = Test-NetConnection -ComputerName "c1.thousandeyes.com" -Port 443 -WarningAction SilentlyContinue
if ($tcpCheck.TcpTestSucceeded) {
    Write-Host "[OK] Conexão TCP 443 estabelecida" -ForegroundColor Green
} else {
    Write-Host "[FALHA] Porta 443 bloqueada" -ForegroundColor Red
}

# 4. Checagem de Tempo (NTP Drift Mínimo)
Write-Host "`n4. Sincronismo de Tempo (Crítico para Autenticação)" -ForegroundColor Cyan
$localTime = (Get-Date).ToUniversalTime().ToString("R")
$serverTime = "Falha ao obter"
try {
    $response = Invoke-WebRequest -Uri "https://c1.thousandeyes.com" -UseBasicParsing -Method Head -TimeoutSec 5
    $serverTime = $response.Headers["Date"]
} catch {
    # Ignora o erro 401/404 da raiz e pega o header de data se possível
    if ($_.Exception.Response) {
        $serverTime = $_.Exception.Response.Headers["Date"]
    }
}

Write-Host "   -> Hora Local do Servidor (UTC): $localTime"
Write-Host "   -> Hora Oficial ThousandEyes   : $serverTime"
Write-Host "* IMPORTANTE: A diferença entre as horas acima não pode ser maior que 2 minutos! *" -ForegroundColor Yellow

Write-Host "`nValidação concluída." -ForegroundColor Cyan