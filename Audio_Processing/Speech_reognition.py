from speech_recognition import Recognizer, AudioFile

recognizer = Recognizer()
with AudioFile('chile.wav') as audiofile:
    audio = recognizer.record(audiofile)

text = recognizer.recognize_google(audio)

print(text)