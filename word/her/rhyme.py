from nltk.corpus import cmudict
#pro is pronunciation

#realRhymes=dict((k,v) for k,v in rhymeToPro.items() if len(v)>1)
def getDictionariesNeededForRhyming(wordToPro=None):
	if wordToPro is None:
		wordToPro=cmudict.dict();
	rhymeToPro=dict()
	pronunciationToWord=dict()
	for key, value in wordToPro.items():
			for pr in value:
				pronunciation=pr[:]
				pronunciation.reverse()
				p=getUntilStressed(pronunciation)
				if p in rhymeToPro and rhymeToPro[p] is not None: 
					rhymeToPro[p].add(tuple(pronunciation))
				else:
					rhymeToPro[p]={tuple(pronunciation)}

				if tuple(pronunciation) in pronunciationToWord and pronunciationToWord[tuple(pronunciation)] is not None:
					pronunciationToWord[tuple(pronunciation)].append(key)
				else:
					pronunciationToWord[tuple(pronunciation)]=[key]
	return rhymeToPro,pronunciationToWord;

def getUntilStressed(phonemes):
	result=list();
	for p in phonemes:
		result.append(p)
		if(p[-1]=='1'):
			break;
	return tuple(result);

def printRhymingWords(word,wordToPros,proToWords,rhymeToPros):
	print('The word is '+word)
	pros=wordToPros[word]
	for pro in pros:
		rPro=pro[:]
		rPro.reverse()
		rhymeGroup=getUntilStressed(rPro)
		print('rhyme group'+str(rhymeGroup))
		for v in rhymeToPros[rhymeGroup]:
			print('  '+str(proToWords[v]))