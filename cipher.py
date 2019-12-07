"""
cipher.py implements CaesarCipher for encrypting and decrypting login password.

The functions below turns each character of the given text
into an ASCII value and then changes the value by the
given key. In this way the text is encrypted and decrypted based
upon the shifting of the characters.
"""


"""enc() encrypts the given plain text using the given key."""
def enc(text, key):
    enc_text = ""
    for itr in range(0, len(text)):
        enc_text = enc_text + chr(ord(text[itr]) + key)
    return enc_text


"""dec() deciphers the encrypted text into plain text if the passed key is correct."""
def dec(text, key):
    dec_text = ""
    for itr in range(0, len(text)):
        dec_text = dec_text + chr(ord(text[itr]) - key)
    return dec_text
