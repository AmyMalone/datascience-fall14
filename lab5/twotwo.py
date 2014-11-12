import nltk
import re

AT = re.compile(""" (.*( analyst| chair(wo)?man| commissioner| counsel| director| 
economist| editor| executive| foreman| governor| head| lawyer| leader| 
librarian).*)| manager| partner| president| producer| professor| researcher| 
spokes(wo)?man| writer| ,\sof\sthe?\s*  # "X, of (the) Y" """, re.VERBOSE)

for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels('PER', 'ORG', doc, corpus='ieer', pattern = AT):
        print(nltk.sem.rtuple(rel))


