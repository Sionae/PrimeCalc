def PrimeC(N, l):
    """Checks if a number is prime or not"""

    for prime in l:
        if N % prime == 0:
            return False

    return True
