"""
Author: KC.
Title: Using Regular Expressions To Find IP Addresses.

"""
import re

# This data is from https://bash-prompt.net/guides/using-logs-1/

log_file = """Aug 23 03:47:13 centos7 sshd[3283]: Invalid user guest from 193.201.224.218
Aug 23 03:47:13 centos7 sshd[3283]: input_userauth_request: invalid user guest [preauth]
Aug 23 03:47:13 centos7 sshd[3283]: pam_unix(sshd:auth): check pass; user unknown
Aug 23 03:47:13 centos7 sshd[3283]: pam_unix(sshd:auth): authentication failure; logname= uid=0 euid=0 tty=ssh ruser= rhost=193.201.224.218
Aug 23 03:47:15 centos7 sshd[3283]: Failed password for invalid user guest from 193.201.224.218 port 13181 ssh2
Aug 23 03:47:16 centos7 sshd[3283]: pam_unix(sshd:auth): check pass; user unknown
Aug 23 03:47:17 centos7 sshd[3283]: Failed password for invalid user guest from 193.201.224.218 port 13181 ssh2
Aug 23 03:47:18 centos7 sshd[3283]: pam_unix(sshd:auth): check pass; user unknown
Aug 23 03:47:20 centos7 sshd[3283]: Failed password for invalid user guest from 193.201.224.218 port 13181 ssh2
Aug 23 03:47:24 centos7 sshd[3283]: pam_unix(sshd:auth): check pass; user unknown
Aug 23 03:47:25 centos7 sshd[3283]: Failed password for invalid user guest from 193.201.224.218 port 13181 ssh2
Aug 23 03:47:26 centos7 sshd[3283]: pam_unix(sshd:auth): check pass; user unknown
Aug 23 03:47:27 centos7 sshd[3283]: Failed password for invalid user guest from 193.201.224.218 port 13181 ssh2
Aug 23 03:47:27 centos7 sshd[3283]: pam_unix(sshd:auth): check pass; user unknown
Aug 23 03:47:29 centos7 sshd[3283]: Failed password for invalid user guest from 193.201.224.218 port 13181 ssh2
Aug 23 03:47:29 centos7 sshd[3283]: Disconnecting: Too many authentication failures for guest [preauth]"""

# The pattern works for any IP address of the form xxx.xxx.xxx.xxx. The {1,3} means between 1 and 4 occurrences. The \d macthes with any digits between 0 and 9.
pattern = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# The re.findall is use extract the IP addresses of the form xxx.xxx.xxx.xxx.
valid_ip_addresses = re.findall(pattern, log_file)

# Display result.
print(valid_ip_addresses)
