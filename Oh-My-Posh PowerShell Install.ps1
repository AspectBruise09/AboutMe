Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/1_shell.omp.json" -OutFile "$env:USERPROFILE\1_shell.omp.json"
Add-Content -Path $PROFILE -Value "`noh-my-posh init pwsh --config '$env:USERPROFILE\1_shell.omp.json' | Invoke-Expression"
. $PROFILE
