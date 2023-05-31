from jira import JIRA
import urllib3
from .config_parser import jira_url, jira_passwd, jira_username, jira_project_key, jira_ticket_summary, jira_ticket_description, jira_ticket_issuetype, jira_ticket_component

# turn off certificate verification so that you can connect to Jira
urllib3.disable_warnings()

# jira connect
jira_options = {"server": jira_url, "verify": False}
jira = JIRA(options=jira_options, basic_auth=(jira_username, jira_passwd))


def jira_ticket(file_for_attach):
    issue_dict = {
    "project"       : {"key": jira_project_key},
    "summary"       : jira_ticket_summary,
    "description"   : jira_ticket_description,
    "issuetype"     : {"name": jira_ticket_issuetype},
    "components"    : [{"name": jira_ticket_component}]
    }
    new_ticket      = jira.create_issue(fields=issue_dict)
    jira.add_attachment(issue=new_ticket, attachment=file_for_attach)

if __name__ == "__main__":
    print("module don`t work alone")