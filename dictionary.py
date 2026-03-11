class Dictionary:
    def __init__(self):
        self._dict = list()

    def loadDictionary(self,path):
        # dict is a string with the filename of the dictionary
        f = open(path, 'r', encoding="utf8").readlines()
        for riga in f:
            campi = riga.strip()
            self._dict.append(campi)

    def printAll(self):
        for riga in self._dict:
            print(riga)

    @property
    def dict(self):
        return self._dict