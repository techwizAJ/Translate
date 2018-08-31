from textblob import TextBlob
text = input(" Enter any text to translate in english ")
en_blob = TextBlob(text)
from_language = en_blob.detect_language()
print(en_blob.translate(from_lang= from_language ,to="en"))
