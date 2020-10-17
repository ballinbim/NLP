import nltk
# nltk.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path
from textblob import TextBlob

blob = TextBlob(Path('book of John text.txt').read_text())
stops = stopwords.words('english')
items = blob.word_counts.items()
items = [i for i in items if i[0] not in stops]

from operator import itemgetter

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
# print(sorted_items)

top15 = sorted_items[:15]
print(top15)

import pandas as pd

df = pd.DataFrame(top15, columns = ['word', 'count'])
print(df)

import imageio

mask_image = imageio.imread('mask_circle.png')

from wordcloud import WordCloud
wc = WordCloud(colormap = 'prism', mask = mask_image, background_color = 'white')

wc = wc.generate(df.to_string())

wc.to_file('Book of John.png')