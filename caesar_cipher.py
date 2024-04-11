def encrypt_caesar(plaintext, shift):
    """
    Encrypts the given plaintext message using the Caesar cipher with the specified shift value.

    :param plaintext: The plaintext message to encrypt.
    :param shift: The shift value to use for encryption.
    :return: The encrypted message.
    """
    encrypted_message = []

    # Iterate through each character in the plaintext
    for char in plaintext:
        if char.isalpha():
            # Determine the alphabet (uppercase or lowercase)
            ascii_offset = ord('A') if char.isupper() else ord('a')

            # Calculate the shifted position in the alphabet
            shifted_position = (ord(char) - ascii_offset + shift) % 26

            # Find the encrypted character and add it to the result
            encrypted_char = chr(shifted_position + ascii_offset)
            encrypted_message.append(encrypted_char)
        else:
            # If the character is not a letter, leave it unchanged
            encrypted_message.append(char)

    # Join the list of characters to form the encrypted message
    return ''.join(encrypted_message)


def decrypt_caesar(ciphertext, shift):
    """
    Decrypts the given ciphertext message using the Caesar cipher with the specified shift value.

    :param ciphertext: The encrypted message to decrypt.
    :param shift: The shift value used for decryption (should be the same as the encryption shift).
    :return: The decrypted message.
    """
    decrypted_message = []

    # Iterate through each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():
            # Determine the alphabet (uppercase or lowercase)
            ascii_offset = ord('A') if char.isupper() else ord('a')

            # Calculate the shifted position in the alphabet (subtracting shift for decryption)
            shifted_position = (ord(char) - ascii_offset - shift) % 26

            # Find the decrypted character and add it to the result
            decrypted_char = chr(shifted_position + ascii_offset)
            decrypted_message.append(decrypted_char)
        else:
            # If the character is not a letter, leave it unchanged
            decrypted_message.append(char)

    # Join the list of characters to form the decrypted message
    return ''.join(decrypted_message)


# Sample usage:
if __name__ == "__main__":
    # Your name
    name = "Jesame Sawan-on"
    # The shift value for encryption and decryption
    shift_value = 3

    # Encrypting the name
    encrypted_name = encrypt_caesar(name, shift_value)
    print(f"Encrypted name: {encrypted_name}")

    # Decrypting the encrypted name
    decrypted_name = decrypt_caesar(encrypted_name, shift_value)
    print(f"Decrypted name: {decrypted_name}")
