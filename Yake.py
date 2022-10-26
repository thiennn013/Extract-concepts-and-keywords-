from yake import KeywordExtractor as Yake
import os
import glob
import pandas as pd
import time
start_time = time.time()

word=[]
diem=[]


file=('C:/Users/thien/PycharmProjects/NLP/Texts/africa_benin_activities.html.txt')
File = open(file) #open file
text =File.read() #read all lines


yake = Yake(lan="en")
yake_keyphrases = yake.extract_keywords(text)
for i in yake_keyphrases:
    word.append(i[0])
    diem.append(i[1])


data={
    'word': pd.Series(word),
    'diem': pd.Series(diem)
}

df=pd.DataFrame(data)
df.to_csv('C:/Users/thien/PycharmProjects/NLP/outYake.csv',sep='\t', encoding='utf-8',index=False)

print("--- %s seconds ---" % (time.time() - start_time))







