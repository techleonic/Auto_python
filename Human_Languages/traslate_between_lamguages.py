from googletrans import Translator

translator = Translator()

translation = translator.translate('hola como estas?',dest='en')
print(translation.text)
