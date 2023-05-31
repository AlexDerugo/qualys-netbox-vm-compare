from configparser import ConfigParser
import os, json

# get the path to the settings.ini file. on the directory below
confif_file_name        = "settings.ini"
config_file_directory   = os.path.dirname(os.getcwd())
config_file             = os.path.join(config_file_directory, confif_file_name)

# read setting.ini
config = ConfigParser()
config.read("settings.ini")

# choices
create_jira_ticket          = config["choices"]["create_jira_ticket"]
create_local_file_vm_netbox = config["choices"]["create_local_file_vm_netbox"]
create_local_file_vm_qualys = config["choices"]["create_local_file_vm_qualys"]

# qualys
qualys_username             = config["qualys"]["qualys_username"]
qualys_password             = config["qualys"]["qualys_password"]
qualys_filter               = config["qualys"]["qualys_filter"]

# netbox
netbox_url                  = config["netbox"]["netbox_url"]
netbox_token                = config["netbox"]["netbox_token"]
# configparser returns strings, but for pynetbox tags must be a list. so we translate str to list
tags_vm_without_agent       = json.loads(config["netbox"]["tags_vm_without_agent"])

# jira
jira_url                    = config["jira"]["jira_url"]
jira_username               = config["jira"]["jira_username"]
jira_passwd                 = config["jira"]["jira_password"]
jira_project_key            = config["jira"]["jira_project_key"]
jira_ticket_summary         = config["jira"]["jira_ticket_summary"]
jira_ticket_description     = config["jira"]["jira_ticket_description"]
jira_ticket_issuetype       = config["jira"]["jira_ticket_issuetype"]
jira_ticket_component       = config["jira"]["jira_ticket_component"]