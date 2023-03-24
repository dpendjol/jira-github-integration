import re
import requests
import json

# Get the payload from GitHub
payload = json.loads(request.data)

# Extract the issue key from the branch name
branch_name = payload["ref"]
issue_key = re.search(r"FEAT-\d+", branch_name).group()

# Update the JIRA ticket with the label "merged_to_master"
jira_url = "https://plauti-test.atlassian.net/rest/api/2/issue/" + issue_key
jira_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ATATT3xFfGF0j_3evjSbUrYSVqnkl-ON9F-9Pp6ZxPA-VRkw6tA5Tu_N-xRaH76uWhq6fHa7z_sDFdmSsiMWYXDY3FCPRKvdeFxPaCzDnF9nFHmFVf2W5yUikdTRTG4hYwDbs-Aikql6oIFEh9tdWaxY_rBOogUG4RUu4MEPtBiF6q_SAsxf2nw=CD53472B",
}  # replace <JIRA_API_KEY> with your JIRA API key
jira_payload = {"update": {"labels": [{"add": "merged_to_master"}]}}

response = requests.put(jira_url, headers=jira_headers, json=jira_payload)

# Print the response from JIRA
print(response.json())
