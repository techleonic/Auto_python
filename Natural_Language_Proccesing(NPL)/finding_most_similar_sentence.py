import nltk
from nltk import  WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


text = 'Originally, vegatables were collected from the wild by hunter-gatherers. Vegetables are all plants. Vegetables can be eaten either raw or cooked'
question = 'What are vegetables?'

print("Question: " + question)
print("Data: "+ text)

lemmatizer = WordNetLemmatizer()
def lemma_me(sent):
    sentence = sent

    # make tokes of words
    sentence_tokens = nltk.word_tokenize(sentence.lower())
    # print(sentence_tokens)

    # part of speech tags (identifies is the part of speech is a verb, noun, adjective. etc)
    post_tags = nltk.pos_tag(sentence_tokens)
    # print(post_tags)

    #empty list fo word
    sentence_lemma = []

    # zip tow list one sentences tokens (separetion of words) and post tags (each word with a identifier)
    for token, post_tag in  zip(sentence_tokens, post_tags):
        # only for nouns verbs adjective and adverbs
        if post_tag[1][0].lower() in ['n','v','a','r','s']:
            # from the list of
            lemma = lemmatizer.lemmatize(token, post_tag[1][0].lower())
            sentence_lemma.append(lemma)

    return sentence_lemma

# tokenize sentence (it tokeize the Question) splits the question in sentences or words
sentence_tokens =  nltk.sent_tokenize(text)

#insert the las item in the list will be the question
sentence_tokens.append(question)
# print(sentence_tokens)

# analyze the importance of the world, make a matriz of the importance of the word
tv = TfidfVectorizer(tokenizer=lemma_me, token_pattern=None)

#learn this data
tf = tv.fit_transform(sentence_tokens)


import pandas

#get the data printed (lemmanized words and their weight { if a word is similliar y al sentences} )
df = pandas.DataFrame(tf.toarray(), columns=tv.get_feature_names_out())
csv = df.to_csv()
with open('sentence_weigth.csv', 'w', newline="") as file:
    file.write(csv )

#get similarities comparing the las item in the list wich is the Question Against the data
values = cosine_similarity(tf[-1], tf)
# print(values)

# first it would order the array from lowest to the highest
# and then it will give you a list of index from de lowest to the highest is -1 index
# nested list that's why we use [0]
# the last index  is the question in itself so (-2) will give you the second higher which is the sentence
index = values.argsort()[0][-2]


#it would get rip of the nested list and give a flat list
values_flat = values.flatten()

#list from the lowest to the highest
values_flat.sort()

# get the second lowest couse the first one is the question
coeff =values_flat[-2]

# threshold
# print the response above the treshhold
if coeff > 0.3 :
    print("Response: " + sentence_tokens[index])