#!/usr/bin/env python3
""" Manage the API authentication """
from api.v1.auth.auth import Auth
from base64 import b64decode


class BasicAuth(Auth):
    """ BasicAuth class """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """ extract_base64_authorization: returns the Base64 part of the
        Authorization header for a Basic Authentication: """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if authorization_header.startswith('Basic ') is False:
            return None

        return authorization_header[6:]

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """ decode_base64_authorization_header: returns the decoded value of a
        Base64 string base64_authorization_header """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            data_to_decode = b64decode(
                base64_authorization_header.encode('utf-8'))
        except BaseException:
            return None
        return data_to_decode.decode('utf-8')

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """ extract_user_credentials: returns the user email and password
        from the Base64 decoded value """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if decoded_base64_authorization_header.find(':') == -1:
            return None, None
        decoded = decoded_base64_authorization_header.split(':')
        return (decoded[0], decoded[1])

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """ user_object_from_credential: returns the User instance
        based on his email and password """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            find_user = User.search({'email': user_email})
            for user in find_user:
                if user.is_valid_password(user_pwd):
                    return user
        except Exception:
            return None
