import pynetbox
from .config_parser import netbox_token, netbox_url, tags_vm_without_agent

# get a list of VMs except for those that have a tag specified in the tags_vm_without_agent variable in the configuration file
def get_vm_from_netbox():
    nb              = pynetbox.api(url=netbox_url, token=netbox_token)
    vm_from_netbox  = []
    response_vm     = nb.virtualization.virtual_machines.filter(tag__n = tags_vm_without_agent)
    for vm in response_vm:
        vm_from_netbox.append(vm.name)
    return vm_from_netbox

list_vm_from_netbox = get_vm_from_netbox()

if __name__ == "__main__":
    # when starting the module, print the list of VMs to the terminal
    print(get_vm_from_netbox())