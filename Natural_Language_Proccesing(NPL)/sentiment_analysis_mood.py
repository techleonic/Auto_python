import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
#sentiments dict
# nltk.download('vader_lexicon')

analyzer = SentimentIntensityAnalyzer()

text1= "Hey, what a beautiful day! How amazing it is!"
print("Text: " + text1)


#analize the text and give youa coefficiant of positivity, negativity and neutrality
#{'neg': 0.0, 'neu': 0.42, 'pos': 0.58, 'compound': 0.8513}
# compound can between -1 : 1
# neg + neu + pos = 1
coeff = analyzer.polarity_scores(text1)


if coeff["compound"] > 0:
    print("Positive Text")
else:
    print("Negative Text")



