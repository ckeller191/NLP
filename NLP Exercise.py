from textblob import TextBlob
import nltk

from nltk.corpus import stopwords
from pathlib import Path



blob = TextBlob(Path("book of John text.txt").read_text())




stops = stopwords.words("english")

more_stops = ["thy", "ye", "verily", "thee", "hath", "say", "thou", "art", "shall"]

stops += more_stops

items = blob.word_counts.items()



clean_items = [item for item in items if item[0] not in stops]


from operator import itemgetter


sorted_items = sorted(clean_items, key=itemgetter(1), reverse=True)


top15 = sorted_items[:15]


import matplotlib.pyplot as plt
from wordcloud import WordCloud

text = str(top15)

text_clean = text.replace("'", "")


wordcloud = WordCloud(colormap="prism", background_color="gray")

wordcloud = wordcloud.generate(text_clean)



wordcloud = wordcloud.to_file("BookOfJohnTop15.png")


plt.imshow(wordcloud)
print("done")
