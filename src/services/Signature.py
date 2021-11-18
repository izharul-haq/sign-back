from typing import Union

from utils import dsa, rsa
from type_aliases import dsign, key


def create_key(algo: str, **kwargs) -> (key, key):
    '''Generate both public and private keys used in
    creating signature.'''

    if algo == 'rsa':
        p: int = kwargs['p']
        q: int = kwargs['q']
        e: int = kwargs['e']

        return rsa.generate_key(p, q, e)

    else:   # algo == 'dsa'
        p: int = kwargs['p']
        q: int = kwargs['q']
        x: int = kwargs['x']

        return dsa.generate_key(p, q, x)


def sign(algo: str, message: int, **kwargs) -> str:
    '''Generate a digital signature using
    given algorithm and parameters.'''

    signature: int = None

    if algo == 'rsa':
        d: int = kwargs['d']
        n: int = kwargs['n']

        signature = rsa.sign(message, d, n)

    else:   # algo == 'dsa'
        p: int = kwargs['p']
        q: int = kwargs['q']
        x: int = kwargs['x']

        signature = dsa.sign(message, x, p, q)

    return hex(signature)[2:].upper()


def verify(algo: str, message: int, sign: dsign, **kwargs) -> bool:
    '''Verify wether given signature is valid
    for given message using given algorithm and
    parameters.'''

    is_valid: bool = None

    if algo == 'rsa':
        e: int = kwargs['e']
        n: int = kwargs['n']

        is_valid = rsa.verify(message, sign, e, n)

    else:   # algo == 'dsa'
        p: int = kwargs['p']
        q: int = kwargs['q']
        g: int = kwargs['g']
        y: int = kwargs['y']

        is_valid = dsa.verify(message, sign, p, q, g, y)

    return is_valid
