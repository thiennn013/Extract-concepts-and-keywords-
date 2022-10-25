import pandas as pd
import numpy as np


file = ('./outNN.txt')
File = open(file)  # open file
lines = File.read()


a=np.array(lines.split(',')) # đưa từng từ vào array a

unique,counts = np.unique(a,return_counts=True) # đếm từ lưu vào array counts và tư lưu vào unique

data={'word':unique,
      'count':counts
      }

df = pd.DataFrame(data)
df.sort_values(['count','word'], inplace=True ,ascending=False) #sắp xếp theo chiều giảm của count

print(df.to_string())
df.to_csv('outExtract.csv',sep='\t', encoding='utf-8',index=False) # xuất file




