class EPredictor():
    def __init__(self,wordPool: list):
        self.wordPool = wordPool

    def doBigger(self,*words: str):
        biggerWord = words[0]
        for word in words:
            if len(word) > len(biggerWord):
                biggerWord = word
        return biggerWord

    def doSmaller(self,*words : str):
        smallerWord = words[0]
        for word in words:
            if len(word) < len(smallerWord):
                smallerWord = word
        return smallerWord

    def convertSet(self,text: str):
        addedLetters = []
        for letter in text:
            if letter in addedLetters:
                continue
            else:
                addedLetters.append(letter)
            
        return addedLetters

    def nGramAlgorithm(self,word: str,n: int):
        packet = []
        i = 0
        while i + n <= len(word):
            packet.append(word[i:i+n])
            i += 1
        return set(packet)
    def sameWordRatio(self,word: str,mass: float):
        setWord = self.convertSet(word) #kelimenin harflerini listeye attık,küme formatı ile
        similarityRatios = {} 

        for poolWord in self.wordPool: #kelime havuzundaki kelimeleri alıyoruz.
            setPoolWord = self.convertSet(poolWord)
            sameWordCount = 0
            for poolWordLetter in setPoolWord:
                for mainWordLetter in setWord:
                    if mainWordLetter == poolWordLetter:
                        sameWordCount += 1
            longerSet = max(len(setWord),len(setPoolWord))
            similarityRatios[poolWord] = (sameWordCount / longerSet) * mass
        
        return similarityRatios
    
    def letterSequenceRatio(self,word: str,mass: float):
        similarityRatios = {}
        for poolWord in self.wordPool:
            sameSequenceCount = 0
            longerWord = self.doBigger(word,poolWord)
            smallerWord = self.doSmaller(poolWord,word)
            for i in range(len(smallerWord)):
                if smallerWord[i] == longerWord[i]:
                    sameSequenceCount += 1
            similarityRatios[poolWord] = (sameSequenceCount / len(longerWord)) * mass
        return similarityRatios

    def nGramRatio(self, word: str,mass: float,n=2):
        wordNGrams = self.nGramAlgorithm(word, n)
        similarityRatios = {}
        for poolWord in self.wordPool:
            sameGramCount = 0
            poolWordNGrams = self.nGramAlgorithm(poolWord, n)

            for poolWordGram in poolWordNGrams:
                for wordGram in wordNGrams:
                    if wordGram == poolWordGram:
                        sameGramCount += 1

            full = len(set(poolWordNGrams).union(set(wordNGrams)))
            similarityRatios[poolWord] = sameGramCount / full
                 
        return similarityRatios

    def allRatio(self,word: str,mass:float):
        pass
pool = ["ali", "veli", "can", "aaa"]

epredictor = EPredictor(pool)

print(epredictor.nGramRatio(word="aaa",mass=1,n=2))