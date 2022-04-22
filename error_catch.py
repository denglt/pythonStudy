#!/usr/bin/python3
import traceback

from collections import namedtuple

def try_exception(num):
    try:
        return int(num)
    except Exception as err:
        traceback.print_exc()
        print(err)
    else:
        print("this is a number inputs")


try_exception("abv")
