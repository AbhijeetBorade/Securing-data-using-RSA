
from lib.decrypt import get_original_message, get_keys
from settings import E
from lib.encrypt import encrypt

import sys




# elif option == "get_keys":
p, q, private_key = get_keys()

n = p * q

print("--Public Key--")

print(f"n = {n}")
print(f"e = {E}\n")

print("--Private Key--")
print(f"p = {p}")
print(f"q = {q}")
print(f"Private Key = {private_key}")

do_save = True

try:
    if sys.argv[2] == "--nosave":
         do_save = False
except IndexError:
    pass

if do_save:
        keys_file = open("keys.txt", "w")

        keys_file.write("--Public Key--\n")
        keys_file.write(f"n = {n}\n")
        keys_file.write(f"e = {E}\n\n")

        keys_file.write("--Private Key--\n")
        keys_file.write(f"p = {p}\n")
        keys_file.write(f"q = {q}\n")
        keys_file.write(f"Private Key = {private_key}\n")

        keys_file.close()

       #Sender tasks
        e = E

        n = 1001

        message = str(input(" Enter message: "))

        cipher_text = encrypt(message, e, n)

if __name__ == "__main__":
            print(cipher_text)


  
message1 = str(input("Enter Cipher Text: "))

    
private_key = int(input("Enter Private Key: "))

decipher_text = get_original_message(message1, private_key, p, q, n)

print("\nDeciphered Message: " + "".join(decipher_text))

