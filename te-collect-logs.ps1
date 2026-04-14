# Script de Coleta de Logs do ThousandEyes Endpoint Agent
$LogPath = "C:\ProgramData\ThousandEyes\Endpoint Agent\Logs"
$DesktopPath = [Environment]::GetFolderPath("Desktop")
$ZipFile = "$DesktopPath\ThousandEyes_Logs_$(Get-Date -f 'yyyyMMdd_HHmm').zip"

Write-Host "Coletando logs do ThousandEyes..." -ForegroundColor Cyan
if (Test-Path $LogPath) {
    Compress-Archive -Path "$LogPath\*" -DestinationPath $ZipFile -Force
    Write-Host "Logs salvos com sucesso na Area de Trabalho: $ZipFile" -ForegroundColor Green
} else {
    Write-Host "Pasta de logs nao encontrada. O agente esta instalado?" -ForegroundColor Red
}