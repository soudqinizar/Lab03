import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        self.dictionary = dict()
        self.dictionary["italian"] = d.Dictionary()
        self.dictionary["english"] = d.Dictionary()
        self.dictionary["spanish"] = d.Dictionary()
        self.dictionary["italian"].loadDictionary("resources/Italian.txt")
        self.dictionary["english"].loadDictionary("resources/English.txt")
        self.dictionary["spanish"].loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        return self.dictionary[language].printAll()

    def searchWord(self, words, language):
        tes = list()

        for word in words:
            rich = rw.RichWord(word)
            tes.append(rich)
            if word in self.dictionary[language].dict:
                rich.corretta = True
            else:
                rich.corretta = False
        return tes


    def searchWordLinear(self, words, language):
        tes = list()

        for word in words:
            rich = rw.RichWord(word)
            tes.append(rich)
            if word in self.dictionary[language].dict:
                rich.corretta = True
            else:
                rich.corretta = False
                break
        return tes

    def searchWordDichotomic(self, words, language):

        tes = list()
        dict1 = self.dictionary[language].dict
        for word in words:
            dict = dict1
            rich = rw.RichWord(word)
            tes.append(rich)
            rich.corretta = False
            meta = 2
            while (not rich.corretta) and (l > 1):
                meta = int(len(dict) / 2)
                if dict[meta] == word:
                    rich.corretta = True
                    break
                elif word > dict[meta]:
                    dict = dict[(meta + 1):]
                else:
                    dict = dict[:(meta - 1)]

        return tes


