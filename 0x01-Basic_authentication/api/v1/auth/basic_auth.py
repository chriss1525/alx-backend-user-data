#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Implement basic auth
"""

from .auth import Auth


class BasicAuth(Auth):
    """implement basic auth
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """extract base64 authorization header
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """decode base64 authorization header
        """
        if base64_authorization_header == None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            return base64_authorization_header.decode('utf-8')
        except Exception:
            return None

