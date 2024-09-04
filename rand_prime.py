# SOURCE
# https://www.geeksforgeeks.org/how-to-generate-large-prime-numbers-for-rsa-algorithm/
#
# Many thanks to tabmir at GeeksForGeeks for providing this code
# as well as a very well-written explanation of the process.

import random

first_primes_list = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,
        37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
        79, 83, 89, 97, 101, 103, 107, 109, 113,
        127, 131, 137, 139, 149, 151, 157, 163,
        167, 173, 179, 181, 191, 193, 197, 199,
        211, 223, 227, 229, 233, 239, 241, 251,
        257, 263, 269, 271, 277, 281, 283, 293,
        307, 311, 313, 317, 331, 337, 347, 349
    ]

def n_bit_random(n):
    return random.randrange(2**(n-1)+1, 2**n-1)

def get_low_level_prime(n):
    while True:
        pc = n_bit_random(n)

        for divisor in first_primes_list:
            if pc % divisor == 0:
                break
            else:
                return pc

def is_miller_rabin_passed(mrc):
    max_divisions_by_two = 0
    ec = mrc - 1
    while ec % 2 == 0:
        ec >>= 1
        max_divisions_by_two += 1
    assert(2**max_divisions_by_two * ec == mrc - 1)

    def trial_composite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(max_divisions_by_two):
            if pow(round_tester, 2**i * ec, mrc) == mrc - 1:
                return False
        return True

    number_of_rabin_trials = 20
    for i in range(number_of_rabin_trials):
        round_tester = random.randrange(2, mrc)
        if trial_composite(round_tester):
            return False
    return True

def get_prime(n):
    while True:
        prime_candidate = get_low_level_prime(n)
        if not is_miller_rabin_passed(prime_candidate):
            continue
        else:
            return prime_candidate
