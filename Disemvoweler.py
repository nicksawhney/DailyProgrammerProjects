word = input()
def disemvowel(word):
    tup = ("a", "e", "i", "o", "u", " ")
    new_word = ""
    for x in word:
        if x not in tup:
            new_word += x
    return new_word

print (disemvowel(word))
