import pymorphy2

def readFile(filename = 'input.txt'):
    file = open(filename, encoding="UTF-8")
    return file

def getWords():
    words = ""
    file = readFile()
    for line in file:
        words += line.replace('\n', '')
    return words

def prepareWordsToParse():
    words = getWords()
    words = words.replace('.', ' ')
    words = words.replace(',', ' ')
    words = words.replace('-', ' ')
    words = words.replace('!', ' ')
    words = words.replace('?', ' ')
    words = words.replace('"', ' ')
    words = words.replace(';', ' ')
    words = words.replace(':', ' ')
    words = words.lower()
    return words.split()

def sortDict(words):
    result = dict(sorted(words.items(), key=lambda item: -item[1]))
    return result

def normalizeWords(words = prepareWordsToParse()):
    wordsNormalized = []
    morph = pymorphy2.MorphAnalyzer(lang="ru")
    for element in words:
        wordsNormalized.append(morph.parse(element)[0].normal_form)
    return wordsNormalized

def countWords(wordsNorma = normalizeWords()):
    wordsStat = {}
    for element in wordsNorma:
        if element in wordsStat:
            wordsStat[element] += 1
        else:
            wordsStat[element] = 1
    return sortDict(wordsStat)

def writeFile(filename = 'output.txt'):
    file = open(filename, encoding='utf-8', mode='w')
    file.write(str(countWords()))
    return "yess"

