from type_aliases import dsign
from random import randint

def sign(_hash: int, p: int, q: int, g: int, x: int) -> dsign:
    '''Generate a signature from given hash,
    and private key (p, q, g) using DSA algorithm.'''

    k = randint(1, q-1)

    r = pow(pow(g,k,p),1,q)
    s = pow((pow(k, -1, q)*(_hash + (x*r))),1,q)
    
    return r,s

def verify(_hash: int, sign: dsign, p: int, q: int, g: int, y: int) -> bool:
    '''Verify wether given sign (r, s) is 
    valid or not with given public key
    (p, q, g, y) using DSA algorithm.'''
    
    s_inv = pow(sign[1], -1, q)
    w = pow(s_inv,1,q)

    u1 = (_hash*w) % q
    u2 = (sign[0]*w) % q
    v = ((g**u1*y**u2) % p) % q

    return v == sign[0]