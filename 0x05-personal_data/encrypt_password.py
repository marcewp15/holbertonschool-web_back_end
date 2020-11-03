#!/usr/bin/env python3
""" Encript password """
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash password: returns a salted, hashed password, which is a byte string
    """
    pswd = password.encode()
    hashed = bcrypt.hashpw(pswd, bcrypt.gensalt())

    return hashed
