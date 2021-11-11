from utils import rsa
from utils import elg


# TODO : implement generate key using elgamal algorithm
def generate_key(algo: str, **kwargs) -> (dict, dict):
    '''Generate both public and private keys used in
    creating signature.'''

    if algo == 'rsa':
        p: int = kwargs['p']
        q: int = kwargs['q']
        e: int = kwargs['e']

        return rsa.generate_key(p, q, e)

    else:   # algo == 'elg'
        pass
