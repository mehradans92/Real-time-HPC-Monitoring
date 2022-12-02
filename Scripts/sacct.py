import os
import csv
import numpy
import json
import random
import math
from collections import defaultdict
from datetime import datetime
import time
import matplotlib.pyplot as plt
import numpy as np
import urllib
import urllib.request
import matplotlib.font_manager as font_manager

urllib.request.urlretrieve('https://github.com/google/fonts/raw/main/ofl/ibmplexmono/IBMPlexMono-Regular.ttf', 'IBMPlexMono-Regular.ttf')
fe = font_manager.FontEntry(
    fname='IBMPlexMono-Regular.ttf',
    name='plexmono')
font_manager.fontManager.ttflist.append(fe)
plt.rcParams.update({'axes.facecolor':'#f5f4e9', 
            'grid.color' : '#AAAAAA', 
            'axes.edgecolor':'#333333', 
            'figure.facecolor':'#FFFFFF', 
            'axes.grid': False,
            'axes.prop_cycle':   plt.cycler('color', plt.cm.Dark2.colors),
            'font.family': fe.name,
            'figure.figsize': (3.5,3.5 / 1.2),
            'ytick.left': True,
            'xtick.bottom': True   
           })


def get_sec(time_str):
	d=0
	h, m, s = time_str.split(':')
	if len(time_str)>8:
		d, h =h.split('-')
	return int(d)*86400 + int(h) * 3600 + int(m) * 60 + int(s)
csvfile = open('../CSVs/sacct.csv', 'r')
next(csvfile)
jsonfile_total = open('../Json/j_total.json', 'w')
fieldnames = ("User","N_nodes","N_CPUs","Elapsed_time","t_CPUs","t_Nodes")
reader = csv.DictReader(csvfile, fieldnames)
output = []
total_node_hour=0
total_CPU_hour=0
for each in reader:
	row = {}
	if each ['User'] != "":
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
		if each['User'] == "jagwara"	:
			each['User'] = "Jane"
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
		if each['User'] == "kashraf":
			each['User'] = "Kareem"
		if each['User'] == "aroll":
			each['User'] = "Allison"
		if each['User'] == "qcampbe2":
			each['User'] = "Quinny"
		if each['User'] == "mcaldasr":
			each['User'] = "Mayk"
		if each['User'] == "jmedina9":
			each['User'] = "Jorge"
		each['Elapsed_time']= get_sec(each['Elapsed_time'])	
		each['t_CPUs']=float(each['Elapsed_time'])*float(each['N_CPUs'])/3600
		each['t_Nodes']=float(each['Elapsed_time'])*float(each['N_nodes'])/3600
		total_node_hour += each['t_Nodes']
		total_CPU_hour += each['t_CPUs']
		for field in fieldnames:		
			row[field] = each[field]
		output.append(row)
	total_output = defaultdict(float)
	for d in output:
		total_output[d['User']] += float(d['t_CPUs'])
	total_output=[{'User': user, 't_CPUs': cput} for user, cput in total_output.items()]
#total_output=sorted(total_output, key=lambda i : i ['User'])
json.dump(total_output, jsonfile_total)
jsonfile_total.close()
NODES=4
CPU=144
DAYS=30
now = datetime.now()
time0=now.replace(day=1 ,hour=0, minute=0, second=0, microsecond=0)
TIME = (now - time0 ).total_seconds()/3600
CPU_usage=total_CPU_hour/(CPU*TIME)*100
print (CPU_usage)
Node_usage=total_node_hour/(NODES*TIME)*100
jsonfile_monthly_avg = open('../Json/j_monthly_avg.json', 'w')
avg_output={"avg_CPUhour": str(math.ceil(CPU_usage)),"avg_Nodehour" : str(math.ceil(Node_usage))}
json.dump(avg_output, jsonfile_monthly_avg)
jsonfile_monthly_avg.close()
csvfile.close()


