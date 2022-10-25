from rake_nltk import Rake
import nltk
import os
import glob
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
NN = open('C:/Users/thien/PycharmProjects/NLP/NN.txt',"a")
NNP = open('C:/Users/thien/PycharmProjects/NLP/NNP.txt',"a")
os.chdir('Texts')
text =''
K=0
for file in list(glob.glob('*.txt')):
    File = open(file) #open file
    lines = File.read() #read all lines
    text +=lines
    K+=1
    if K == 30 :
        rake = Rake( max_length=4)
        rake.extract_keywords_from_text(text)
        rake_keyphrases = rake.get_ranked_phrases_with_scores()[:10]
        print(rake_keyphrases)
        text=''
        K=0