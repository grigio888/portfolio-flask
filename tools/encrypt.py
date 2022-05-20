import cryptography.fernet as fernet

def encoder_token(action, arg):
    """
    Responsavel por encryptar e desencriptar o Token.
    """
    encoder_key = b'3K5oiOzfV4NU6mdzDeNubuvaT8sFKQAuc7NvbWOjTeo='

    if action == 'encript':
        encryption = fernet.Fernet(encoder_key)
        pre_token = arg
        encrypted = encryption.encrypt(pre_token.encode())

        return encrypted.decode('ascii')

    if action == 'decript':
        encryption = fernet.Fernet(encoder_key)
        pre_token = arg.encode('ascii')
        byte_token = bytes(pre_token)
        decrypted = encryption.decrypt(byte_token).decode()

        return decrypted


if __name__ == '__main__':

    test = 'grigio888-12345678'

    input = encoder_token('encript', test)
    print(input)
    output = encoder_token('decript', 'gAAAAABh0gPiZmk7QNs2W_whQAACh1MDLW0UhfQu_3TypCvUfYCfdyMYDN0RCGsmDWzmZhaQN9D6plOhigrS4fiLIaUd3rhshkd1iO317T3x4fhKTZQAXSc=')
    print(output)