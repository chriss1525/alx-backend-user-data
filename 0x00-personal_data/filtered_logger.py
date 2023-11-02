#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""return the log message obfuscated"""
import re
from typing import List
import logging
import mysql.connector
import os


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """returns the log message obfuscated"""
    for i in fields:
        message = re.sub(i + "=.*?" + separator,
                         i + "=" + redaction + separator, message)
    return message
