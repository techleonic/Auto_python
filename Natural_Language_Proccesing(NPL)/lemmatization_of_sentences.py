import nltk
from nltk.stem import WordNetLemmatizer


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


print(lemma_me("i am the best programmer"))