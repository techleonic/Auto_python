from speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

recognizer = Recognizer()

with AudioFile('download.wav') as audio_file:
    audio =  recognizer.record(audio_file)

text =  recognizer.recognize_google(audio)
print(text)

analyzer = SentimentIntensityAnalyzer()
score = analyzer.polarity_scores(text)
print(score)

if score["compound"] > 0:
    print("positive speech")
else:
    print("Negative Speech")