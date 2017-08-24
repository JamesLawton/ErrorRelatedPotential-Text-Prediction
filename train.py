import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer
import string
from nltk.tokenize.moses import MosesDetokenizer
import codecs
import collections
import numpy as np
import csv
import pandas as pd
import random
from random import randrange
import more_itertools as mit

from nltk.tokenize import word_tokenize



text = gutenberg.raw('carroll-alice.txt')
sentence_length = 5
text = text.replace('\n', ' ').replace('\r', '')
clean_text = RegexpTokenizer(r'\w+')

punctuations = list(string.punctuation)
punctuations.append("''")
punctuations.append("'")
punctuations.append('""')


sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
alice_sentences = sent_detector.tokenize(text.strip())
alice_sentences = [clean_text.tokenize(p) for p in alice_sentences]


#Reconstructed sentences to be congruent for displaying whole sentences
detokenizer = MosesDetokenizer()
detokenized_text = [detokenizer.detokenize(p, return_str=True) for p in alice_sentences if len(p) == sentence_length]

#Tokenized Sentences
tokenized_text = [word for word in alice_sentences if len(word) == 5]


print(tokenized_text)
print(detokenized_text[0])

#scramble detokenizer
random_index = randrange(0, len(tokenized_text))
#scrambled_text = random.choice(detokenized_text.replace(random_index))
#print (scrambled_text)

#example = [detokenized_text.replace(random_index) for x in detokenized_text]
#print (scrambled_text)






#scrambled text
lst = scrambled_text = tokenized_text
lst = ([x[randrange(0, sentence_length)] for x in tokenized_text])
word_randomizer = random.choice(lst)
random_number = randrange(0, sentence_length)
indices_to_replace = [i for i,x in enumerate(scrambled_text)]
print(indices_to_replace)
for i in indices_to_replace:
    scrambled_text[i][randrange(0, sentence_length)] = random.choice(lst)

print(scrambled_text)



#write to CSV

header = ["detokenized_text", "tokenized_text", "scrambled_text"]
csv_converter = pd.DataFrame(list(zip(detokenized_text, tokenized_text, scrambled_text)), columns = header)
csv_converter.to_csv("training.csv")









