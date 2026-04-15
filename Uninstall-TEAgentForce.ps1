# Script de Desinstalação Forçada e Limpeza - ThousandEyes Endpoint Agent
Write-Host "Iniciando limpeza profunda do ThousandEyes..." -ForegroundColor Yellow

# 1. Parar serviços e processos
Stop-Process -Name "te-endpoint-agent" -Force -ErrorAction SilentlyContinue
Stop-Service -Name "ThousandEyes Agent" -Force -ErrorAction SilentlyContinue

# 2. Desinstalação via WMI
$app = Get-WmiObject -Class Win32_Product | Where-Object { $_.Name -match "ThousandEyes Endpoint Agent" }
if ($app) {
    Write-Host "Desinstalando pacote MSI..."
    $app.Uninstall() | Out-Null
}

# 3. Limpeza de Pastas Órfãs
$folders = @(
    "C:\Program Files (x86)\ThousandEyes",
    "C:\Program Files\ThousandEyes",
    "C:\ProgramData\ThousandEyes"
)
foreach ($folder in $folders) {
    if (Test-Path $folder) {
        Remove-Item -Path $folder -Recurse -Force -ErrorAction SilentlyContinue
        Write-Host "Pasta removida: $folder"
    }
}

Write-Host "Limpeza concluída. O computador está pronto para uma reinstalação limpa." -ForegroundColor Green