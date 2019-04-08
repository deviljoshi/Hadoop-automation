#!/usr/bin/python36
import os
import subprocess
import numpy as np


#configuring master.
def conf_master(mip):
	os.system("scp /root/Desktop/pythoncode/hadoop/j_m_c_s_corefile.xml {}:/etc/hadoop/core-site.xml".format(mip))
	
	os.system("scp /root/Desktop/pythoncode/hadoop/masterhdfsfile.xml {}:/etc/hadoop/hdfs-site.xml".format(mip))
	os.system("ssh {} mkdir /etc/hadoop/mydata".format(mip))	
	os.system("ssh {} hadoop namenode -format".format(mip))
	os.system("ssh {} hadoop-daemon.sh start namenode".format(mip))




#configuring slaves and task trackers.
def conf_slave_task(stip):
	os.system("scp /root/Desktop/pythoncode/hadoop/j_m_c_s_corefile.xml {}:/etc/hadoop/core-site.xml".format(stip))
	
	os.system("scp /root/Desktop/pythoncode/hadoop/slavehdfsfile.xml {}:/etc/hadoop/hdfs-site.xml".format(stip))
	os.system("scp /root/Desktop/pythoncode/hadoop/j_t_c_mapred.xml {}:/etc/hadoop/mapred-site.xml".format(stip))
	os.system("ssh {} mkdir /etc/hadoop/data".format(mip))
	os.system("ssh {} hadoop-daemon.sh start namenode".format(mip))
		


#configuring client.
def conf_client(cip):
	os.system("scp /root/Desktop/pythoncode/hadoop/j_m_c_s_corefile.xml {}:/etc/hadoop/core-site.xml".format(cip))
	os.system("scp /root/Desktop/pythoncode/hadoop/j_t_c_mapred.xml {}:/etc/hadoop/mapred-site.xml".format(cip))
	


#configuring job tracker.
def conf_job_tracker(jip):
	os.system("scp /root/Desktop/pythoncode/hadoop/j_m_c_s_corefile.xml {}:/etc/hadoop/core-site.xml".format(mip))
	
	os.system("scp /root/Desktop/pythoncode/hadoop/j_t_c_mapred.xml {}:/etc/hadoop/mapred-site.xml".format(jip))	
	
	




#installing Java.
def install_java:
	s = sp.getstatusoutput('java -version')

	if 'HotSpot1' in s[1] :
		print ("java installed")

	else :
		path = input("Give path of your java package...")
		s=sp.getstatusoutput('rpm -ivh {}'.format('path'))
		if 'HotSpot' in s[1] :
			print ("java Successfully installing...")
			echo "export JAVA_HOME=/usr/java/jdk1.8.0_171-amd64/" >> {}/root/.bashrc
			echo "export PATH=/usr/java/jdk1.8.0_171-amd64/bin:$PATH" >> /root/.bashrc
		
			print ("java Successfully installed")
	


#installing Hadoop.
def install_hadoop:
	
	s = sp.getstatusoutput('hadoop version')

	if 'Hadoop' in s[1] :
		print ("Hadoop installed")

	else :
		path = input("Give path of your Hadoop package...")
		s=sp.getstatusoutput('rpm -ivh {} --force'.format('path'))
	    	s = sp.getstatusoutput('hadoop version')
		if 'Hadoop' in s[1] :
			print ("Hadoop installed Successfully ....")

def disable_firewall(ip):
	os.system("ssh {} firewall-cmd  --add-port=0-65535/tcp  --permanent".format(ip))
	os.system("ssh {} firewall-cmd  --add-port=0-65535/udp  --permanent".format(ip))
	 








	
	
	
