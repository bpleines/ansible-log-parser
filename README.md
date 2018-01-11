# Ansible Tower Log Parser
_tested on python2.7 & 3.6_

The following script uses python to parse an Ansible Tower log file into successes, failures, and unreachables by hostname. Ansible Tower jobs can run against large inventories and there are times that digging through the Play Recap can be a cumbersome task.  This script is designed to take the human assessment out and quickly return a summary of your job to you on your terminal.

## Usage:
`ansibleLogParser.py -h`
  
```
usage: ansibleLogParser.py [-h] -l LOGFILE [-c CRITERIA]

optional arguments:
  -h, --help            show this help message and exit
  -l LOGFILE, --logfile LOGFILE
                        The log file that you want to parse
  -c CRITERIA, --criteria CRITERIA
                        Whether you want to see "all" output parsed (default)
                        or only the "success", "failure", or "unreachable"
                        output
 ```
 
## Example Usage and Outputs:

### Show all output

`ansibleLogParser.py -l ansibleDiskmapLogTest.txt` 

```
Successes: 6
rhtudhtltapp.prod.redhat.com
rhtudhtltweb.prod.redhat.com
rhtudhtrmapp.prod.redhat.com
rhtudhtrmweb.prod.redhat.com
rhtudhuatapp.prod.redhat.com
rhtudhuatweb.prod.redhat.com

Failures: 4
rhtubtib23.prod.redhat.com
rhtubtib24.prod.redhat.com
rhtubtib25.prod.redhat.com
rhtudeip2.prod.redhat.com

Unreachable: 1
rhtubtib66.prod.redhat.com

```
### Show only success output
`ansibleLogParser.py -l ansibleDiskmapLogTest.txt -c success` 
```
Successes: 6
rhtudhtltapp.prod.redhat.com
rhtudhtltweb.prod.redhat.com
rhtudhtrmapp.prod.redhat.com
rhtudhtrmweb.prod.redhat.com
rhtudhuatapp.prod.redhat.com
rhtudhuatweb.prod.redhat.com
```

### Show only failure output
`ansibleLogParser.py -l ansibleDiskmapLogTest.txt -c failure` 
```
Failures: 4
rhtubtib23.prod.redhat.com
rhtubtib24.prod.redhat.com
rhtubtib25.prod.redhat.com
rhtudeip2.prod.redhat.com
```

### Show only unreachable output
`ansibleLogParser.py -l ansibleDiskmapLogTest.txt -c unreachable` 
```
Unreachable: 1
rhtubtib66.prod.redhat.com
```
