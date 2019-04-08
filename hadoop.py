import os
import subprocess
import all
import numpy as np

#slave_ip=[]
#TaskTracker_ip=[]
#client_ip=[]

#cofiguring master
master_ip = input("Enter ip to configure master ...")
all.install_java()
all.install_hadoop()	
all.conf_master(master_ip)
all.disable_firewall(master_ip)



#configuring slaves and task trackers.
slave_task_no = input ("Enter number of slave and tasktrackers you want to configure ...")
i=1
while (i <= int(slave_task_no)):
	slave_task_ip = (int(input("Enter ip of slave / tasktracker {} : ".format(i))))
	all.install_java()
	all.install_hadoop()	
	all.conf_slave_task(slave_task_ip)
	all.disable_firewall(slave_task_ip)	
	i=i+1





#configuring clients.
client_no = input ("Enter number of client you want to configure ...")
i=1
while (i <= int(client_no)):
	client_ip = (int(input("Enter ip of client {} : ".format(i))))
	all.install_java()
	all.install_hadoop()		
	all.conf_client(client_ip)	
	all.disable_firewall(client_ip)	
	i=i+1


#configuring job tracker.
job_tracker_ip = ("enter the ip of job tracker")
all.install_java()
all.install_hadoop()	
all.conf_job_tracker(job_tracker_ip)
all.disable_firewall(job_tracker_ip)




	
