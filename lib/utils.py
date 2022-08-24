


from tokenize import Double


def phi(x: int, y: int) -> int:
    return (x - 1) * (y - 1)


def egcd(a, b) -> tuple[int, int, int]:
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


def mod_inv(a: int, m: int) -> int | None:
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None
    else:
        return x % m


def convert_to_ascii(message: str) -> list[int]:
    final_message = []

    for i in range(len(message)):
        final_message.append(int(ord(message[i])))

    return final_message


def convert_from_ascii(message: list) -> list[str]:
    return list(map(lambda x: chr(int(x)), message))
