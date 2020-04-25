import lib

def enc_dec(text, key):
    enc_dec_text = ""
    for encrypt in range(0, len(text)):
        enc_dec_text = enc_dec_text + chr(lib.to_dec(lib.xor(ord(text[encrypt]), key)))
    return enc_dec_text
