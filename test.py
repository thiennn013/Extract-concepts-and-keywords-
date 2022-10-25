import nltk
import os
import glob
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()


file=('./Texts/africa_benin_activities.html.txt')
# file = ('C:/Users/thien/PycharmProjects/NLP/Texts/africa_benin_activities.html.txt')
File = open(file)
lines = File.read() #read all lines
# lines=lines.lower()
sentences = nltk.sent_tokenize(lines) #tokenize sentences


# for sentence in sentences:
#     print(nltk.pos_tag(nltk.word_tokenize(str(sentence)),end='\n'))
#     #

for sentence in sentences:
     for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
         print(word,pos)
print('done')