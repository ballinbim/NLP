from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

# print(blob.sentences)

# print(blob.words)

# print(blob.tags)

# print(blob.noun_phrases)

# print(blob.sentiment)


sentences = blob.sentences

# for sentence in sentences:
#     print(sentence)
#     print(sentence.sentiment)
#     print(round(sentence.sentiment.polarity,3))
#     print(round(sentence.sentiment.subjectivity,3))

from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer= NaiveBayesAnalyzer())

# print(blob.sentiment)

sentences = blob.sentences

# for sentence in sentences:
#     print(sentence.sentiment)

# print(blob.detect_language())

spanish = blob.translate(to = 'es')
# print(spanish)
# print(spanish.translate())

viet = blob.translate(to = 'vi')
# print(viet)
# print(viet.translate())

from textblob import Word

index = Word('index')
# print(index.pluralize())

animals = TextBlob('dog cat fish sheep bird').words
# print(animals.pluralize())

cacti = Word('cacti')
# print(cacti.singularize())

word = Word('theyr')
# print(word.spellcheck())
word = word.correct()
# print(word)

sentence = TextBlob('The sentence has missplled wrds.')
sentence = sentence.correct()
print(sentence)