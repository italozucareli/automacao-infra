@echo off
REM --- Script de Instalação Silenciosa do ThousandEyes Endpoint Agent ---

REM Verifica se o agente já está instalado para não instalar duas vezes
IF EXIST "C:\Program Files (x86)\ThousandEyes\Endpoint Agent\te-endpoint-agent.exe" GOTO FIM
IF EXIST "C:\Program Files\ThousandEyes\Endpoint Agent\te-endpoint-agent.exe" GOTO FIM

REM Comando de instalação silenciosa
msiexec.exe /i "\\NOME-DO-SERVIDOR\DeployTE$\nome-do-arquivo-baixado.msi" ACCOUNT_TOKEN="COLE_O_SEU_TOKEN_AQUI" /qn /norestart

:FIM
exit