with open('../Json/j_total.json') as json_file:
    data = json.load(json_file)
    USERS=[]
    TIME=[]
    for p in data:
        USERS.append(p['User'])
        TIME.append(p['t_CPUs'])
clr = ['#4BC0C0','#961E12','#2d4ab4','#46fb84','#565656','#ff9f40','#680ac6','#c25e5e','#266d3c','#ff6384','#1e31ff']
random.shuffle(clr)
# Ploting Pi-chart
now = datetime.now()
currentMonth=now.strftime('%B')
labels = USERS
sizes = np.array(TIME)
explode = [0]*len(USERS)  # explode 1st slice
explode[0]=0
plt.subplots(figsize=(14,8))
plt.pie(sizes, explode=explode, colors=clr, shadow=False, startangle=140)
percent= 100.*sizes/sizes.sum()
labels = ['{0} : {1:1.2f} %'.format(i,j) for i,j in zip(USERS, percent)]
plt.legend(labels,
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1),fontsize=20)
plt.title('Top Users of ' + currentMonth,fontsize=32,fontweight="bold") 
plt.tight_layout()        
#plt.show()
plt.savefig('../Media/chart_pi.png', dpi = 100)
plt.close()
json_file.close()

## Plotting multiple total cpu-hours per user in case of very frequent users
low_data=[]
high_data=[]
for k,v in enumerate(data):
		if v['t_CPUs']<500:
			low_data.append(data[k])
		else:
			high_data.append(data[k])

## Non-Freqent users
USERS=[]
TIME=[]
for p in low_data:
		USERS.append(p['User'])
		TIME.append(p['t_CPUs'])
plt.subplots(figsize=(14,8))
ax=plt.bar(range(len(low_data)), list(TIME), align='center',color =clr[0:len(clr)],edgecolor='k')
plt.xlim(-1, len(low_data))
plt.xticks(range(len(low_data)), list(USERS),fontsize=17)
plt.yticks(fontsize=20)
plt.ylabel("CPU-hours",fontsize=25)
plt.title('Total HPC Usage in ' + currentMonth,fontsize=32,fontweight="bold")
xlocs, xlabs = plt.xticks()
for i, v in enumerate(low_data):
		## Bar_label_size
		plt.text(xlocs[i]-0.25 , v['t_CPUs'] , str("%0.2f" %v['t_CPUs']),fontsize=18)
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(linestyle='--')
plt.savefig("../Media/chart_bar_low.png", dpi = 100)
#plt.show()
plt.close()

## Freqent users
if len(high_data)==0:
	os.system('rm -rf /home/mgholiza/HPC_monitoring/Media/chart_bar_high.png')
	os.system('sshpass -p "Whitelabisawesome" ssh pi@10.17.0.250 "cd HPC_monitoring && rm -rf ./Media/chart_bar_high.png "')
else:
	USERS=[]
	TIME=[]
	for p in high_data:
			USERS.append(p['User'])
			TIME.append(p['t_CPUs'])
	plt.subplots(figsize=(14,8))
	ax=plt.bar(range(len(high_data)), list(TIME), align='center',color =clr[0:len(clr)],edgecolor='k')
	plt.xlim(-1, len(high_data))
	plt.xticks(range(len(high_data)), list(USERS),fontsize=17)
	plt.yticks(fontsize=20)
	plt.ylabel("CPU-hours",fontsize=25)
	now = datetime.now()
	currentMonth=now.strftime('%B')
	plt.title('Total HPC Usage in ' + currentMonth,fontsize=32,fontweight="bold")
	xlocs, xlabs = plt.xticks()
	for i, v in enumerate(high_data):
			## Bar_label_size
			plt.text(xlocs[i]-0.25 , v['t_CPUs'] , str("%0.2f" %v['t_CPUs']),fontsize=18)
	plt.xticks(rotation=45)
	plt.tight_layout()
	plt.grid(linestyle='--')
	plt.savefig("../Media/chart_bar_high.png", dpi = 100)
	#plt.show()
	plt.close()

	




