import subprocess

fileName = input("Enter The Name Of Theme You Want. (Note:You Can See All Themes In https://ohmyposh.dev/docs/themes) : --> ")

PowerShell = r"""Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/{fileName}.omp.json" -OutFile "$env:USERPROFILE\{fileName}.omp.json"
Add-Content -Path $PROFILE -Value "`noh-my-posh init pwsh --config '$env:USERPROFILE\{fileName}.omp.json' | Invoke-Expression"
. $PROFILE""".format(fileName=fileName)

result = subprocess.run(["powershell", "-Command", PowerShell], capture_output=True)

print(result.stdout.decode())