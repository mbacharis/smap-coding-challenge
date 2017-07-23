# -*- coding: utf-8 -*-
from consumption.models import User,Summary
import os,sys
from django.utils.dateparse import parse_datetime
import pytz
#loads the data for the models
#to run:
# $python manage.py shell
# >>>execfile("../load.py")

#for getting the current path
dirpath = os.path.dirname(os.path.abspath(os.path.dirname(sys.argv[0])))
#load user_data.csv
filename1=os.path.join(dirpath,'data','user_data.csv')
f1=open(filename1,'r')
#skip the header
f1.readline()
#for the summary analysis
Stime=[]
Sconsumption=[]
#error log
errorReport=[]
counter1=0
for i in f1:
    print counter1 #progress monitor
	#parsing user_data.csv data
    data=i.strip().split(',')
    #loading data to User model	
    currentuser=User(user_id=int(data[0]),user_area=data[1],user_tariff=data[2])
    currentuser.save()
	#load corresponding consumption file
    targetfile=data[0]+'.csv'
    filename2=os.path.join(dirpath,'data','consumption',targetfile)
    f2=open(filename2)
    f2.readline()
    counter2=0
    for j in f2:
	    #parse consumption data
        cdata=j.strip().split(',')
		#convert to timezone aware date and times
        naive = parse_datetime(cdata[0])
        time=pytz.timezone("UTC").localize(naive, is_dst=None)
		#load consumption data
        currentuser.energyuse_set.create(EnergyUse_time=time,EnergyUse_consumption=float(cdata[1]))
		#load the first set of data to the summary lists
        if counter1==0:
            Stime.append(time)
            Sconsumption.append(float(cdata[1]))
        else:
			#process the rest of the data
			#make sure that data for the correct timestamp are added
            if Stime[counter2]==time:
                Sconsumption[counter2]=Sconsumption[counter2]+float(cdata[1])
                counter2=counter2+1
            else:
				#there are some additional elements in some of the files
				#same timestamp repeated twice.
				#These second instances are 
				#saved here and produce an error
				#report see line:76-81
                errorMessage=i.strip()+","+j.strip()+","+str(counter2+2)
                errorReport.append(errorMessage)
                counter2=counter2+2
    counter1=counter1+1 
    f2.close()
    #for testing the system remove at deployment
    if counter1==4:
        break     
    
f1.close()
#load summary model
for i in range(len(Stime)):
    currentSummary=Summary(summary_time=Stime[i],summary_use=Sconsumption[i])
    currentSummary.save()
#create error report
filename3=os.path.join(dirpath,'error_report.csv')
f3=open(filename3,'w')
f3.write('id,area,tariff,datetime,consumption,file line\n')
for i in errorReport:
    f3.write(i+'\n')
f3.close()




