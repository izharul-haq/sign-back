def shift_right(num: int, shift: int, size: int = 32) -> int:
    return (num >> shift) | (num << size - shift)


def sigma0(num: int) -> int:
    return (shift_right(num, 7) ^ shift_right(num, 18) ^ (num >> 3))


def sigma1(num: int) -> int:
    return (shift_right(num, 17) ^ shift_right(num, 19) ^ (num >> 10))


def s0(num: int) -> int:
    return (shift_right(num, 2) ^ shift_right(num, 13) ^ shift_right(num, 22))


def s1(num: int) -> int:
    return (shift_right(num, 6) ^ shift_right(num, 11) ^ shift_right(num, 25))


def choose(E: int, F: int, G: int) -> int:
    return (E & F) ^ (~E & G)


def majority(A: int, B: int, C: int) -> int:
    return (A & B) ^ (A & C) ^ (B & C)
