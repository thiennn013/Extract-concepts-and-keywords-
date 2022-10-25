import os
import requests
import io #codecs
import nltk
from nltk.util import pad_sequence
from nltk.util import bigrams
from nltk.util import ngrams
from nltk.util import everygrams
from nltk.lm.preprocessing import pad_both_ends
from nltk.lm.preprocessing import flatten
# Text version of https://kilgarriff.co.uk/Publications/2005-K-lineer.pdf
# if os.path.isfile('language-never-random.txt'):
#     with io.open('language-never-random.txt', encoding='utf8') as fin:
#         text = fin.read()
# else:
#     url = "https://gist.githubusercontent.com/alvations/53b01e4076573fea47c6057120bb017a/raw/b01ff96a5f76848450e648f35da6497ca9454e4a/language-never-random.txt"
#     text = requests.get(url).content.decode('utf8')
#     with io.open('language-never-random.txt', 'w', encoding='utf8') as fout:
#         fout.write(text)
# # Tokenize the text.
# tokenized_text = [list(map(str.lower, nltk.word_tokenize(sent)))
#                   for sent in nltk.sent_tokenize(text)]
# print(tokenized_text[0])
# from nltk.lm.preprocessing import padded_everygram_pipeline
# n=3
# train_data, padded_sents = padded_everygram_pipeline(n, tokenized_text)
# # huấn luyện
# from nltk.lm import MLE
# model = MLE(n) # Lets train a 3-grams model, previously we set n=3
# print(model.vocab)
# model.fit(train_data, padded_sents)
# print(model.vocab)

import dill as pickle

# with open('kilgariff_ngram_model.pkl', 'wb') as fout:
#     pickle.dump(model, fout)

with open('kilgariff_ngram_model.pkl', 'rb') as fin:
    model = pickle.load(fin)
#Su dung
print(model.score("is","language".split()))#P(is|language)
print(model.entropy("The key word"))
print(model.generate(20,random_seed=3))