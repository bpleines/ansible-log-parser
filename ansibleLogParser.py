from __future__ import print_function

from sys import argv
import re

script, logfile = argv

def printSummary():
    hitRecap = False
    successes = []
    failures = []
    unreachables = []
    with open(logfile, 'r') as log:
        for line in log:
            if 'PLAY RECAP' in line and not hitRecap:
                hitRecap = True
            elif hitRecap:
                nextLine = line[6:]
                hostname, tasks = nextLine.split('[0m', 1)
                if 'unreachable=1' in tasks:
                    unreachables.append(hostname)
                elif re.search('failed=[1-9+]', tasks):
                    failures.append(hostname)
                else:
                    successes.append(hostname)
            else:
                pass

    #For 2.7 compatibility
    successCount = len(successes)
    failureCount = len(failures)
    unreachableCount = len(unreachables)
       
    #print(f"Successes: {successes}")
    print("Successes: " + str(successCount)) 
    for success in successes:
        print(success)
    #print(f"\nFailures: {len(failures)}")
    print("\nFailures: " + str(failureCount))
    for failure in failures:
        print(failure)
    #print(f"\nUnreacheables: {len(unreachables)}")
    print("\nUnreachable: " + str(unreachableCount))
    for unreachable in unreachables:
        print(unreachable)

printSummary()
