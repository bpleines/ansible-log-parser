[![static-code-analysis](https://github.com/bpleines/ansible-log-parser/actions/workflows/static-code-analysis.yaml/badge.svg)](https://github.com/bpleines/ansible-log-parser/actions/workflows/static-code-analysis.yaml)

# Ansible Tower Log Parser

The following script uses python to parse an Ansible Tower log file into successes, failures, and unreachables by hostname. Ansible Tower jobs can run against large inventories and there are times that digging through the Play Recap can be a cumbersome task. This script is designed to remove human assessment and quickly return a summary of a job to the terminal or in an output file.

_tested on Tower v3.0.3 & v3.2.3_

## Usage:
`python ansible_log_parser.py -h`

```
usage: python ansible_log_parser.py [-h] -l LOGFILE [-c CRITERIA] [-o OUTPUT]

optional arguments:
  -h, --help            show this help message and exit
  -l LOGFILE, --logfile LOGFILE
                        The log file that you want to parse
  -c CRITERIA, --criteria CRITERIA
                        Whether you want to see "all" output parsed (default)
                        or only the "success", "failure", or "unreachable"
                        output
  -o OUTPUT, --output OUTPUT
			Additionally direct printed information to an output file
 ```

## Example Usage and Outputs:

### Show all output

`python ansible_log_parser.py -l ansibleDiskmapLogTest.txt`

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
`python ansible_log_parser.py -l ansibleDiskmapLogTest.txt -c success`
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
`python ansible_log_parser.py -l ansibleDiskmapLogTest.txt -c failure`
```
Failures: 4
rhtubtib23.prod.redhat.com
rhtubtib24.prod.redhat.com
rhtubtib25.prod.redhat.com
rhtudeip2.prod.redhat.com
```

### Show only unreachable output
`python ansible_log_parser.py -l ansibleDiskmapLogTest.txt -c unreachable`
```
Unreachable: 1
rhtubtib66.prod.redhat.com
```
