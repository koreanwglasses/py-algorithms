import gmpy2
from gmpy2 import mpz
from PIL import Image

length = 100000                                     # Number of primes to plot
primes = [mpz(2)]                               # Init list of primes
for _ in range(length - 1):
    primes.append(gmpy2.next_prime(primes[-1])) # Add next prime to list

width = primes[-1].num_digits(2)           # Calculate total width

binary = []                                     # Initialize binary array
for p in primes:
    row = ['0' for _ in range(width - p.num_digits(2))] + list(p.digits(2))
    binary.append(row)

bitmap = Image.new('RGB', (width, length), 'white')
pixels = bitmap.load()

for r in range(length):
    for c in range(width):
        pixels[c,r] = (255,255,255) if binary[r][c] == '0' else (0,0,0)

bitmap.save('images/primes_'+str(length)+'.png', 'PNG')

