import nltk
from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer
from nltk.tokenize.moses import MosesDetokenizer
import csv
import pandas as pd
import random
from random import randrange
import copy




#text = gutenberg.raw('carroll-alice.txt')


#Text Import and Cleaning
f = open('pg13897.txt')
text = f.read()
sentence_length = 5
text = text.replace('\n', ' ').replace('\r', '').replace('_', '')
clean_text = RegexpTokenizer(r"'\w+|\w+'\w+|\w+'|\w+")

#Create sentences from the text, then tokenize each sentence
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
text_sentence = sent_detector.tokenize(text.strip(',.').lower())
print(text_sentence)
text_sentence = [clean_text.tokenize(p) for p in text_sentence]
print(text_sentence)

#Reconstruct the sentences for displaying whole sentences of only a certain sentence length
detokenizer = MosesDetokenizer()
detokenized_text = [detokenizer.detokenize(p, return_str=True) for p in text_sentence if len(p) == sentence_length]

#Tokenized Sentences
tokenized_text = [word for word in text_sentence if len(word) == sentence_length]

#Scramble the text
scrambled_text = copy.deepcopy(tokenized_text)
lst = tokenized_text
random_index = randrange(0, len(tokenized_text))
lst = ([x[randrange(0, sentence_length)] for x in list(tokenized_text)])
random_number = randrange(0, sentence_length)
correct_target = []
indices_to_replace = [i for i,x in enumerate(scrambled_text)]
for i in indices_to_replace:
    word_randomizer = random.choice(lst)
    scrambled_text[i][randrange(0, sentence_length)] = word_randomizer
    #index the word randomizer to output the correct target
    correct_target.append(scrambled_text[i].index(word_randomizer))

#write to CSV
header = ["correct_target", "detokenized_text", "scrambled_text", "tokenized_text"]
csv_converter = pd.DataFrame(list(zip(correct_target,detokenized_text, scrambled_text, tokenized_text)), columns = header)
csv_converter.to_csv("training.csv")









