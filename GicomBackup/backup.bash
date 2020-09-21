#!/bin/bash
if cd sudo mount -t cifs -o username=openhabian //192.168.254.175/Share /etc/ ; then
{
rsync -rt --verbose /mnt/c/HARVEG/Gicomdata/
echo $(date) "Success" >> /mnt/c/Harveg/Backup_Log.txt
}
else
{
  echo $(date) "No Backup drive" >> /mnt/c/Harveg/Backup_Log.txt

}
