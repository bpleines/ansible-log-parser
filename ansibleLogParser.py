#!/usr/bin/env python

import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--logfile', required=True, help='The log file that you want to parse')
parser.add_argument('-c', '--criteria', default='all', help='Whether you want to see "all" output parsed (default) or only the "success", "failure", or "unreachable" output')
parser.add_argument('-o', '--output', required=False, help='Specify an output file to store the output')
args = parser.parse_args()

if args.criteria not in ['all','success','failure','unreachable']:
  print("The --criteria or -c option must be one of: all, success, failure, or unreachable")
  exit(1)

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
                #Tower 3.0.3 log compatible
                if '[0m' in line:
                    nextLine = line[6:]
                    hostname, tasks = nextLine.split('[0m', 1)
                #Tower 3.2.3 log compatible
                else:
                    hostname, tasks = line.split(' : ',1)
                if 'unreachable=1' in tasks:
                    unreachables.append(hostname)
                elif re.search('failed=[1-9+]', tasks):
                    failures.append(hostname)
                else:
                    successes.append(hostname)
            else:
                #This should theortically never run
                pass

    #+= syntax chosen for readability - could use join() with a list instead
    output_file_string = ''
    if 'all' in args.criteria:
        output_file_string += "Successes: " + str(len(successes)) + "\n"
        for success in successes:
            output_file_string += success + "\n"
        output_file_string += "\nFailures: " + str(len(failures)) + "\n"
        for failure in failures:
            output_file_string += failure + "\n"
        output_file_string += "\nUnreachables: " + str(len(unreachables)) + "\n"
        for unreachable in unreachables:
            output_file_string += unreachable + "\n"
        finalize(output_file_string)
        allHostnames = [successes, failures, unreachables]
        return allHostnames
    elif 'success' in args.criteria:
        output_file_string += "Successes: " + str(len(successes)) + "\n"
        for success in successes:
            output_file_string += success + "\n"
        finalize(output_file_string)
        return successes
    elif 'failure' in args.criteria:
        output_file_string += "Failures: " + str(len(failures)) + "\n"
        for failure in failures:
            output_file_string += failure + "\n"
        finalize(output_file_string)
        return failures
    elif 'unreachable' in args.criteria:
        output_file_string += "Unreachables: " + str(len(unreachables)) + "\n"
        for unreachable in unreachables:
            output_file_string += unreachable + "\n"
        finalize(output_file_string)
        return unreachables
    else:
        pass

def finalize(output_file_string):
    print(output_file_string)
    if args.output:
        with open(args.output, 'w') as outputFile:
            outputFile.write(output_file_string)

result = printSummary()
