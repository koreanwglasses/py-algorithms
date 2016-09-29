import random

cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
cons_ex_b = ['bl', 'br', 'ch', 'ck', 'cl', 'cr', 'dr', 'fl', 'fr', 'gh', 'gl', 'gr', 'ph', 'pl', 'pr', 'qu', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn', 'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr', 'sch', 'scr', 'shr', 'spl', 'spr', 'squ', 'str', 'thr']
cons_ex_f = ['st', 'sk', 'sp', 'nd', 'ng', 'nt', 'nk', 'mp', 'rd', 'ld', 'lp', 'rk', 'lt', 'lf', 'pt', 'ft', 'ct', 'nth']
vows = ['a', 'e', 'i', 'o', 'u']
vows_ex = ['ai', 'au', 'aw', 'ay', 'ea', 'ee', 'ei', 'eu', 'ew', 'ey', 'ie', 'oi', 'oo', 'ou', 'ow', 'oy']

def simp_pronounceable(length):
    word = ''
    for _ in range(length):
        word += random.choice(cons) + random.choice(vows)
    return word

def syllable():
    return random.choice(cons + cons_ex_b) + random.choice(vows + vows_ex) + random.choice(cons + cons_ex_f)

print((len(cons) + len(cons_ex_b)) * (len(vows) + len(vows_ex)) * (len(cons) + len(cons_ex_f)))
while True:
    input()
    words = [syllable() for _ in range(10)]
    print(' '.join(words))