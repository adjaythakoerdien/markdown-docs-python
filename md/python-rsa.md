# Python Rsa Encrypt And Decrypt Messages 

```python
# python

import rsa

def create_rsa_keys():
    public_key, private_key = rsa.newkeys(2048)
    with open("public.pem", "wb") as file:
        file.write(public_key.save_pkcs1("PEM"))

    with open("private.pem", "wb") as file:
        file.write(private_key.save_pkcs1("PEM"))


def load_keys():
    with open("public.pem", "rb") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())

    with open("private.pem", "rb") as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    return public_key, private_key


def encrypt(message: str, public_key) -> bytes:
    message_encrypted = rsa.encrypt(message.encode(), public_key)
    return message_encrypted


def decrypt(message: bytes, private_key) -> str:
    message_decrypted = rsa.decrypt(message, private_key).decode()
    return message_decrypted


def main():
    create_rsa_keys()
    public, private = load_keys()
    message = "TEEEEEST message"
    encrypted = encrypt(message, public)

    with open("encrypted.txt", "wb") as f:
        f.write(encrypted)

    with open("encrypted.txt", "rb") as f:
        msg = decrypt(f.read(), private)

    print(msg)


if __name__ == "__main__":
    main()
```

### Resource
-

