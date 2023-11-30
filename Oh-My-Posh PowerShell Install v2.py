import subprocess

theme = input("Enter The Name Of Theme You Want (Note: You Can See All Themes In https://ohmyposh.dev/docs/themes). : --> ")

PowerShell = r"""Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/{theme}.omp.json" -OutFile "$env:USERPROFILE\{theme}.omp.json"
Add-Content -Path $PROFILE -Value "`noh-my-posh init pwsh --config '$env:USERPROFILE\{theme}.omp.json' | Invoke-Expression"
. $PROFILE""".format(theme=theme)

result = subprocess.run(["powershell", "-Command", PowerShell], capture_output=True)

print(result.stdout.decode())
