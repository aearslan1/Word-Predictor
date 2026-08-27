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
    
    def sameWordRatio(self,word: str,mass: int):
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
    
    def letterSequenceRatio(self,word: str,mass: int):
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
  

    
