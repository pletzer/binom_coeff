def binom_coeff(n, k):
    """
    Compute the binomial coefficient
    Input:
    n number of values to choose from
    k number of values to choose
        
    Return:
    number of possibilities to choose k from n
    """
    
    # Only one possibility
    if k == 0 or k == n:
        return 1
    
    # See https://en.wikipedia.org/wiki/Binomial_coefficient#Combinatorics_and_statistics
    # making sure the result is an integer
    num = 1
    denom = 1
    for i in range(1, k + 1):
        num *= (n + 1 - i)
        denom *= i

    # integer division
    return num // denom
