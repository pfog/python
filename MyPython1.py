# This is an example submission to test the end-end work flow
# on Grid Optimization Platform
# Author: Dr. Xiaoyuan Fan
# Pacific Northwest National Laboratory
# April 3rd, 2017


# to dump the EMS name in RAS files
import os
import re
import sys
import time

# file path
rawfile1 = sys.argv[1] + '/powersystem.raw'
outputfile = 'solution1.txt'
outputlog = 'log_temp1.txt'
input_solution = sys.argv[1] + '/solution1.txt'

# read the input raw file
def read_from_raw(filepath):
    f = open(filepath, "rb")
    lines = f.readlines()
    f.close()
    return lines

def writefile(linelists, filepath):
##    print linelists
    f = open(filepath, "wb")
    lines = list(linelists)
    for row in lines:
##        print row
##        raw_input('test')
        f.write(str(row))
    f.close()

def exmaplesubmission(timelength):
    time.sleep(timelength)
    print "This prints once every 5 sec."

def processSolution1():

    rawlines = read_from_raw(rawfile1)
    writefile(rawlines,outputlog)

    exmaplesubmission(1)

    solulines = read_from_raw(input_solution)
    print solulines
    writefile(solulines,outputfile)

# main function from here
processSolution1()
print '-'*64
#raw_input('MyPython1 runs completely.')
exit()
