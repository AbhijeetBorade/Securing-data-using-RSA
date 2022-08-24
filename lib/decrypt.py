
from lib.generate_primes import get_prime
from lib.utils import phi, convert_from_ascii, mod_inv
from settings import KEY_BIT_SIZE, E


def decrypt(cipher: int, private_key: int, p: int, q: int, mod: int) -> int:
    return pow(cipher, (private_key % phi(p, q)), mod)


def get_original_message(
    message: str | list[int], private_key: int, p: int, q: int, n: int
) -> list[str]:
    if isinstance(message, str):
        message_list = message.replace("[", "").replace("]", "").split(",")

        message_list = [int(i) for i in message_list]
        
        return convert_from_ascii(
            [decrypt(i, private_key, p, q, n) for i in message_list]
        )

    decipher_text = convert_from_ascii(
        [int(decrypt(i, private_key, p, q, n)) for i in message]
    )

    return decipher_text


def get_keys(key_size: int = KEY_BIT_SIZE, e: int = E) -> tuple[int, int, int]:
    p = get_prime(bit_size=key_size / 2)

    q = get_prime(bit_size=key_size / 2)

    if p == q:
        return get_keys(key_size, e)

    private_key = mod_inv(e, phi(p, q))

    return p, q, private_key
