
from lib.encrypt import encrypt
from settings import E


e = E

n = 1001

message = str(input("Enter message: "))

cipher_text = encrypt(message, e, n)

if __name__ == "__main__":
    print(cipher_text)
