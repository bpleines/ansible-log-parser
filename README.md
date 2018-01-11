# Ansible Tower Log Parser
_tested on python2.7 & 3.6_

The following scripts use python to parse an Ansible Tower log file into successes, failures, and unreachables by hostname. Ansible Tower jobs can run against large inventories and there are times that digging through the Play Recap can be a cumbersome task.
ansibleLogParser.py and ansibleLogParserCriteria.py are designed to take the human assessment out and quickly return a summary of your job to you on your terminal.

## Usage:
  * ansibleLogParser.py <logfile\>
  * ansibleLogParserCriteria.py <logfile\> < all | success | failure | unreachable >
  

## Example Usage and Outputs:

`ansibleLogParser.py ansibleDiskmapLogTest.txt`

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

Unreachable: 0

```
`ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt success`
```
Successes: 6
rhtudhtltapp.prod.redhat.com
rhtudhtltweb.prod.redhat.com
rhtudhtrmapp.prod.redhat.com
rhtudhtrmweb.prod.redhat.com
rhtudhuatapp.prod.redhat.com
rhtudhuatweb.prod.redhat.com
```

`ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt failure`
```
Failures: 4
rhtubtib23.prod.redhat.com
rhtubtib24.prod.redhat.com
rhtubtib25.prod.redhat.com
rhtudeip2.prod.redhat.com
```
