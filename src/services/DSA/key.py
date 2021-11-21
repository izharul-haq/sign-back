from type_aliases import key

def generate_key(p: int, q: int, x: int) -> (key, key):
    '''Generate DSA public/private key using given prime
     numbers p and q and private key x.

    It's assumed that q is prime and a factor of (p - 1) while
    x is a random integer less than q.'''

    g = pow(100,int((p-1)/q), p)
    y = pow(g,x,p)

    pub_key: key = {'p': p, 'q': q, 'g': g, 'y': y}
    pri_key: key = {'x': x}
    return pub_key, pri_key