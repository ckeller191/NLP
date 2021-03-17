from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

#print(blob.sentences)

#print(blob.words)


#print(blob.tags)

#print(blob.noun_phrases)

#print(blob.sentiment)

#print(round(blob.sentiment.polarity,3))

#print(round(blob.sentiment.subjectivity,3))

sentences = blob.sentences

"""
for sentence in sentences:
    print(sentence)
    print(sentence.sentiment)
    #can use round on the ones below
    print(sentence.sentiment.polarity)
    print(sentence.sentiment.subjectivity)
"""


from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

"""
print(blob.sentiment)

for sentence in blob.sentences:
    print(blob.sentiment)

blob.detect_language()   #detect the language of the text - should return 'en'

spanish = blob.translate(to='es')

print(spanish)
"""

from textblob import Word
"""
index = Word('index')

print(index.pluralize())

cacti = Word('cacti')

print(cacti.singularize())


animals = TextBlob('dog cat fish bird').words

print(animals.pluralize())

"""

word = Word('theyr')

print(word.spellcheck())

corrected_word = word.correct()

sentence = TextBlob('Ths sentense has missplle wrds')

corrected_sentence = sentence.correct()

print(corrected_word)
print(corrected_sentence)
