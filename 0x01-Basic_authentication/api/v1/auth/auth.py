#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""manage API authentication"""
from flask import request
from typing import List, TypeVar


class Auth(object):
    """manage API authentication"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require authentication"""
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path[-1] != '/':
            path += '/'
        if path in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None