from rand_prime import getPrime
from extended_euclidean import eEuclidean


def choosePQ(n_bits):
    return (getPrime(n_bits), getPrime(n_bits))

def phi_func(p, q):
    return (p - 1) * (q - 1)

def main():
    p, q = choosePQ(1024)
    n = p * q
    phi = phi_func(p, q)

    e = 65537

    message = 1234

    print(f'Message: {message}')

    encrypted = pow(message, e, n)

    print(f'Encrypted: {hex(encrypted)}')

    d = eEuclidean(phi, e)
    decrypted = pow(encrypted, d, n)

    print(f'Decrypted: {decrypted}')

if __name__=="__main__":
    main()
