import time

import multiDictionary as md

class SpellChecker:

    def __init__(self):
        pass

    def handleSentence(self, txtIn, language):


        multi = md.MultiDictionary()
        words = replaceChars(txtIn.lower()).split(" ")

        start_timeCon = time.perf_counter()
        soluzioneCon = multi.searchWord(words, language)
        end_timeCon = time.perf_counter()
        erroriCon = list()
        i = 0
        for riga in soluzioneCon:
            if not riga.corretta:
                erroriCon.append(riga)
                i = i + 1
        print("______________________________\n" +
              "      Using Contains Method\n" +
              "______________________________")
        print(f"Il numero di parole errate è: {i}")
        for elemento in erroriCon: print(f"Parola errata: {elemento}")
        elapsed_time = end_timeCon - start_timeCon
        print(f"Tempo di esecuzione: {elapsed_time:.6f} secondi")
        print("______________________________\n" +
              "      Using Linear Method\n" +
              "______________________________")



        start_timeLin = time.perf_counter()
        soluzioneLin = multi.searchWordLinear(words, language)
        end_timeLin = time.perf_counter()
        erroriLin = None
        i = 0
        for riga in soluzioneLin:
            if not riga.corretta:
                erroriLin = riga
                i = 1
        print(f"Il numero di parole errate è: {i}")
        print(f"La prima parola errata trovata è: {erroriLin}")
        elapsed_timeLin = end_timeLin - start_timeLin
        print(f"Tempo di esecuzione: {elapsed_timeLin:.6f} secondi")
        print("______________________________\n" +
              "      Using Dichotomic Method\n" +
              "______________________________")

        start_timeDicho = time.perf_counter()
        soluzioneDicho = multi.searchWordLinear(words, language)
        end_timeDicho = time.perf_counter()
        erroriDicho = None
        i = 0
        for riga in soluzioneDicho:
            if not riga.corretta:
                erroriDicho = riga
                i = 1
        print(f"Il numero di parole errate è: {i}")
        print(f"La prima parola errata trovata è: {erroriDicho}")
        elapsed_timeDicho = end_timeDicho - start_timeDicho
        print(f"Tempo di esecuzione: {elapsed_timeDicho:.6f} secondi")



        print("\nFINE\n")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text
