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
				pronunciation=tuple(pronunciation)
				p=getUntilStressed(pronunciation)
				#if p==pronunciation: #skip the base cases because those don't count as rhymes
				#	pass
				#belief and leaf??
				if p in rhymeToPro and rhymeToPro[p] is not None: 
					rhymeToPro[p].add(pronunciation)
				else:
					rhymeToPro[p]={pronunciation}

				if pronunciation in pronunciationToWord and pronunciationToWord[pronunciation] is not None:
					pronunciationToWord[pronunciation].append(key)
				else:
					pronunciationToWord[pronunciation]=[key]
	return rhymeToPro,pronunciationToWord;

def getUntilStressed(phonemes):
	result=list();
	for p in phonemes:
		result.append(p)
		if(p[-1]=='1'):
			break;
	return tuple(result);


def printRhymingWords(word,wordToPros,proToWords,rhymeToPros,identity=True):
	print('The word is '+word)
	pros=wordToPros[word]
	for pro in pros:
		rPro=pro[:]
		rPro.reverse()
		rhymeGroup=getUntilStressed(rPro)
		print('rhyme group'+str(rhymeGroup[::-1]))
		for pro in rhymeToPros[rhymeGroup]:

			print('  '+str(proToWords[pro]))