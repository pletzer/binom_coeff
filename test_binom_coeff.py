import sys
from binom_coeff import binom_coeff

if len(sys.argv) < 3:
    print('Need at least 2 arguments')
    print('Usage: {} n k'.format(sys.argv[0]))
    print('choose "k" out of "k"')
    sys.exit(1)

n = sys.argv[1]
k = sys.argv[2]

coeff = binom_coeff(n, k)

print("""
There are {0} possibilities to choose {1} elements out of a collection of {2}
""".format(coeff, n, k)

