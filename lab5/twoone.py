import nltk
#import re
nltk.download()

def traverse(t, a):
    try:
        t.label()
    except AttributeError:
        b = 0
    else:
        #print t.label()       
        if t.label() == 'S':           
            for child in t:
                traverse(child, a)
            
        elif t.label() == 'PERSON':         
            l = t.leaves() 
            
            if  len(l)>0: 
                tup = l[0], 'PERSON' 
                a.append(tup)
            for child in t:
                traverse(child, a)
        
        elif t.label() == 'ORGANIZATION':         
            l = t.leaves() 
            if  len(l)>0: 
                tup = l[0], 'ORGANIZATION'
                a.append(tup)
            for child in t:
                traverse(child, a)
        
        elif t.label() == 'GPE':         
            l = t.leaves() 
            if  len(l)>0: 
                tup = l[0], 'GPE'
                a.append(tup)
            for child in t:
                traverse(child, a)

with open("news3.html", "r") as myfile:
    data = myfile.read()   
sentences = nltk.sent_tokenize(data)
sentences = [nltk.word_tokenize(sent) for sent in sentences]
sentences = [nltk.pos_tag(sent) for sent in sentences]

a = []

for i in range(len(sentences)):
    s = nltk.ne_chunk(sentences[i])
    traverse(s, a)

for x in a:
    print x[0][0],", ",x[1]

