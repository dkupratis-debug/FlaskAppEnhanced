param(
    [string]$PythonExe = "",
    [switch]$NoIsolation
)

$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location $repoRoot

function Resolve-Python {
    param([string]$Requested)
    if ($Requested -and (Test-Path $Requested)) {
        return $Requested
    }

    $localAppData = [Environment]::GetFolderPath("LocalApplicationData")
    $candidates = @(
        (Join-Path $localAppData "Programs\Python\Python312\python.exe"),
        (Join-Path $localAppData "Programs\Python\Python313\python.exe")
    )
    foreach ($py in $candidates) {
        if (Test-Path $py) { return $py }
    }

    # Fallback to python launcher if available.
    if (Get-Command py -ErrorAction SilentlyContinue) {
        return "py -3"
    }
    return "python"
}

$py = Resolve-Python -Requested $PythonExe
Write-Host "Using Python: $py"

$args = @("-m", "build")
if ($NoIsolation) { $args += "--no-isolation" }

try {
    if ($py -eq "py -3") {
        & py -3 @args
    } else {
        & $py @args
    }
    Write-Host "Build succeeded."
    exit 0
}
catch {
    Write-Warning "Build failed: $($_.Exception.Message)"
    Write-Host ""
    Write-Host "Possible local policy issue (temp/write restriction)."
    Write-Host "Try these steps:"
    Write-Host "1) Run PowerShell as Administrator."
    Write-Host "2) Allow python.exe in Windows Controlled Folder Access."
    Write-Host "3) Re-run with -NoIsolation:"
    Write-Host "   .\tools\build_local.ps1 -NoIsolation"
    exit 1
}
