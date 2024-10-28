from pydub import AudioSegment

beat = AudioSegment.from_wav('beat.wav')
sax = AudioSegment.from_wav('sax.wav')
print(len(beat), len(sax))
beat_2 = beat*2

mixed = beat_2.overlay(sax)
mixed.export('mixed.wav')
