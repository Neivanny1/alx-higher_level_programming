#!/usr/bin/python3
"""
Class MyInt that inherits from int
"""


class MyInt(int):
    """overrrides =="""
    def __eq__(self, other):
        return super().__ne__(other)
    """overrides =!"""
    def __ne__(self, other):
        return super().__eq__(other)
