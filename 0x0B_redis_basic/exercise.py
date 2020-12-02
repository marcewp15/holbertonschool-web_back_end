#!/usr/bin/env python3
""" Module: Redis Server, use redis for basic operations,
    to use redis as a simple cache"""
import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """ Class: Cache"""
    def __init__(self):
        """ Method: Constructor Cache, initialize REDIS and flush the
            instance using flushdb"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method: should generate a random key with uuid4() and
            set in redis key: value and return the key"""
        mykey = str(uuid.uuid4())
        self._redis.set(mykey, data)
        return mykey

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Method: This callable will be used to convert the data
        back to the desired format."""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Method: Return Get Str in data"""
        data = self._redis.get(key)
        return data.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Method: Return Get Int in data"""
        data = self._redis.get(key)
        try:
            return int(data.decode("utf-8"))
        except Exception:
            return 0