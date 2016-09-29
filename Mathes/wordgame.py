with open('words.txt') as f:
    words = f.readlines()

words = [word.strip().lower() for word in words]

include = list('barx')
exclude = list('eghilmnostuw')

def check(word):
    for char in include:
        if char not in word:
            return False
    for char in exclude:
        if char in word:
            return False
    return True

for word in words:
    if len(word) == 5:
        chars = list(word)
        if check(word):
            print word
