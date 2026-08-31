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
            similarityRatios[poolWord] = (sameGramCount / full) * mass
                 
        return similarityRatios 

    def allRatio(self,word):
        letterSequenceRatio = self.letterSequenceRatio(word,0.2)
        sameWordRatio = self.sameWordRatio(word,0.1)
        nGramRatio = self.nGramRatio(word,0.7)

        ratioResults = [letterSequenceRatio, sameWordRatio, nGramRatio]

        blankDict = {}
        for name in self.wordPool:
            blankDict[name] = 0
        
        for ratios in ratioResults:
            for ratio in ratios:
                blankDict[ratio] += ratios[ratio]

        return blankDict

    def bestProb(self,word:str):
        allRatios = self.allRatio(word)
        maxValueKey = list(allRatios.keys())[0]
        for key in allRatios:
            if allRatios[key] > allRatios[maxValueKey]:
                maxValueKey = key

        return maxValueKey

examplePool1 = [
    "ahmet", "mehmet", "ali", "veli", "ayse", "fatma", "zeynep", "emine", "hatice", "elif",
    "can", "cem", "efe", "ege", "kaaan", "deniz", "derin", "duru", "su", "toprak",
    "yagmur", "ruzgar", "gunes", "bulut", "irmak", "nehir", "okyanus", "uzay", "evren", "dunya",
    "burak", "emre", "onur", "serkan", "hakan", "gokhan", "volkan", "koray", "tolga", "alper",
    "arda", "baran", "batuhan", "berk", "berkay", "berkan", "bugra", "doruk", "yigit", "yagiz",
    "asli", "banu", "buse", "ceren", "damla", "ebru", "eda", "esra", "gamze", "gözde",
    "gizem", "gül", "hande", "ilayda", "ipek", "irem", "kubra", "leyla", "merve", "naz",
    "ozge", "pinar", "selin", "sibel", "simge", "sinem", "tugba", "yagmur", "yasemin", "yaren",
    "adem", "akif", "alp", "alparslan", "anil", "aras", "atilla", "aykut", "ayhan", "azer",
    "bahadir", "baris", "baskin", "bayram", "bilal", "bora", "bulut", "cagri", "cihan", "cumhur",
    "davut", "dogukan", "durmus", "ekrem", "enver", "erdal", "erhan", "erkan", "ercan", "erdinc",
    "erim", "erol", "ersin", "ersun", "eup", "fatih", "ferdi", "ferhat", "feti", "feyyaz",
    "fikret", "furkan", "hakan", "halil", "haluk", "hamza", "harun", "hasan", "huseyin", "ibrahim",
    "ismail", "izzet", "kadir", "kamil", "kerem", "kerim", "korhan", "kursat", "levent", "mahir",
    "mahmut", "metin", "mithat", "muhammed", "mustafa", "muzaffer", "naci", "nadird", "naim", "nami",
    "necati", "necmi", "nedim", "nihat", "niyazi", "nuri", "oguz", "oguzhan", "okan", "oktay",
    "orhan", "osman", "ozan", "ozgur", "ozkan", "omer", "onder", "orhan", "ramazan", "rasim",
    "recep", "resul", "riza", "saban", "sabit", "sadik", "samet", "sami", "sedat", "selim",
    "semih", "serdar", "serhat", "serkan", "sinan", "soner", "suleyman", "taha", "tahir", "tarkan",
    "tashin", "tayfun", "taylan", "temel", "teoman", "timur", "tolga", "turgut", "ufuk", "ugur",
    "umut", "unal", "utku", "uzeyir", "vahit", "vedat", "veysel", "volkan", "yasin", "yasar",
    "yavuz", "yunus", "yusuf", "zafer", "zihni", "ziya", "azra", "belinay", "berra", "ceylin",
    "defne", "duru", "ecrin", "ela", "eslem", "ebrar", "eylul", "hira", "liva", "mira",
    "nisanur", "oyku", "zehra", "zümra", "asude", "aybuke", "aysegul", "azile", "bengusu", "beren",
    "beyza", "bilge", "busra", "cansu", "dilan", "dilara", "dilay", "ece", "edanur", "elvin",
    "esma", "esmanur", "feride", "filiz", "funda", "gulsen", "habibe", "hacer", "hale", "hanife",
    "havva", "hidayet", "humeysa", "ilknur", "inci", "kader", "kibriye", "kubra", "lale", "leman",
    "leyla", "medine", "melek", "meltem", "meryem", "mihriban", "mine", "muge", "nagihan", "nalan",
    "nazli", "necla", "neslihan", "nesrin", "nimet", "nurgul", "nuran", "nuray", "pelin", "perihan",
    "rabia", "rahiyle", "ramize", "reyhan", "rumeysa", "saadet", "safiye", "samime", "sanem", "saniye",
    "seda", "seher", "selma", "semra", "senem", "serap", "sevda", "sevgi", "sevil", "sevim",
    "sezen", "songul", "suheda", "sule", "sümeyye", "sultan", "suzun", "serife", "sermin", "sukran",
    "tuba", "tulay", "turkan", "ulku", "umran", "vildan", "vuslat", "zehra", "zeliha", "zubeyde"
]

epredictor = EPredictor(examplePool1)

print(epredictor.bestProb("mrym")) #returns meryem