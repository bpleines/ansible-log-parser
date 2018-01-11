<h1>Ansible Tower Log Parser</h1>
<body>
<i>tested on python2.7&3.6</i>
<br>
<p>
The following scripts use python to parse an Ansible Tower log file into successes, failures, and unreachables by hostname. Ansible Tower jobs can run against large inventories and there are times that digging through the Play Recap can be a cumbersome task.
ansibleLogParser.py and ansibleLogParserCriteria.py are designed to take the human assessment out and quickly return a summary of your job to you on your terminal.
</p>
<br>
Usage:
<ul>
<li>python3.6 ansibleLogParser.py <logfile></li>
<li>python3.6 ansibleLogParserCriteria.py <logfile> <[all,success,failure,unreachable]></li>
</ul>
<br>
Examples:
<ul>
<li>python3.6 ansibleLogParser.py ansibleDiskmapLogTest.txt</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt all</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt success</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt failure</li>
<li>python3.6 ansibleLogParserCriteria.py ansibleDiskmapLogTest.txt unreachable</li>
</body>
