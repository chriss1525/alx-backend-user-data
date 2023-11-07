#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Implement basic auth
"""

from flask import *
from .auth import Auth


class BasicAuth(Auth) -> Auth:
    """implement basic auth
    """
    pass
