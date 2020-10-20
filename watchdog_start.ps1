Write-Output "---------------------------------------HARVEG---------------------------------------" 
$KeepLogsFor = 15
$VerbosePreference = "Continue"
$LogPath = Split-Path $MyInvocation.MyCommand.Path
Get-ChildItem "$LogPath\*.log" | Where LastWriteTime -LT (Get-Date).AddDays(–$KeepLogsFor) | Remove-Item –Confirm:$false
$LogPathName = Join-Path –Path $LogPath –ChildPath "$($MyInvocation.MyCommand.Name)-$(Get-Date –Format 'MM-dd-yyyy').log"
Start-Transcript $LogPathName –Append
"------------------------------------------------------------------------" | Out-Default
Stop-Transcript
cd C://Harveg/scripts
py -u hiag_watchdog_win | % ToString | Tee-Object $LogPathName

