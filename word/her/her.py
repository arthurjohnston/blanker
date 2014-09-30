from nltk.corpus import cmudict
from nltk.corpus import wordnet as wn
import sys
class her:
    def __init__(self,a_list=None,a_dict=None):
        self.d=cmudict.dict()
        if a_list is not None and a_dict is not None:
            self.prolist=a_list
            self.prodict=a_dict
            return
       
        self.prolist=list()
        #this is actually a reverse pronouncing dictionary
        self.prodict=dict()
    
        for key, value in self.d.items():
            for pr in value:
                p=pr[:]
                p.reverse()
                self.prolist.append(tuple(p))
                #the is not none is because None is a key 
                if tuple(p) in self.prodict and self.prodict[tuple(p)] is not None: 
                    self.prodict[tuple(p)].append(key)
                else:
                    self.prodict[tuple(p)]=[key]

        #get rid of prolist after done            
        self.prolist.sort()
        
    def getSimilarEndings(self, phonemes, numMatches=1):
        '''gets the words with similar phonetic endings as (word) if
        numMatches is not specified then only the last phoneme is
        matched.''' 
        reverse=phonemes[:]
        reverse.reverse()
        reverse=tuple(reverse)
        return [p for p in self.prolist if p[:numMatches]==reverse[:numMatches]]

    def getRealWordsMinusPhonemes(self,phoneticWords,numRemoved=1):
         '''returns new dictionary of short words and long words from
         a set which are not also words when the last numRemoved
         phonemes are taken off'''
         realwords=dict()
         for phoneme in phoneticWords:
             
             shortphonemes=phoneme[numRemoved:]
             if not self.prodict.has_key(shortphonemes):
                 continue
             for t in self.prodict[shortphonemes]:
                 realwords[t]=self.prodict[tuple(phoneme)]
         return realwords

def getNonVerbs(toCheck):
    '''takes a dictionary and returns a dictionary where the each key
    has a meaning in verb form'''
    return dict((k,v) for k, v in toCheck.items() if any(w.pos=='v' for w in wn.synsets(k)))
    
def removeNonWords(toCheck):
    '''takes a dictionary and returns a list of only words that are in
    wordnet only for the values though'''
    return [(k,w) for k,v in toCheck.items() for w in v if wn.synsets(w) ]

def printToFile(items,fileName='her.txt'):
    f=open(fileName,'w')
    for v,n in items:
        f.write(n+'\t'+v+'\n')

def getAllBlankers(word='her',count=1):
    r=her()
    pronounciations=r.d[word]
    done=dict()
    for v in pronounciations: 
        endings=r.getSimilarEndings(r.d[word][0])
        rw=r.getRealWordsMinusPhonemes(endings,count)
        nv=getNonVerbs(rw)
        #dm=getDifferentMeanings(nv)
        done.update(nv)
    removed=removeNonWords(done)
    removed.sort()
    return removed

if __name__ == "__main__":
    if(len(sys.argv)<3):
        sys.exit("The program requires at least 2 arguments, a word and how many syllables to match, and optionally a file to write the results to.")
    matches=int(sys.argv[2])
    results=getAllBlankers(sys.argv[1],matches)
    if(len(sys.argv)>3):
        printToFile(results,sys.argv[3])
    else:
        for i in results:
            print (i)



    
