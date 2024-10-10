import nltk
from nltk.stem import WordNetLemmatizer

x = "was"
y = "is"
# nltk.download("wordnet")
lemmatizer = WordNetLemmatizer()

lemma = lemmatizer.lemmatize(x,"v")
lemma2 = lemmatizer.lemmatize(y, "v")
print(lemma == lemma2)