from nltk.corpus import cmudict
#realRhymes=dict((k,v) for k,v in rhymeToPro.items() if len(v)>1)
def getPronounciationGroupedByRhyme(wordToPro=None):
	if wordToPro is None:
		wordToPro=cmudict.dict();
	rhymeToPro=dict()
	pronunciationToWord=dict()
	for key, value in wordToPro.items():
			for pr in value:
				pronunciation=pr[:]
				pronunciation.reverse()
				p=getUntilStressed(pronunciation)
				if tuple(p) in rhymeToPro and rhymeToPro[tuple(p)] is not None: 
					rhymeToPro[tuple(p)].add(tuple(pronunciation))
				else:
					rhymeToPro[tuple(p)]={tuple(pronunciation)}

				if tuple(pronunciation) in pronunciationToWord and pronunciationToWord[tuple(pronunciation)] is not None:
					pronunciationToWord[tuple(pronunciation)].append(key)
				else:
					pronunciationToWord[tuple(pronunciation)]=[key]
	return rhymeToPro,pronunciationToWord;

def getUntilStressed(pr):
	result=list();
	for p in pr:
		result.append(p)
		if(p[-1]=='1'):
			break;
	return result;

