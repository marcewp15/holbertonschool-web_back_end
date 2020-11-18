#!/usr/bin/env python3
""" User authentication service """
import bcrypt

def _hash_password(password: str) -> str:
    """ Hash password method """
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed
