from type_aliases import dsign


def sign(_hash: int, d: int, n: int) -> dsign:
    '''Generate a signature from given hash
    and private key (d, n) using RSA algorithm.'''

    return pow(_hash, d, n)


def verify(_hash: int, sign: dsign, e: int, n: int) -> bool:
    '''Verify whether given sign is valid or not
    with given public key (e, n) using RSA algorithm.'''

    signature: int = pow(sign, e, n)

    return signature == (_hash % n)
