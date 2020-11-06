#!/usr/bin/env python3
""" Manage the API authentication """
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith('Basic ') is False:
            return None

        return authorization_header[6:]
