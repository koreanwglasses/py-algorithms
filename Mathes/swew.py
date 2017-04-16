import random
import re

with open('words.txt') as f:
    words = f.readlines()

words = [word.strip().lower() for word in words]
seed_words = [word for word in words if 3 <= len(word)]

def challenge(words):
    word = random.choice(words)
    regex = re.compile('^'+word[:1]+'.+'+word[1:]+'$')
    solutions = [solution for solution in words if regex.match(solution)]
    return word, solutions

print 'Thinking...'
print

while True:
    word, solutions = challenge(seed_words)
    if len(solutions) > 10:
        print word + ' (' + str(len(solutions)) + ' words)'
        raw_input()
        if len(solutions) <= 15:
            print '\n'.join(solutions)
        else:
            print '\n'.join(sorted(solutions, key=lambda s: -len(s))[:15])
            print '... and ' + str(len(solutions) - 15) + ' more'
        print
        print 'Thinking...'
        print