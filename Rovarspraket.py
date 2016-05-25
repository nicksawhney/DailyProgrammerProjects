shit = str(input("->"))
def killme(word):
    new_word = ""
    for x in word:
        if (x == "a" or x == "e" or x=="i" or x == "u" or x == "o" or x==" "):
            new_word += x
        else:
            new_word += (x + "o" + x)
    return new_word


def longboy(word):
    dam = {"bob": "b", "coc":"c", "dod":"d", "fof":"f", "gog":"g", "hoh": "h", "joj" :"j", "kok" : "k", "lol": "l", "mom" :"m", "pop": "p", "qoq": "q", "ror":"r", "sos":"s", "tot":"t", "vov":"v", "wow":"w", "xox":"x", "yoy":"y", "zoz":"z"}




print (killme(shit))