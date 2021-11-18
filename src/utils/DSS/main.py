from type_aliases import dsign


# TODO : implement sign function using elgamal algorithm.
def sign(_hash: int, x: int, p: int, q: int) -> dsign:
    '''Generate a signature from given hash
    and <key> using DSS algorithm.'''

    pass


# TODO : implement verify function using elgamal algorithm
def verify(_hash: int, sign: dsign, p: int, q: int, g: int, y: int) -> bool:
    '''Verify wether given sign (r, s) is valid or not
    with given public key (g, y, p, q) using DSS
    algorithm.'''

    pass
