import pytest
import caesar
import affine

def test_caesar_encrypt_decrypt():
    plaintext = "hello world!!"
    key = 3
    encrypted = caesar.caesarEncrypt(plaintext, key)
    decrypted = caesar.caesarDecrypt(encrypted, key)
    assert decrypted == plaintext

def test_caesar_encrypt_lowercase():
    assert caesar.caesarEncrypt("abc", 1) == "bcd"

def test_caesar_encrypt_uppercase():
    assert caesar.caesarEncrypt("XYZ", 2) == "ZAB"

def test_caesar_encrypt_nonalpha():
    assert caesar.caesarEncrypt("123!", 5) == "123!"
