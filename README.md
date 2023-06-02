***
## Description
The purpose of the script is to get a list of VMs without an installed qualys agent.  
The script compares the list of VMs from netbox with the list of VMs from qualys.  
After executing the script, you will get a local json file. Additionally, you can create a jira ticket and attach this file there.  
It does not use password protection, does not describe virtual environments or docker. This is all you do according to your needs.  
***
## Configuration
Parameters for connections and choice of actions are defined in the file settings.ini.  
*Section [choices]*  
Here you decide whether to create separate files from netbox and from qualys. Also here you decide whether to create a jira ticket.  
*Section [qualys]*  
Here you describe connection parameters.  
qualys_filter - qualys filter by which VMs are searched.  
*Section [netbox]*  
Here you describe connection parameters.  
tags_vm_without_agent - a list of tags from the netbox, VMs with these tags are included in the exceptions, they should not have a qualys agent.  
*Section [jira]*  
This section is used if the create_jira_ticket variable is set to yes.  
***
