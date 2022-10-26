import nltk
import os
import glob
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
import pandas as pd
import numpy as np
import time


start_time = time.time()



NN = open('C:/Users/thien/PycharmProjects/NLP/outNN.txt',"a")
NNP = open('C:/Users/thien/PycharmProjects/NLP/outNNP.txt',"a")

os.chdir('Texts')

# thao tác từng file trong corpus
for file in list(glob.glob('*.txt')):
    File = open(file) #mở file
    lines = File.read() # đọc tất cả dòng
    sentences = nltk.sent_tokenize(lines) #tách câu

# Duyệt từng câu trong file
    for sentence in sentences:
        # Tách và duyệt từng từ trong câu, sau đó tiến hành gán nhãn
         for word,pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
             if pos == 'NN':
                 NN.write(word.lower()+',')
             if  pos == 'NNS':
                 NN.write(lemma.lemmatize(word).lower() + ',')


file = ('C:/Users/thien/PycharmProjects/NLP/outNN.txt')
File = open(file)  # open file
lines = File.read()

# đưa từng từ vào array a
a=np.array(lines.split(',')) 

# đếm từ lưu vào array counts và tư lưu vào unique
unique,counts = np.unique(a,return_counts=True) 

data={'word':unique,
      'count':counts
      }

df = pd.DataFrame(data)
df.sort_values(['count','word'], inplace=True ,ascending=False) #sắp xếp theo chiều giảm của count

print(df.to_string())
df.to_csv('C:/Users/thien/PycharmProjects/NLP/outExtract.csv',sep='\t', encoding='utf-8',index=False) # xuất file


print("--- %s seconds ---" % (time.time() - start_time))
print('done')
