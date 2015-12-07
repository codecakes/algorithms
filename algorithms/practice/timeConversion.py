#!/bin/python
'''
You are given a time in AM/PM format. Can you convert this into a 24-hour format?

Input

Input consists of the time in the AM/PM format i.e. hh:mm:ssAM or hh:mm:ssPM
where 01≤hh≤12.

Sample: 07:05:45PM

Output

You need to print the time in a 24-hour format i.e. hh:mm:ss
where 00≤hh≤23.

Sample output for the above input: 19:05:45

Note: Midnight is 12:00:00AM or 00:00:00. Noon is 12:00:00PM.
'''

import sys


time = raw_input().strip()

hh,mm,ss = time[:-2].split(':')

period = time[-2:]

h = int(hh)
if 0<=h<=23:
    if period == 'PM':
        h = (h+12)%24
    if period=='PM' and h==0:
        h=12
    if period=='AM' and h==12:
        h = 0
    h = str(h).rjust(2,'0')
    print ':'.join([h, mm, ss])
