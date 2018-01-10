from sys import argv
import re

script, logfile, criteria = argv
if not ('all' in criteria or 'success' in criteria or 'failure' in criteria or 'unreacheable' in criteria):
        print("The criteria must be either: all, success, failure, or unreacheable")
        exit(0)

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
                #This should theortically never run
                pass
    
    #The print statements can be commented out to return the list of criteria 
    if 'all' in criteria:
        print(f"Successes: {len(successes)}")
        for success in successes:
            print(success)
        print(f"\nFailures: {len(failures)}")
        for failure in failures:
            print(failure)
        print(f"\nUnreacheables: {len(unreacheables)}")
        for unreacheable in unreacheables:
            print(unreacheable)
        allHostnames = [successes, failures, unreacheables]
        return allHostnames
    elif 'success' in criteria:
        print(f"Successes: {len(successes)}")
        for success in successes:
            print(success)
        return successes
    elif 'failure' in criteria:
        print(f"Failures: {len(failures)}")
        for failure in failures:
            print(failure)
        return failures
    elif 'unreacheable' in criteria:
        print(f"Unreacheables: {len(unreacheables)}")
        for unreacheable in unreacheables:
            print(unreacheable)
        return unreacheables
    else:
        pass

result = printSummary()
