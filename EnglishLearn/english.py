from wordsCounter import countWords
from translate import Translator
def translateDict():
    translator = Translator(from_lang='ru', to_lang='en', provider='mymemory')
    words = countWords()
    for word in words.keys():
        print(translator.translate(word))
translateDict()