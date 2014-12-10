from nltk.corpus import cmudict
import itertools 
import syllabifier  
#from nltk.corpus import cmudict
#cmu=cmudict.dict()
#rhymeToPro,pronunciationToWords=rhyme.getDictionariesNeededForRhyming(cmu)
#rgs=[rhyme.rhymeGroup(r,rhymeToPro,pronunciationToWords,syllabifier.syllabify) for r in rhymeToPro]
#multi=[r for r in rgs if rhyme.groupHasAtLeastOneDifference(r) and not(r.HasOneWord() or r.HasOnePronunciation())]
#multi=sorted(multi,key= lambda x: len(x.words))

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


def groupHasAtLeastOneDifference(rg):
	return any(SyllabificationsRhyme(pair[0],pair[1])for pair in itertools.combinations(rg.proToSyllables.values(),2))

def SyllabificationsRhyme(syllable1,syllable2): #assumes it's in the same rhymegroup
	seenStressed=False
	for s1,s2 in zip(syllable1[::-1],syllable2[::-1]):
		if(s1[0]==1):#if it is a stressed
			seenStressed=True
		if(seenStressed):
			if s1[1]!=s2[1] and s1[2]==s2[2] and s1[3]==s2[3]:
				return True;
			if s1[1]!=s2[1] or s1[2]!=s2[2] or s1[3]!=s2[3]:
				return False;
	return False
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


def getMulti():
	cmu=cmudict.dict();
	rhymeToPros,pronunciationToWords=getDictionariesNeededForRhyming(cmu);
	print("rhymeToPros has "+str(len(rhymeToPros))+" items")
	print("pronunciationToWords has "+str(len(pronunciationToWords))+" items")
	rgs=[rhymeGroup(r,rhymeToPros,pronunciationToWords,syllabifier.syllabify) for r in rhymeToPros]
	multi=[r for r in rgs if (groupHasAtLeastOneDifference(r) and not(r.HasOneWord() or r.HasOnePronunciation()))]
	print("English has "+ str(len(multi))+" good rhyme groups\n")
	return multi

# If this module was run directly, print the total number of 
# rhyme groups in english
if __name__ == "__main__":
	getMulti()
#tests for checking if 2 syllabifications rhyme
def allTests():
	allTests=[testSyllablesRhyme1(),testSyllablesRhyme2(),
	testSyllablesRhyme3(),testSyllablesRhyme4(),
	testDontRhyme1(),testDontRhyme2(),
	testDontRhyme3(),testDontRhyme4(),
	testDontRhyme5(),testDontRhyme6()]
	return all(x==True for x in allTests)
def testSyllablesRhyme1():
	s1=[(0, ['F', 'R'], ['AH'], []), (1, ['T'], ['ER'], []), (0, ['N'], ['IH'], []), (0, ['T'], ['IY'], [])]
	s2=[(0, ['P'], ['AH'], []), (1, ['T'], ['ER'], []), (0, ['N'], ['IH'], []), (0, ['T'], ['IY'], [])]
	return SyllabificationsRhyme(s1,s2);
def testSyllablesRhyme2():
	s1=[(1, ['M'], ['AA'], []), (0, ['D'], ['AH'], ['S', 'T'])]
	s2=[(1, [], ['AA'], []), (0, ['D'], ['AH'], ['S', 'T'])]
	return SyllabificationsRhyme(s1,s2);
def testSyllablesRhyme3():
	s1= [(1, ['R'], ['AY'], []), (2, ['D'], ['AW'], ['T'])]
	s2=	[(1, ['HH'], ['AY'], []), (2, ['D'], ['AW'], ['T'])]
	return SyllabificationsRhyme(s1,s2);
def testSyllablesRhyme4():
	s1=[(0, [], ['IH'], ['M']), (1, ['P'], ['AE'], []), (0, ['N'], ['AH'], ['L', 'D'])]
	s2=[(0, ['D'], ['IH'], []), (1, ['S', 'M'], ['AE'], []), (0, ['N'], ['AH'], ['L', 'D'])]
	return SyllabificationsRhyme(s1,s2);
def testDontRhyme1():
	s1=[(1, ['S'], ['EH'], ['L', 'F']), (1, ['D'], ['EH'], []), (0, ['P', 'R'], ['AH'], []), (2, ['K'], ['EY'], []), (0, ['T'], ['IH'], ['NG'])]
	s2=[(1, ['D'], ['EH'], []), (0, ['P', 'R'], ['AH'], []), (2, ['K'], ['EY'], []), (0, ['T'], ['IH'], ['NG'])]
	return not SyllabificationsRhyme(s1,s2);
def testDontRhyme2():
	s1=[(0, ['D'], ['IH'], []), (1, ['F'], ['EH'], ['N', 'S'])]
	s2=[(1, ['F'], ['EH'], ['N', 'S'])]
	return not SyllabificationsRhyme(s1,s2);
def testDontRhyme3():
	s1=[(2, ['M'], ['AA'], []), (0, ['N'], ['AH'], []), (1, ['S'], ['AE'], []), (0, ['K'], ['ER'], []), (2, [], ['AY'], ['D'])]
	s2=[(2, ['P'], ['AA'], []), (0, ['L'], ['IH'], []), (1, ['S'], ['AE'], []), (0, ['K'], ['ER'], []), (2, [], ['AY'], ['D'])]
	return not SyllabificationsRhyme(s1,s2)
def testDontRhyme4():
	s1=[(0, ['R'], ['IY'], []), (1, ['P', 'R'], ['IH'], ['N', 'T'])]
	s2=[(0, [], ['IH'], ['M']), (1, ['P', 'R'], ['IH'], ['N', 'T'])]
	return not SyllabificationsRhyme(s1,s2);
def testDontRhyme5():
	s1=[(1, ['P'], ['AE'], []), (0, ['N'], ['AH'], ['L', 'D'])]
	s2=[(0, [], ['IH'], ['M']), (1, ['P'], ['AE'], []), (0, ['N'], ['AH'], ['L', 'D'])]
	return not SyllabificationsRhyme(s1,s2);
def testDontRhyme6():
	s1=[(1, ['F', 'L'], ['AY'], ['T']), (1, ['S'], ['EY'], ['F']), (0, ['T'], ['IY'], [])]
	s2=[(2, ['B'], ['AY'], []), (0, [], ['OW'], []), (1, ['S'], ['EY'], ['F']), (0, ['T'], ['IY'], [])]
	return not SyllabificationsRhyme(s1,s2);

