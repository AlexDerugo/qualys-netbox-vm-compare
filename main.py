from modules.config_parser import create_jira_ticket, create_local_file_vm_netbox, create_local_file_vm_qualys
from modules.netbox import list_vm_from_netbox
from modules.qualys import list_vm_from_qualys
from modules.jira_create_ticket import jira_ticket
import json, os

file_name_vm_no_agent       = "vm_no_agent.json"
file_name_vm_from_netbox    = "vm_from_netbox.json"
file_name_vm_from_qualys    = "vm_from_qualys.json"
# compare the list of VMs from netbox and from qualys. We get a list of VMs that are in netbox and are not available as an asset in qualys (most likely they do not have qualys agent)
list_vm_no_agent            = list(set(list_vm_from_netbox) - set(list_vm_from_qualys))

def delete_local_json_files():
    current_directory = os.getcwd()
    for file in os.scandir(current_directory):
        if file.name.endswith(".json"):
            os.unlink(file.path)

def create_file_vm_no_agent():   
    json_obj = json.dumps(list_vm_no_agent, indent = 2)
    with open(file_name_vm_no_agent, "w") as f:
        f.write(json_obj)

def create_file_vm_from_netbox():
    json_obj = json.dumps(list_vm_from_netbox, indent = 2)
    with open(file_name_vm_from_netbox, "w") as f:
        f.write(json_obj)

def create_file_vm_from_qualys():
    json_obj = json.dumps(list_vm_from_qualys, indent = 2)
    with open(file_name_vm_from_qualys, "w") as f:
        f.write(json_obj)

def main():
    # before executing the script, delete all json files from the directory
    try:
        delete_local_json_files()
    except:
        print("unable to delete local json files")
    
    # create a local file with VM without qualys agent
    create_file_vm_no_agent()

    # check the values in the settings.ini file and perform actions according to the specified parameters
    try:
        # create a local file with a list of VMs from netbox
        if create_local_file_vm_netbox == "yes":
            create_file_vm_from_netbox()
        elif create_local_file_vm_netbox == "no":
            None
        # create a local file with a list of VMs from qualys
        if create_local_file_vm_qualys == "yes":
            create_file_vm_from_qualys()
        elif create_local_file_vm_qualys == "no":
            None
        # create a ticket in Jira and attach a file with a list of VMs without an agent
        if create_jira_ticket == "yes":
            jira_ticket(file_name_vm_no_agent)
        elif create_jira_ticket == "no":
            None
    except:
        print("check settings.ini file")

if __name__ == "__main__":
    main()
