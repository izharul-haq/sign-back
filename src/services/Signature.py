from utils import elg, rsa


def generate_key(algo: str, **kwargs) -> (dict, dict):
    '''Generate both public and private keys used in
    creating signature.'''

    if algo == 'rsa':
        p: int = kwargs['p']
        q: int = kwargs['q']
        e: int = kwargs['e']

        return rsa.generate_key(p, q, e)

    else:   # algo == 'elg'
        p: int = kwargs['p']
        q: int = kwargs['q']
        x: int = kwargs['x']

        return elg.generate_key(p, q, x)


# TODO : implement signature generator using elgamal algorithm
def sign(algo: str, message: int, **kwargs) -> str:
    '''Generate a digital signature using
    given algorithm and parameters.'''

    signature: int = None

    if algo == 'rsa':
        d: int = kwargs['d']
        n: int = kwargs['n']

        signature = rsa.sign(message, d, n)

    else:   # algo == 'elg'
        pass

    return hex(signature)[2:].upper()


# TODO : implement verify signature using elgamal algorithm
def verify(algo: str, message: int, sign: int, **kwargs) -> bool:
    '''Verify wethet given signature is valid
    for given message using given algorithm and
    parameters.'''

    is_valid: bool = None

    if algo == 'rsa':
        e: int = kwargs['e']
        n: int = kwargs['n']

        is_valid = rsa.verify(message, sign, e, n)

    else:   # algo == 'elg'
        pass

    return is_valid
