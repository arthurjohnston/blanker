from nltk.corpus import cmudict
#import imp
#rhyme=imp.load_source('rhyme','C:/Sites/blanker/word/her/rhyme.py')
#from nltk.corpus import cmudict
#cmu=cmudict.dict()
#rhymeToPro,pronunciationToWords=rhyme.getDictionariesNeededForRhyming(cmu)
#realRhymes=dict((k,v) for k,v in rhymeToPro.items() if len(v)>1)
#rgs=[rhyme.rhymeGroup(r,realRhymes,pronunciationToWords,s.syllabify) for r in realRhymes]
#len([g for g in rgs if g.HasOneWord()==False])
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
	def EndsWith(self,shorter,longer):
		if(all(i[0]==i[1] for i in zip(reversed(shorter),reversed(longer)))):
			return True;
		return False;
	def __str__(self):
		string= "rhyme:"+str(self.rhyme)+"\npronunciations:\n"		
		for p in self.proToWords.keys():
			string=string+"\tpronunciation:"+str(p)+"\n"
			string=string+"\t"+str(self.proToSyllables[p])+"\n"
		string+="words:"+str(self.words)
		return string;
#http://www.cs.colorado.edu/~jbg/
#http://www.ling.upenn.edu/phonetics/p2tk/