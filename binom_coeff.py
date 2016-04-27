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
    res = 1
    for i in range(1, k + 1):
        res *= (n + 1 - i)/i

    return res
