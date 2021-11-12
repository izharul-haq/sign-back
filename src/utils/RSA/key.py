from math import gcd


def generate_key(p: int, q: int, e: int) -> (dict, dict):
    '''Generate RSA public/private key using given prime numbers p
     and q and initial public key e.

    It's assumed that both p and q are prime while e is less than
    Φ(n) = (p - 1) * (q - 1), may or may not co-prime with Φ(n),
    and greater than one.'''

    n: int = p * q
    toitent: int = (p - 1) * (q - 1)

    step: int = 1 if e < n else -1

    # update e so that e is co-prime with toitent
    for i in range(e, n, step):
        if gcd(toitent, e) == 1:
            break
        else:
            e = i

    d: int = pow(e, -1, toitent)

    e: str = str(e)
    d: str = str(d)
    n: str = str(n)

    pub_key: dict = {'e': e, 'n': n}
    pri_key: dict = {'d': d, 'n': n}

    return pub_key, pri_key
