#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Implement basic auth"""

from flask import *
from functools import wraps
from .auth import Auth

class BasicAuth(Auth):
    """implement basic auth
    """
    pass
