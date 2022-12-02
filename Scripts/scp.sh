#!/bin/bash
module load sshpass/1.06 anaconda3
cd ~/HPC_monitoring/Scripts
c=2
while [ c>1 ]
do
	START_CURRENT_MONTH=$(date "+%Y-%m-01");
	##END_CURRENT_MONTH=$(date "+%Y-%m-%d" -d "$START_CURRENT_MONTH +1 month -1 day");
	squeue -p awhite -o "%A,%u,%j,%M,%l,%D,%C,%N,%b,%m"> /home/mgholiza/HPC_monitoring/CSVs/HPC_data.csv
	sacct -r awhite -a -p --delimiter=',' --format "User,AllocNodes,AllocCPUs,Elapsed" --starttime=$START_CURRENT_MONTH > /home/mgholiza/HPC_monitoring/CSVs/sacct.csv
	##sinfo -p awhite -o "%F,%C" > /home/mgholiza/HPC_monitoring/CSVs/sinfo_data.csv
	python writejson.py && python sacct.py
    	sshpass -p "Whitelabisawesome" scp /home/mgholiza/HPC_monitoring/Media/*.png /home/mgholiza/HPC_monitoring/Json/*.json pi@10.17.0.250:/home/pi/HPC_monitoring/
	sshpass -p "Whitelabisawesome" ssh pi@10.17.0.250 "cd HPC_monitoring && mv *.json ./Json && mv *.png ./Media"
	#sshpass -p "Whitelabisawesome" ssh pi@10.4.12.19 "cd HPC_monitoring && python3 writejson.py && python3 sacct.py "

done
