#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Hashing Passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """ use bcrypt to hash a password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ check if a password is valid """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
