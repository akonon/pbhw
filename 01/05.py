#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 5: Name of type
# Take an object and return a string with type of that object:
# typer(777) == "int"
# typer("777") == "str"
# typer(typer) == "function"

def typer(inp):
    return str(type(inp)).split("'")[1]

print typer(777) == 'int'
print typer('777') == 'str'
print typer(typer) == 'function'
