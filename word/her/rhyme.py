import itertools;

def getUntilStressed(pr):
	rev=pr[:];
	rev.reverse();
	result=list();
	for p in rev:
		result.append(p)
		if(p[-1]=='1'):
			break;
	return result;
