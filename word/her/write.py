import sys
import os
if (len(sys.argv)>1):
    fileName=sys.argv[1]
else:
    fileName='x'

f=open(fileName,'r')

lines=f.readlines()
f.close()
choice=''
start=True
for l in lines:
    if choice is not 'x':
        choice=raw_input(l)
        f=open(choice,'a')
    
    else:
        if start:
            f=open(choice,'w')
            start=False
        else:
            f=open(choice,'a')
            
    f.write(l)
    f.close()

