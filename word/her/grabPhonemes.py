from collections import defaultdict
from curses.ascii import isdigit

def returnNGramNonVowelsPhonemes(pronunciations):
    '''takes a pronunciation (a list of phonemes) and returns all N-gram 
    phonemes. However it only returns the greedy matching versions'''
    a_set=set()
    for p in pronunciations:
        start,end=0,0
        while end<len(p):
            if isdigit(p[end][-1]):
                if start!=end:
                    a_set.add(tuple( p[start:end]))
                start=end+1
            end+=1
    return a_set

def createNGramPhonemes(values,size=None):
    phonemes=defaultdict(int)

    #goes through all the words and pulls out multi-consonant phonemes
    for pronunciations in values:
        for p in pronunciations:
            start,end=0,0
            while end<len(p):
                if isdigit(p[end][-1]):
                    #the first is to not add empties, the second
                    #is to not catch length 1 consonants
                    if start!=end and start+1!=end:
                        #print start,' ',end, ' ',p[start:end],' ',p
                        phonemes[(tuple( p[start:end]))]+=1
                    start=end+1
                end+=1

    if size is None:
        return phonemes
    items=sorted(((v,k) for k,v in phonemes.items()),reverse=True)
    return items[:size]
def easy(v):
    return addNGramNonVowelsPhonemes(v)
