from nltk.corpus import cmudict
from itertools import *
#import imp
#rhyme=imp.load_source('rhyme','C:/Sites/blanker/word/her/rhyme.py')
#from nltk.corpus import cmudict
#cmu=cmudict.dict()
#rhymeToPro,pronunciationToWords=rhyme.getDictionariesNeededForRhyming(cmu)
#realRhymes=dict((k,v) for k,v in rhymeToPro.items() if len(v)>1)
#s=imp.load_source('syllabifier','C:/Sites/blanker/word/her/syllabifier.py')
#rgs=[rhyme.rhymeGroup(r,realRhymes,pronunciationToWords,s.syllabify) for r in realRhymes]
#multi=[r for r in rgs if rhyme.groupHasAtLeastOneDifference(r) and not(r.HasOneWord() or r.HasOnePronunciation())]


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
def sameLastStressed(sy1,sy2):
	'''Checks if the last stressed syllable is the same in 2 syllabifications'''
	return next(x for x in sy2[::-1] if x[0]==1)==next(y for y in sy1[::-1] if y[0]==1)

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def groupHasAtLeastOneDifference(rg):
	return not all(sameLastStressed(pw[0],pw[1])for pw in pairwise(rg.proToSyllables.values()))
class rhymeGroup:
	def __init__(self,rhyme,rhymeToPros,proToWords,syllabification):
		self.rhyme=rhyme
		self.proToWords=dict()
		self.proToSyllables=dict()
		for pro in rhymeToPros[rhyme]:
			realPro=pro[::-1]#proToWords is reversed
			self.proToWords[realPro]=proToWords[pro]
			self.proToSyllables[realPro]=syllabification(realPro)
		self.words=set([w for words in list(self.proToWords.values()) for w in words])
	def HasOneWord(self):
		return len(self.words)==1
	def HasOnePronunciation(self):
	 	return len(self.proToWords.keys())==1
	def __str__(self):
		string= "rhyme:"+str(self.rhyme)+"\npronunciations:\n"		
		for p in self.proToWords.keys():
			string=string+"\tpronunciation:"+str(p)+"\n"
			string=string+"\t"+str(self.proToSyllables[p])+"\n"
		string+="words:"+str(self.words)
		return string;
#http://www.cs.colorado.edu/~jbg/
#http://www.ling.upenn.edu/phonetics/p2tk/