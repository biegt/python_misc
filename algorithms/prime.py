def find_primes(n):
    """Function that finds all prime numbers up to a given number (n). Algorithm used is the the sieve of Eratosthenes."""
    is_prime = [True] * (n - 1)
    current_prime = 2

    while True:
        multiplier = 2
        multiple = current_prime * multiplier

        while multiple <= n:
            is_prime[multiple - 2] = False
            multiplier += 1
            multiple = current_prime * multiplier

        for i, prime in enumerate(is_prime):
            if prime and i + 2 > current_prime:
                current_prime = i + 2
                break
        else:
            break
    
    prime_list = [] * sum(is_prime)
    for i, prime in enumerate(is_prime):
        if prime: prime_list.append(i + 2)
    
    return prime_list
