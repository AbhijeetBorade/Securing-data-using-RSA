
from lib.decrypt import get_original_message, get_keys
from lib.encrypt import encrypt
from settings import E


def run_test(key_size: int, e: int, sample_message: str) -> tuple[str, int, int, int]:
    p, q, private_key = get_keys(key_size=key_size, e=e)
    n = p * q

    encrypted_message = encrypt(sample_message, e, n)

    decrypted_message = get_original_message(encrypted_message, private_key, p, q, n)

    return "".join(decrypted_message), p, q, private_key


def run_series_test(
    iterations: int,
    starting_key_size: int = 8,
    e: int = E,
    sample_message: str = "Hello, world!",
) -> None:
    current_key_size = starting_key_size

    for i in range(iterations):
        test_output, p, q, private_key = run_test(current_key_size, e, sample_message)

        if test_output == "Hello, world!":
            print(
                f"Test #{i + 1}: Passed - key_size={current_key_size}"
            )
        else:
            print(
                f"Test #{i + 1}: Failed - key_size={current_key_size}"
            )

        current_key_size *= 2


if __name__ == "__main__":
    run_series_test(8)
