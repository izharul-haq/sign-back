from hashlib import sha256


# TODO : implement hash generator using SHA algorithm from scratch
def generate_hash(message: bytes) -> int:
    '''Generate hash value from given message.'''

    return int.from_bytes(sha256(message).digest(), byteorder='big')
