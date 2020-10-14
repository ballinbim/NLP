import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords
from textblob import TextBlob
from pathlib import Path
from textblob import TextBlob

blob = TextBlob(Path('RomeoAndJuliet.txt').read_text())


stops = stopwords.words('english')
# print(stops)

# blob = TextBlob('Today is a beautiful day.')
#print(blob.words)

# new_blob = [word for word in blob.words if word not in stops]
# print(new_blob)

items = blob.word_counts.items()
# print(items)

items = [i for i in items if i[0] not in stops]
# print(items)

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
# print(sorted_items)

top20 = sorted_items[1:21]
print(top20)

import pandas as pd

df = pd.DataFrame(top20, columns = ['word', 'count'])
print(df)

exes = df.plot.bar(x = 'word', y = 'count', legend = False)

import matplotlib.pyplot as plt

plt.gcf().tight_layout()

plt.show()