Write-Output "---------------------------------------HARVEG---------------------------------------" 
$KeepLogsFor = 15
$VerbosePreference = "Continue"
$LogPath = Split-Path $MyInvocation.MyCommand.Path
Get-ChildItem "$LogPath\*.log" | Where LastWriteTime -LT (Get-Date).AddDays(–$KeepLogsFor) | Remove-Item –Confirm:$false
$LogPathName = Join-Path –Path $LogPath –ChildPath "$($MyInvocation.MyCommand.Name)-$(Get-Date –Format 'MM-dd-yyyy').log"
Start-Transcript $LogPathName –Append
cd C://Harveg/scripts
py hiag_watchdog_win
"------------------------------------------------------------------------" | Out-Default
Stop-Transcript
