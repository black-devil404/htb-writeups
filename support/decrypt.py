import base64

key = b"armando"  # XOR key from the binary

# Get encrypted password from user input
enc_password = input("Enter Base64-encoded encrypted password: ")

try:
    # Decode the base64 string
    cipher = base64.b64decode(enc_password)

    # Decrypt using the logic from the binary
    decrypted = bytearray()
    for i in range(len(cipher)):
        decrypted.append(cipher[i] ^ key[i % len(key)] ^ 223)

    # Output the result
    print("Decrypted password:", decrypted.decode('utf-8'))

except Exception as e:
    print("Error:", e)

