import os
import csv
import numpy
import json 
import math
from collections import defaultdict       
csvfile = open('../CSVs/HPC_data.csv', 'r')
next(csvfile)
jsonfile = open('../Json/j1.json', 'w')
fieldnames = ("Job_ID","User","Job_Name","Run_time","Time_limit","N_Nodes","N_CPU","Node_Name","GRES","MIN_MEMORY")
reader = csv.DictReader(csvfile, fieldnames)		
output = []
for each in reader:
	row = {}
	if each ['User'] == "damirkul":
		each ['User'] = "Dilnoza"
	if each['User'] == "mgholiza":
 		each['User'] = "Mehrad"
	if each['User'] == "awhite38":
		each['User'] = "Andrew"
	if each['User'] == "tsahin"	:
		each['User'] = "Tayfun"
	if each['User'] == "jxu52"	:
		each['User'] = "Jinyu"
	if each['User'] == "mchakra2":
		each['User'] = "Maghesree"
	if each['User'] == "rbarret8":
		each['User'] = "Rainier"
	if each['User'] == "kashraf":
		each['User'] = "Kareem"
	if each['User'] == "zyang43"	:
		each['User'] = "Ziyue"
	if each['User'] == "hgandhi"	:
		each['User'] = "Heta"
	if each['User'] == "gwellawa":
		each['User'] = "Geemi"		
	if each['User'] == "smichtav":
		each['User'] = "Shane"		
	if each['User'] == "oakif":
			each['User'] = "Oion"
	if each ['User'] == "aseshad4":
		each ['User'] = "Aditi"
	if each ['User'] == "ngokul":
		each ['User'] = "Navneeth"
	if each['User'] == "swrig30":
		each['User'] = "Sam"
	if each['User'] == "cmilas":
		each['User'] = "Kat"
	if each['User'] == "wzhu15":
		each['User'] = "Wei"
	if each['User'] == "aroll":
		each['User'] = "Allison"
	if each['User'] == "qcampbe2":
		each['User'] = "Quinny"
	if each['User'] == "mcaldasr":
		each['User'] = "Mayk"
	if each['User'] == "jmedina9":
		each['User'] = "Jorge"
	if each['GRES']== "gpu":
		each['GRES']= 1
	elif each['GRES']== "(null)":
		each['GRES']= 0
	else:
		each['GRES'] = each['GRES'][-1]
	each['MIN_MEMORY']= each['MIN_MEMORY'] + 'B'
	for field in fieldnames:
		row[field] = each[field]
	output.append(row)
total_output = defaultdict(float)
for d in output:
	total_output[d['User']] += float(d['N_CPU'])
total_current_CPU=sum(total_output.values())
CPU=144
current_CPU_usage=total_current_CPU/CPU*100
json.dump(output, jsonfile)    
jsonfile.close()
csvfile.close()
jsonfile = open('../Json/total_current_CPU.json', 'w')
Current_CPU={"Total_current_CPU": math.ceil(current_CPU_usage)}
json.dump(Current_CPU, jsonfile)
jsonfile.close()
# csvfile = open('sinfo_data.csv', 'r')
# next(csvfile)
# jsonfile = open('j2.json', 'w')
# fieldnames = ("Node_usage","CPU_usage")
# reader = csv.DictReader(csvfile, fieldnames)		
# output = []
# for each in reader:
#     row = {}
#     for field in fieldnames:
#         row[field] = each[field]
# N= numpy.array([int(x) for x in row['Node_usage'].split('/')])
# N_A=N[0]
# N_T=N[-1]
# row['Node_usage']=str(int(int(N_A)/int(N_T)*100))
# C= numpy.array([int(x) for x in row['CPU_usage'].split('/')])
# C_A=C[0]
# C_T=C[-1]
# row['CPU_usage']=str(math.ceil(int(C_A)/int(C_T)*100))
# json.dump(row, jsonfile)    
# jsonfile.close()
# csvfile.close()
