from type_aliases import dsign


# TODO : implement sign function using DSA algorithm.
def sign(_hash: int, p: int, q: int, g: int, x: int) -> dsign:
    '''Generate a signature from given hash
    and private key (p, q, g, x) using DSA
    algorithm.'''

    pass


# TODO : implement verify function using DSA algorithm
def verify(_hash: int, sign: dsign, p: int, q: int, g: int, y: int) -> bool:
    '''Verify wether given sign (r, s) is 
    valid or not with given public key
    (p, q, g, y) using DSA algorithm.'''

    pass
