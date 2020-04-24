'''
# Sample code to perform I/O:

name = raw_input()          # Reading input from STDIN
print 'Hi, %s.' % name      # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

import math

tc_count=int(raw_input())
tc_inputs=[]
for i in range(tc_count):
    tc_inputs.append([int(i) for i in raw_input().split()])
    

for tc in tc_inputs:
    n=tc[0]
    m=tc[1]
    
    more_pc=True
    if n >= m:
        limiter=m
    else:
        limiter=n
        more_pc=False
        
    p_count=1
    time_count=1
    while p_count*2 <= limiter:
        p_count = p_count*2
        time_count+=1
    
    if not more_pc:
        print(time_count)
    else:
        rem_pc = n - p_count
        time_count += (-rem_pc/m)*-1
        print(time_count)
    

