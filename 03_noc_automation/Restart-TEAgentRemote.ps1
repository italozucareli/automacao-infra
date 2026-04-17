# Reinicia o serviço do ThousandEyes em um computador remoto da rede
param (
    [Parameter(Mandatory=$true)]
    [string]$ComputerName
)

Write-Host "Tentando comunicar com $ComputerName..." -ForegroundColor Cyan

try {
    Invoke-Command -ComputerName $ComputerName -ScriptBlock {
        Write-Host "Parando serviço ThousandEyes..."
        Stop-Service -Name "ThousandEyes Agent" -Force
        
        Start-Sleep -Seconds 5
        
        Write-Host "Iniciando serviço ThousandEyes..."
        Start-Service -Name "ThousandEyes Agent"
    } -ErrorAction Stop
    
    Write-Host "Serviço reiniciado com sucesso remotamente!" -ForegroundColor Green
} catch {
    Write-Host "Falha ao conectar ou reiniciar o serviço. Verifique se o computador esta ligado e conectado a VPN." -ForegroundColor Red
}