import HTMLParser
class TableParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.in_td = False
        self.in_tr = False
        self.values =dict()
        self.TDCount = 0
        self.word =""
        
    def handle_starttag(self, tag, attrs):
        if tag == 'tr':
            self.in_tr = True
            self.TDCount = 0; # need to keep track of this because of extra tds
        if tag == 'td' and self.in_tr:
            self.in_td = True
            self.TDCount+=1
        if tag == 'b':
            self.in_td = False
    def handle_data(self, data):
        if self.in_td:
            if self.TDCount%3==2:
                self.word=data
            if self.TDCount%3==0:
                self.values[self.word]=int(data)
     
    def handle_endtag(self, tag):
        self.in_td = False
        if tag=='tr':
            self.in_tr = False
    def get_values(self):
        return self.values

def getWordFrequency(): 
    import urllib
    htmlparser = TableParser()
    fileName='{0}-{1}.html'
    start = 1
    end = 0
    iterate = 1000
    while end< 40000:
        end+=iterate
        data = urllib.urlopen(fileName.format(start,end))
        htmlparser.feed(data.read())      
        start+=iterate
        if end==10000:
            iterate=2000
    data = urllib.urlopen(fileName.format(start,41284))
    htmlparser.feed(data.read())      
       
    
    return htmlparser.get_values()
    
    
