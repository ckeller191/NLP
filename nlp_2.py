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

stops = stopwords.words("engligh")

items = blob.word_counts.items()