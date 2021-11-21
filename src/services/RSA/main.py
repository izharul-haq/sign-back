from type_aliases import dsign


def sign(digest: int, d: int, n: int) -> dsign:
    '''Generate a signature from given hash
    and private key (d, n) using RSA algorithm.'''

    return pow(digest, d, n)


def verify(digest: int, sign: dsign, e: int, n: int) -> bool:
    '''Verify whether given sign is valid or not
    with given public key (e, n) using RSA algorithm.'''

    signature: int = pow(sign, e, n)

    return signature == (digest % n)
