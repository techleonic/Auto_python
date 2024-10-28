#pip intall pydub
from pydub import AudioSegment

original_audio = AudioSegment.from_wav("beat.wav")

#reversing audio
reversed = original_audio.reverse()
reversed.export('reversed.wav')


#frist tow seconds
first_two = original_audio[0:2000]
first_two.export('tow_seconds.wav')

#leng in miliseconds
print(len(original_audio))

#merged audiofiles
merged = original_audio + reversed
merged.export("merged.wav")


#add silent
merged_silent = merged + AudioSegment.silent(1000)
merged_silent.export("merged_silent.wav")

#multiply audio
log_original =  original_audio*3
log_original.export("log_original.wav")

#increase de volumen
volume = log_original + 15
volume.export('volumen.wav')