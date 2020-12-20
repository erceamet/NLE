import nltk
from nltk.book import *
from nltk import re
from nltk import FreqDist

ws = text7.tokens
ws_nopunct = [word.lower() for word in ws if re.search("\w", word)] 
ws_fdist = FreqDist(ws_nopunct)
ws_fdist_50 = ws_fdist.most_common(50)
print(ws_fdist_50)
