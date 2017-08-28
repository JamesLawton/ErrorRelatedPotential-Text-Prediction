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
import copy
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


#scramble detokenizer
random_index = randrange(0, len(tokenized_text))

#scrambled text
lst = tokenized_text
scrambled_text = copy.deepcopy(tokenized_text)

lst = ([x[randrange(0, sentence_length)] for x in list(tokenized_text)])
word_randomizer = random.choice(lst)
random_number = randrange(0, sentence_length)
indices_to_replace = [i for i,x in enumerate(scrambled_text)]
for i in indices_to_replace:
    scrambled_text[i][randrange(0, sentence_length)] = word_randomizer
    print(scrambled_text[i].index(word_randomizer))


#TODO
for i, line in enumerate(scrambled_text):
    for j, value in enumerate(line):
        if (scrambled_text[i][j] not in tokenized_text[i][j]):
            new_list = scrambled_text[i][j]
            #print(new_list)

#print(new_list)


"""
for i in indices_to_replace:
    for x in enumerate(scrambled_text[i]):
        if (scrambled_text[x] not in tokenized_text[x]):
            result = x
        print(result)
"""

print(tokenized_text)
print(scrambled_text)
print(scrambled_text)



#write to CSV

header = ["detokenized_text", "tokenized_text", "scrambled_text"]
csv_converter = pd.DataFrame(list(zip(detokenized_text, tokenized_text, scrambled_text)), columns = header)
csv_converter.to_csv("training.csv")









