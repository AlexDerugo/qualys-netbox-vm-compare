The script compares the list of VMs from netbox with the list of VMs from qualys.  
Result - VMs without qualys agent in json file.  
Parameters for connections and choice of actions are defined in the file setting.ini.  
You can specify virtual machine tags in netbox for exclusion.  
You can create a jira ticket and attach a file with a list of VMs without an agent there. If you add to cron, then you can make, for example, a monthly report.  
