from random import randint

from type_aliases import dsign


def sign(digest: int, p: int, q: int, g: int, x: int) -> dsign:
    '''Generate a signature from given hash,
    and private key (p, q, g, x) using DSA
    algorithm.'''

    k = randint(1, q - 1)

    r = pow(g, k, p) % q
    s = (pow(k, -1, q) * ((digest + (x * r)) % q)) % q

    return r, s


def verify(digest: int, sign: dsign, p: int, q: int, g: int, y: int) -> bool:
    '''Verify whether given sign (r, s) is 
    valid or not with given public key
    (p, q, g, y) using DSA algorithm.'''

    r, s = sign

    w = pow(s, -1, q)
    u1 = (digest * w) % q
    u2 = (r * w) % q
    v = ((pow(g, u1, p) * pow(y, u2, p)) % p) % q

    return v == r
