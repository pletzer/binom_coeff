# binom_coeff

A small code example showing how to compute the binomial coefficient in Python

To test: 

```python

from binom_coeff import binom_coeff

# Choose 54 out of 100
n = 100
k = 54
coeff = binom_coeff(n, k)
print("""
There are {0} possibilities to choose {1} elements out of a collection of {2}
""".format(coeff, n, k)
```