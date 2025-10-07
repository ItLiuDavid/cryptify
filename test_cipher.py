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

def test_affine_encrypt_decrypt():
    plaintext = "hello world"
    a, b = 5, 8
    encrypted = affine.affineEncrypt(plaintext, a, b)
    decrypted = affine.affineDecrypt(encrypted, a, b)
    assert decrypted == plaintext

def test_affine_encrypt_uppercase():
    assert affine.affineEncrypt("ABC", 3, 7) == "HKN"

def test_affine_encrypt_nonalpha():
    assert affine.affineEncrypt("123!", 5, 8) == "123!"

def test_affine_invalid_key():
    with pytest.raises(ValueError):
        affine.affineEncrypt("test", 2, 5)  # 2 is not coprime with 26

def test_affine_decrypt_invalid_key():
    with pytest.raises(ValueError):
        affine.affineDecrypt("test", 2, 5)  # 2 is not coprime with 26
