from rand_prime import get_prime
from extended_euclidean import extended_euclidean

def choose_pq(n_bits):
    return (get_prime(n_bits), get_prime(n_bits))

def totient(p, q):
    return (p - 1) * (q - 1)

def main():
    # Randomly select two 1024-bit prime numbers, calculate n and phi.
    p, q = choose_pq(1024)
    n = p * q
    phi = totient(p, q)

    # Select public key "e", where 1 <= e < phi and e is prime.
    # 65537 is commonly used.
    e = 65537

    # Specify example message.
    message = 1234
    print(f'Message: {message}')

    # Encrypt message with public key.
    encrypted = pow(message, e, n)
    print(f'Encrypted: {hex(encrypted)}')

    # Find private key "d" by getting the modular multiplicative inverse of e.
    d = extended_euclidean(phi, e)

    # Decrypt encrypted message with private key.
    decrypted = pow(encrypted, d, n)
    print(f'Decrypted: {decrypted}')

if __name__ == "__main__":
    main()
