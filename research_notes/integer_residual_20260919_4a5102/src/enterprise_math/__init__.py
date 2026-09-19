"""Isolated validation harness: not a replacement for the upstream package init.

Only exact_arithmetic.py, core.py and division.py are vendored, byte-for-byte.
The upstream __init__.py imports other modules not included in this small bundle.
"""
