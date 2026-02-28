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

    $candidates = @(
        "C:\Users\kupra\AppData\Local\Programs\Python\Python312\python.exe",
        "C:\Users\kupra\AppData\Local\Programs\Python\Python313\python.exe"
    )
    foreach ($py in $candidates) {
        if (Test-Path $py) { return $py }
    }
    return "python"
}

$py = Resolve-Python -Requested $PythonExe
Write-Host "Using Python: $py"

$args = @("-m", "build")
if ($NoIsolation) { $args += "--no-isolation" }

try {
    & $py @args
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
