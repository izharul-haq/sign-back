def sign(_hash: int, d: int, n: int) -> int:
    '''Generate a signature from given hash
    and private key (d, n) using RSA algorithm.'''

    return pow(_hash, d, n)


def verify(_hash: int, sign: int, e: int, n: int) -> bool:
    '''Verify wether given sign is valid or not
    with given public key (e, n) using RSA algorithm.'''

    signature: int = pow(sign, e, n)

    return signature == _hash
