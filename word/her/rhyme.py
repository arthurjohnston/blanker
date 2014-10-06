from nltk.corpus import cmudict
#pro is pronunciation
#import imp
#rhyme=imp.load_source('rhyme','C:/Sites/blanker/word/her/rhyme.py')
#from nltk.corpus import cmudict
#cmu=cmudict.dict()
#rhymeToPro,pronunciationToWord=rhyme.getDictionariesNeededForRhyming(cmu)
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
		print('rhyme group'+str(rhymeGroup[::-1])) #reversed to make it easier to read
		for pro in rhymeToPros[rhymeGroup]:
			if(any (x[0]!=x[1] for x in tuple(zip(pro,rPro)))): #non identity
				print('  '+str(proToWords[pro]))
			else:
				print('identity words '+str(proToWords[pro]))

class rhymeGroup:
	def __init__(self,rhyme,rhymeToPros,proToWords):
		self.rhyme=rhyme
		self.proToWords=dict()
		for pro in rhymeToPros[rhyme]:
			self.proToWords[pro]=proToWords[pro]

