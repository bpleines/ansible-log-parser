<head>
<h1>Ansible Tower Log Parser</h1>
<body>
The following scripts use python3.6 to parse an Ansible Tower log file into successes, failures, and unreacheables on the host level

Usage:
python3.6 ansibleLogParser.py <logfile>
python3.6 ansibleLogParserCriteria.py <logfile> <[all,success,failure,unrecheable]>

Examples:
python3.6 ansibleLogParser.py ansibleDiskmapLogTest.txt
python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt all
python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt success
python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt failure
python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt unreacheable

