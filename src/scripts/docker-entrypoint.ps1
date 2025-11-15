$ErrorActionPreference = "Stop"
if (-not $env:PORT) {
    $env:PORT = "3636"
}

if ($env:PURE_FLASK -eq "true") {
    #Write-Host "Starting Flask in development mode on port $env:PORT" &
    python app.py -p $env:PORT
} else {
    if ([string]::IsNullOrEmpty($env:WAITRESS_THREADS)) {
        $cpuCount = (Get-CimInstance Win32_ComputerSystem).NumberOfLogicalProcessors
        $threads = [Math]::Max(4, $cpuCount * 2)
    } else {
        $threads = $env:WAITRESS_THREADS
    }

    #Write-Host "Starting Waitress with $threads threads on port $env:PORT" &
    waitress-serve --host=0.0.0.0 --port=$env:PORT --threads=$threads wsgi:app
}