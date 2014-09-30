from nltk.corpus import cmudict
#rhyme=dict((k,v) for k,v in proToWord.items() if len(v)>1)
def getWordsGroupedByRhyme(wordToPro=None):
	if wordToPro is None:
		wordToPro=cmudict.dict();
	proToWord=dict()
	for key, value in wordToPro.items():
            for pr in value:
                pronounciation=pr[:]
                pronounciation.reverse()
                p=getUntilStressed(pronounciation)
                if tuple(p) in proToWord and proToWord[tuple(p)] is not None: 
                    proToWord[tuple(p)].append(key)
                else:
                    proToWord[tuple(p)]=[key]
	return proToWord;
def getUntilStressed(pr):
	result=list();
	for p in pr:
		result.append(p)
		if(p[-1]=='1'):
			break;
	return result;
