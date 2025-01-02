def sieve(limit):
    if limit < 2:
        return []

    primes = [False] * (limit + 1)

    if limit >= 2:
        primes[2] = True
    if limit >= 3:
        primes[3] = True

    for x in range(1, int(limit**0.5) + 1):
        for y in range(1, int(limit**0.5) + 1):
            n = 4 * x**2 + y**2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                primes[n] = not primes[n]

            n = 3 * x**2 + y**2
            if n <= limit and n % 12 == 7:
                primes[n] = not primes[n]

            n = 3 * x**2 - y**2
            if x > y and n <= limit and n % 12 == 11:
                primes[n] = not primes[n]

    for n in range(5, int(limit**0.5) + 1):
        if primes[n]:
            for k in range(n**2, limit + 1, n**2):
                primes[k] = False

    primes_list = [n for n in range(limit + 1) if primes[n]]
    return primes_list


def pick_prime(primes, min_size=1000):
    """returns a suitable prime to use as modulus"""
    for prime in primes:
        if prime >= min_size:
            return prime
        
    # if no prime large enough exists, use last one on list
    return primes[-1]


def hash(string, modulus):
    """implements polynomial rolling of string keys"""
    hash_value = 5381
    for char in string:
         # hash = 33 XOR ord(c)
        hash_value = ((hash_value << 5) + hash_value) ^ ord(char)
    
    return hash_value % modulus


if __name__ == '__main__':
    # generate primes list to use as modulus
    primes = sieve(10000)  # modify limit based on your needs
    modulus = pick_prime(primes, 1000)
    test_array = ["alpha", "beta", "gamma", "delta", "epsilon"]

    for string in test_array:
        hash_value = hash(string, modulus)
        print(f"Hash of {string} is {hash_value}")
