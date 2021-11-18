from type_aliases import key


# TODO : implement key generator for DSA algorithm
def generate_key(p: int, q: int, x: int) -> (key, key):
    '''Generate DSA public/private key using given prime
     numbers p and q and private key x.

    It's assumed that q is prime and a factor of (p - 1) while
    x is a random integer less than q.'''

    pass
