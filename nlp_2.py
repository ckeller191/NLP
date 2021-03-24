from textblob import TextBlob
import nltk

#nltk.download("stopwords")
from nltk.corpus import stopwords
from pathlib import Path

import pandas as pd

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

"""
print(blob.word_counts["juliet"])

print(blob.word_counts["romeo"])

print(blob.word_counts["thou"])

print(blob.words.count("joy"))

print(blob.noun_phrases.count("lady capulet"))
"""

stops = stopwords.words("english")

more_stops = ['thee', 'thy', 'thou']

stops += more_stops

items = blob.word_counts.items()
#print(items)

clean_items = [item for item in items if item[0] not in stops]

#print(clean_items)


#Sorting natively

from operator import itemgetter

sorted_items = sorted(clean_items)
#print(sorted_items[:10])

#using itemgetter

sorted_items = sorted(clean_items, key=itemgetter(1), reverse=True)
#print(sorted_items[:10])

top20 = sorted_items[:20]

print(top20)

df = pd.DataFrame(top20, columns=["word", "count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="word", y="count", rot=0, legend=False, color=["y", "c", "m", "b", "g", "r"])

plt.gcf().tight_layout

plt.show()

#WORDCLOUD -- Make sure to install wordcloud

from pathlib import Path
from wordcloud import WordCloud
import imageio

text = Path("RomeoAndJuliet.txt").read_text()
#print(text)

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoAndJulietHeart.png")

plt.imshow(wordcloud)
print("done")