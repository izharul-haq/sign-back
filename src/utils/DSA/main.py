from type_aliases import dsign


# TODO : implement sign function using DSA algorithm.
def sign(_hash: int, x: int, p: int, q: int) -> dsign:
    '''Generate a signature from given hash
    and <key> using DSA algorithm.'''

    pass


# TODO : implement verify function using DSA algorithm
def verify(_hash: int, sign: dsign, p: int, q: int, g: int, y: int) -> bool:
    '''Verify wether given sign (r, s) is valid or not
    with given public key (g, y, p, q) using DSA
    algorithm.'''

    pass
