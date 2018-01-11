from sys import argv
import re

script, logfile, criteria = argv
if not ('all' in criteria or 'success' in criteria or 'failure' in criteria or 'unreachable' in criteria):
        print("The criteria must be either: all, success, failure, or unreachable")
        exit(0)

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
                #This should theortically never run
                pass


    #Commented lines are python3 syntax - adjusted to be python2.7 compatible
    #The print statements can be commented out to return the list of criteria 
    if 'all' in criteria:
        #print(f"\nSuccesses: {len(successes)}")
        print("Successes: " + str(len(successes)))
        for success in successes:
            print(success)
        #print(f"\nFailures: {len(failures)}")
        print("\nFailures: " + str(len(failures)))
        for failure in failures:
            print(failure)
        #print(f"\nUnreacheables: {len(unreachables)}")
        print("\nUnreachable: " + str(len(unreachables)))
        for unreachable in unreachables:
            print(unreachable)
        allHostnames = [successes, failures, unreachables]
        return allHostnames
    elif 'success' in criteria:
        print("Successes: " + str(len(successes)))
        for success in successes:
            print(success)
        return successes
    elif 'failure' in criteria:
        print("\nFailures: " + str(len(failures)))
        for failure in failures:
            print(failure)
        return failures
    elif 'unreachable' in criteria:
        print("\nUnreachable: " + str(len(unreachables)))
        for unreachable in unreachables:
            print(unreachable)
        return unreachables
    else:
        pass

result = printSummary()
