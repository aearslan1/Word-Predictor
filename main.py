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
  
    def getLeftSideMinOnMatrix(self,matrix: list,row: int,col: int):
        colCount = len(matrix[0])
        rowCount = len(matrix)
        if row < 0 or col < 0 or row >= rowCount or col >= colCount:
            return False
        
        rowNum = row
        colNum = col

        sides = [] #[üst , sol üst çapraz , sol]
    
        #üst taraf (row - 1 , col)
        if rowNum - 1 >= 0:
            sides.append(matrix[rowNum - 1][colNum])
        #sol üst taraf (row - 1 , col - 1)
        if rowNum - 1 >= 0 and colNum - 1 >= 0:
            sides.append(matrix[rowNum - 1][colNum - 1])
        
        #sol taraf (row , col - 1)
        if colNum - 1 >= 0:
            sides.append(matrix[rowNum][colNum - 1])
        if sides:
            minValue = min(sides)
        else:
            minValue = 0
        return minValue
    
    def levenshteinDistance(self,word: str):
        similarityRatios = {}
        wordList = [0]
        wordList.extend(letter for letter in word)
        for poolWord in self.wordPool:
            poolWordList = [0]
            poolWordList.extend(letter for letter in poolWord)
            matrix = [[0 for _ in range(len(poolWord) + 1)] for _ in range(len(word) + 1)]

            for y in range(len(poolWord) + 1):
                for x in range(len(wordList)):
                    minValue = self.getLeftSideMinOnMatrix(matrix,x,y)
                    if wordList[x] == poolWordList[y]:
                        matrix[x][y] = minValue
                    else:
                        matrix[x][y] = minValue + 1
            self.getLeftSideMinOnMatrix(matrix,0,0)
            
            

    def allRatio(self,word: str):
        sameWordProbs = self.sameWordRatio(word,0.3)
        letterSequenceProbs = self.letterSequenceRatio(word,0.7)
        for poolWord in self.wordPool:
            letterSequenceProbs[poolWord]+= sameWordProbs[poolWord]
        return letterSequenceProbs

    def bestProb(self,word: str):
        ratios = self.allRatio(word)
        biggerValue = (list(ratios.keys())[0],ratios[list(ratios.keys())[0]])
        for name in ratios:
            keyValue = ratios[name]
            if keyValue > biggerValue[1]:
                biggerValue = (name,keyValue)
        return biggerValue
epredictor = EPredictor(wordPool=["egemem","berkay","görkem"])

print(epredictor.bestProb("pep"))
