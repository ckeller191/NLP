from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob)

#print(blob.sentences)

#print(blob.words)


print(blob.tags)