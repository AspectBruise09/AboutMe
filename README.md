<!-- # 🔰 Introduction -->
<!-- # 🔰 Introducing -->
<!-- # 🔰 Getting Started -->
# 🔶 Oh-My-Posh 🔶
## 🔹 • Installation
<!-- DownLoad And Run [Oh-My-Posh PowerShell Install.ps1](https://github.com/AspectBruise09/AboutMe/blob/main/Oh-My-Posh%20PowerShell%20Install.ps1) -->
DownLoad [Oh-My-Posh PowerShell Install v2.py](https://github.com/AspectBruise09/AboutMe/blob/main/Oh-My-Posh%20PowerShell%20Install%20v2.py) And Run It By Using `python <path_of_Oh-My-Posh_PowerShell_Install_v2.py>` In PowerShell.
> [!Note]
> [Oh-My-Posh Bash Install.sh](https://github.com/AspectBruise09/AboutMe/blob/main/Oh-My-Posh%20Bash%20Install.sh) And [Oh-My-Posh ZShell Install.zsh](https://github.com/AspectBruise09/AboutMe/blob/main/Oh-My-Posh%20ZShell%20Install.zsh) Are <ins>**Not**</ins> Completed.
## 🔹 • UnInstallation
To Delete And UnInstall [Oh-My-Posh PowerShell Install v2.py](https://github.com/AspectBruise09/AboutMe/blob/main/Oh-My-Posh%20PowerShell%20Install%20v2.py); You Should Use These Commands In PowerShell:

`Remove-Item "$env:USERPROFILE\AppData\Local\Programs\oh-my-posh" -Force -Recurse`.

After That, Delete `oh-my-posh init pwsh --config 'C:\Users\<USER>\<theme>.omp.json' | Invoke-Expression` Line By Using `notepad $PROFILE`.
## 🔹 • Code
```py
import subprocess

theme = input("Enter The Name Of Theme You Want (Note: You Can See All Themes In https://ohmyposh.dev/docs/themes). : --> ")

PowerShell = r"""Set-ExecutionPolicy Bypass -Scope Process -Force; Invoke-Expression ((New-Object System.Net.WebClient).DownloadString('https://ohmyposh.dev/install.ps1'))
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/JanDeDobbeleer/oh-my-posh/main/themes/{theme}.omp.json" -OutFile "$env:USERPROFILE\{theme}.omp.json"
Add-Content -Path $PROFILE -Value "`noh-my-posh init pwsh --config '$env:USERPROFILE\{theme}.omp.json' | Invoke-Expression"
. $PROFILE""".format(theme=theme)

result = subprocess.run(["powershell", "-Command", PowerShell], capture_output=True)

print(result.stdout.decode())
```
## 🔹 • Assets
[^1]

[^1]:
