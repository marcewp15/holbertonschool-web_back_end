#!/usr/bin/env python3
""" Filtered Logger """
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Regex-ing - filter datum returns the log message obsfuscated """

    for field in fields:
        message = re.sub(field + '=.*?' + separator, field + '=' +
                         redaction + separator, message)
    return message
