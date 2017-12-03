import nltk 
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import RegexpStemmer
from nltk.tokenize import word_tokenize
from TurkishStemmer import TurkishStemmer

stemmer = PorterStemmer()
stem1 = stemmer.stem('cooking')
print stem1

stem2 = stemmer.stem('cookery')
print stem2

stemmer = LancasterStemmer()
stem3 = stemmer.stem('cooking')
print stem3

stemmer = RegexpStemmer('ing')
stem4 = stemmer.stem('ingleside')
print stem4

example_words = ['python','pythoner','pythoning','pythoned']


for w in example_words:
	print(PorterStemmer().stem(w))
"""
next_text = "It is very important to be pythonly while you are pythoning with python.All pythoners have pythoned poorly at least once."

words = word_tokenize(next_text)

for w in words:
	print(PorterStemmer().stem(w))
"""

stemmer = TurkishStemmer()
stemmer.stem("okuldakilerden")
