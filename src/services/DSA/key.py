from random import randint


from type_aliases import key


def generate_key(p: int, q: int, x: int) -> (key, key):
    '''Generate DSA public/private key using given prime
     numbers p and q and private key x.

    It's assumed that q is prime and a factor of (p - 1) while
    x is a random integer less than q.'''

    g = 0
    while g <= 1:
        h = randint(2, p - 2)
        g = pow(h, (p - 1) // q, p)

    y = pow(g, x, p)

    p = str(p)
    q = str(q)
    y = str(y)
    g = str(g)
    x = str(x)

    pub_key: key = {'p': p, 'q': q, 'g': g, 'y': y}
    pri_key: key = {'x': x}

    return pub_key, pri_key
