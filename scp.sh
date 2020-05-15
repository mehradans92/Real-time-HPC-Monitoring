\#!/bin/bash
module load sshpass/1.06
c=2
while [ c>1 ]
do
	squeue -p awhite -o "%A,%u,%j,%M,%D,%C,%N" > HPC_data.csv
        sshpass -p "Whitelabisawesome" scp HPC_data.csv pi@10.4.3.90:/home/pi/HPC_monitoring
	sshpass -p "Whitelabisawesome" ssh pi@10.4.3.90 "cd HPC_monitoring && python3 writejson.py"
	sleep 30
done
