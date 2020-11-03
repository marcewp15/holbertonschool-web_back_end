#!/usr/bin/env python3
""" Filtered Logger """
from typing import List
import re
import logging
from os import getenv
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Method Constructor """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Print format record """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ Regex-ing - filter datum returns the log message obsfuscated """

    for field in fields:
        message = re.sub(field + '=.*?' + separator, field + '=' +
                         redaction + separator, message)
    return message


def get_logger() -> logging.Logger:
    """ Get Logger """

    logger = logging.getLogger("user_data")

    logger.setLevel(logging.INFO)

    logger.propagate = False

    sh = logging.StreamHandler()

    sh.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(sh)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Connect to secure database """
    user_name = getenv('PERSONAL_DATA_DB_USERNAME', "root")
    db_pwrd = getenv('PERSONAL_DATA_DB_PASSWORD', "")
    db_host = getenv('PERSONAL_DATA_DB_HOST', "localhost")
    db_name = getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connection.MySQLConnection(user=user_name,
                                                      password=db_pwrd,
                                                      host=db_host,
                                                      database=db_name)
