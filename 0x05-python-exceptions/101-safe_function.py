#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except Exception as e:
        error_message = "Exception: {}".format(e)
        print(error_message, file=sys.stderr)
        return None
