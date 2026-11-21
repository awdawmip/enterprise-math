#!/usr/bin/env python3
"""Exact integer certificate for CBRC F7 homogeneous-mark B=10 half-defect."""
from base64 import b64decode
from hashlib import sha256
from itertools import product
from math import gcd
from zlib import decompress

TABLE_ZLIB_BASE64 = """eNo9l1GS7SgMQzfErQo2BKje/746tnX4GemBLMvchPR4+1nbf95+vfXnQ0EsjvbztgJycTRBLM72GwX+KWe4fHtT0tkEWi1NFLztNwtS8TZBLK72ewv0r/GVrejwSZZaLFWuJtCqRFUy879htttvFcTaltmWyW4CrZYmCk7Vnao7keVTHIU4qj9NoFWJqiTq+1M+gdkjSBcB2Uhhb78j3ML12QW+wpn6rkxBHGKQLgKygZJSvOStVuqcQUwBjMaGuzWQjRTGs9SjMsgjcoRbipUVHkOJTMiAOMQgXQRkAyWleGFON3U/BYSrtIPYI9LuxPIZROFN6HoV+mhsoFRlOcXr4BBWdionRzAZmHeo8xJ1vUVdr1GfDSWleGFe3V7avrR9NdJL15fZXmbLNzIlApbRUSijjjo7xVs5IQNytwySRSufiyInXRfHsgi4eDIWSRcHxY3QV91d6Vco0CoqyvDBmE60JgvhSNvlxzwMWBNvBt3Mtxlikz3vm5QIWEZHYTnF9fJCJmRAriZzHdqePNbwO5zr4VwPkQ7nesh26p4NdKHRoFCgVYlUgwemdKEtOW4yshK+y4/xmDcPwOK2XJBQJukiaW6PZrOnvlf2NAHL6CjEqaw7PbqOPUlKejaL4s7hWteZWq9vg/X6FFpvAq2iunXXCnO6VXsjh+lXT5JSY1Zdxmb1jTRrAq2ioqxPYRrHDXogG3K3XkgWeT5yIg7Jm8j8novfc3Ey6pY3V1avz7q5MnsTaFUi1eBxXW+j25s0xCNvf4WaiBFr5sHwg5lHDhae484z6nv9oeCuX2nPwEO2cW13kbtSnSeNZh7uLjIg5Tfvoc4bYtZ1bbP+BrCpULMJtCrRrbpG15tutK/ssxGQxDXCyywvs7w5wi4yIV1EEgHL6CjEqazj0jbII1KSRbPFedXXJEZZ98D4jNjSnxe22kVtXOmtxo8GdCRCZfruaXORnqe7ybTzAMJs8z5sfV5tt4vauFKKcSv7Q5/DaRyO/uSx7CRVdPJ5ElmQvHDt3FSHR+sQ7+jDa4ecp13UBkpKr9n1pyMRyFQHdxqpGSPn8kcDBskKfxTeH33B/GkXtYGySuPP2QG5KwaJnzrJI1LVXaflnYZdT1OSCcG5y/miNlBSihfmdKM9eQhI4hrhu6/j7S3ikCwxkhuBuf/d2kVtoKQUrzJ3ujhdnPNxujhduPHd20VtoKQ0bufENP+uSDuQu+KQTDZoNxrIRpmNa1ZecY2+kAFJ6cxfvUiZccM6N6zPdlEbKCnFy4Ywu8Wfv13kC/IWmaxkDZeh6yr7kA2bwixdHEyQBXkhE5IJFvZ1Iaq8s/JI3GUIsoGSUrwwr2QrxixUngq4GXuTdGfAXcTDM++qQm2grNK4qDYkFdxqzi1wGhupHPEHmkO+/+dMkomSxNP3kYvaQFmlXdGDlKJnkF1kQd4o6jr2wRXyERZQUIIHptXFsssOUhvx/6UGifcjSEk8g7xFVmkuagOlP7VeXoOhhh7DMRro8UsHZu6JcjL+bGApZ3h+lfFoZ8nLYb/tYm6sVLxFBivGSi9S7qvxbwTuQlWWVTxZOfLGfN+d2jg8BKd+0clTMfUTT0uP9296kX/e/6qn"""
TABLE_SHA256 = "aaccfb63cc2e12e9f2d4de2ac7c16370caac90c503cc574088c866faca7a26c1"

def coefficient_table():
    raw = decompress(b64decode(TABLE_ZLIB_BASE64))
    assert sha256(raw).hexdigest() == TABLE_SHA256
    rows = [tuple(map(int, x.split(","))) for x in raw.decode("ascii").split(";")]
    assert len(rows) == 574
    table = {(a, b): v for a, b, v in rows}
    assert len(table) == 574
    assert all(b != 0 and gcd(a, abs(b)) == 1 and v in (6, 7, 8, 10)
               for (a, b), v in table.items())
    assert (2, 1) not in table and (1, -1) not in table
    return table

def q10(x, y, table):
    """Value of 10*q(x,y) on the entire integer plane."""
    if x == 0 and y == 0:
        return 0
    if y == 0:
        return 10
    g = gcd(abs(x), abs(y))
    return table.get((abs(x)//g, y//g), 5)

def defect10(z, table):
    a, b, c, d = z
    t = a - 2*b - c + 2*d
    return q10(a+t, b+t, table) + q10(c-t, d-t, table) - q10(a, b, table) - q10(c, d, table)

def check():
    table = coefficient_table()
    maximum, count, count_max, witness = 0, 0, 0, None
    for z in product(range(-10, 11), repeat=4):
        d = abs(defect10(z, table))
        count += 1
        if d > maximum:
            maximum, witness, count_max = d, z, 1
        elif d == maximum:
            count_max += 1
        assert d <= 5, (z, d)
    assert count == 21**4 == 194481
    assert maximum == 5
    assert count_max == 38042
    assert abs(defect10((1, -1, 0, 0), table)) == 5
    assert q10(2, 1, table) == q10(-1, -1, table) == 5
    print(f"PASS: B=10, inputs={count}, distinct_exception_rays={len(table)}, "
          f"max_abs_defect={maximum}/10, equality_count={count_max}, witness={witness}")

if __name__ == "__main__":
    check()
