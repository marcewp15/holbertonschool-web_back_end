#!/usr/bin/env python3
""" Manage the Session authentication """
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ Session Authentication """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Creates a Session ID for user_id """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        session_id = str(uuid.uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id
