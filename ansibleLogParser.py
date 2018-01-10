from sys import argv
import re

script, logfile = argv

def printSummary():
    hitRecap = False
    successes = []
    failures = []
    unreacheables = []
    with open(logfile, 'r') as log:
        for line in log:
            if 'PLAY RECAP' in line and not hitRecap:
                hitRecap = True
            elif hitRecap:
                nextLine = line[6:]
                hostname, tasks = nextLine.split('[0m', 1)
                if 'unreacheable=1' in tasks:
                    unreacheables.append(hostname)
                elif re.search('failed=[1-9+]', tasks):
                    failures.append(hostname)
                else:
                    successes.append(hostname)
            else:
                pass
       
    print(f"Successes: {len(successes)}")
    for success in successes:
        print(success)
    print(f"\nFailures: {len(failures)}")
    for failure in failures:
        print(failure)
    print(f"\nUnreacheables: {len(unreacheables)}")
    for unreacheable in unreacheables:
        print(unreacheable)

printSummary()
