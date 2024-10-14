import nltk
from nltk import  WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer


text = 'Originally, vegatables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked'
question = 'What are vegetables?'
def lemma_me(sent):
    lemmatizer = WordNetLemmatizer()
    sentence = sent

    # make tokes of words
    sentence_tokens = nltk.word_tokenize(sentence.lower())

    # part of speech tags
    post_tags = nltk.pos_tag(sentence_tokens)
    print(post_tags)
    sentence_lemma = []
    for token, post_tag in  zip(sentence_tokens, post_tags):
        # only for nouns verbs adjective and adverbs
        if post_tag[1][0].lower() in ['n','v','a','r','s']:
            lemma = lemmatizer.lemmatize(token, post_tag[1][0].lower())
            sentence_lemma.append(lemma)

    return sentence_lemma

sentence_tokens =  nltk.sent_tokenize(text)
print(sentence_tokens)

tv = TfidfVectorizer(tokenizer=lemma_me)

tf = tv.fit_transform(sentence_tokens)

# see data
print(tf.toarray())
import pandas

df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())
csv = df.to_csv()
with open('sentence_weigth.csv', 'w', newline="") as file:
    file.write(csv, )