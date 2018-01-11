import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--logfile', required=True, help='The log file that you want to parse')
parser.add_argument('-c', '--criteria', default='all', help='Whether you want to see "all" output parsed (default) or only the "success", "failure", or "unreachable" output')
args = parser.parse_args()

if args.criteria not in ['all','success','failure','unreachable']:
        print("The --criteria or -c option must be one of: all, success, failure, or unreachable")
        exit(0)

def printSummary():
    hitRecap = False
    successes = []
    failures = []
    unreachables = []
    with open(args.logfile, 'r') as log:
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
    if 'all' in args.criteria:
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
    elif 'success' in args.criteria:
        print("Successes: " + str(len(successes)))
        for success in successes:
            print(success)
        return successes
    elif 'failure' in args.criteria:
        print("\nFailures: " + str(len(failures)))
        for failure in failures:
            print(failure)
        return failures
    elif 'unreachable' in args.criteria:
        print("\nUnreachable: " + str(len(unreachables)))
        for unreachable in unreachables:
            print(unreachable)
        return unreachables
    else:
        pass

result = printSummary()
