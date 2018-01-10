<h1>Ansible Tower Log Parser</h1>
<body>
<p>
The following scripts use python3.6 to parse an Ansible Tower log file into successes, failures, and unreachables by hostname. Ansible Tower jobs can run against large inventories and there are times that digging through the Play Recap can be a cumbersome task.
ansibleLogParser.py and ansibleLogParserCriteria.py are designed to take the human assessment out and quickly return a summary of your job to you on your terminal.
</p>
<br>
<p>
Usage:
python3.6 ansibleLogParser.py <logfile>
python3.6 ansibleLogParserCriteria.py <logfile> <[all,success,failure,unreachable]>
</p>
<br>
Examples:
<ul>
<li>python3.6 ansibleLogParser.py ansibleDiskmapLogTest.txt</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt all</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt success</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt failure</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt unreachable</li>
</body>
