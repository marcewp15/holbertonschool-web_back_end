#!/usr/bin/env python3
""" Module: Redis Server, use redis for basic operations,
    to use redis as a simple cache"""
import redis
import uuid
from typing import Union


class Cache:
    """Class: Cache"""
    def __init__(self):
        """ Method: Constructor Cache, initialize REDIS and flush the
        instance using flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method: should generate a random key with uuid4() and
        set in redis key: value and return the key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key