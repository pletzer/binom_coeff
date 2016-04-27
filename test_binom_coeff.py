import sys
from binom_coeff import binom_coeff

if len(sys.argv) < 3:
    print('Choose "k" out of "k"')
    print('ERROR: need at least 2 arguments')
    print('Usage: {} n k'.format(sys.argv[0]))
    sys.exit(1)

n = int(sys.argv[1])
k = int(sys.argv[2])

coeff = binom_coeff(n, k)

print("""
{0:10.0f} possibilities to choose {2} elements out of a collection of {1}
""".format(coeff, n, k)
)

