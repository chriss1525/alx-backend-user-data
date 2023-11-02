#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Hashing Passwords """

import bcrypt


def hash_password(password: str) -> bytes:
    """ use bcrypt to hash a password """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
