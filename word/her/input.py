import sys, select

print "You have ten seconds to answer!"

i, o, e = select.select( [sys.stdin], [], [], 3 )

if (i):
  print "You said", sys.stdin.read().strip()
else:
  print "You said nothing!"

import sys
import select

def heardEnter():
    i,o,e = select.select([sys.stdin],[],[],0.0001)
    for s in i:
        if s == sys.stdin:
            input = sys.stdin.readline()
            return True
    return False

