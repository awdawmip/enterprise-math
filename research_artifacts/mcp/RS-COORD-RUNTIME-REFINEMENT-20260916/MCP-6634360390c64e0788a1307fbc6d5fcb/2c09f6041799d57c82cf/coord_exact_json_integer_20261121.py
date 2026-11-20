"""Proposed exact JSON integer paths for a registered, validated Cell slice.
No global interpreter decimal-digit setting; integration is not yet performed.
"""
import json
import sys
BASE = 10**9

def parse_int_exact(lexeme: str) -> int:
    sign = -1 if lexeme.startswith('-') else 1
    digits = lexeme[1:] if sign == -1 else lexeme
    if not digits or any(c not in '0123456789' for c in digits):
        raise ValueError('INVALID_INTEGER_LEXEME')
    n = 0
    first = len(digits) % 9 or 9
    j = 0
    for width in [first] + [9] * ((len(digits) - first) // 9):
        part = digits[j:j+width]
        n = n * (10**width) + int(part)
        j += width
    return sign*n

def decimal_exact(num: int) -> str:
    if type(num) is not int:
        raise TypeError('INTEGER_REQUIRED')
    if num == 0: return '0'
    sign = '-' if num < 0 else ''
    n = abs(num)
    chunks = []
    while n:
        n, r = divmod(n, BASE)
        chunks.append(r)
    return sign + str(chunks[-1]) + ''.join(str(x).zfill(9) for x in reversed(chunks[:-1]))

def exact_from_json(source: str, cls):
    def pairs(items):
        record = {}
        for key, val in items:
            if key in record: raise ValueError('DUPLICATE_JSON_KEY')
            record[key] = val
        return record
    def reject(_): raise ValueError('NON_INTEGER_JSON_NUMBER')
    return cls.from_wire(json.loads(source, object_pairs_hook=pairs,
        parse_int=parse_int_exact, parse_float=reject, parse_constant=reject))

def exact_to_json(valid_address, SCHEMA: str) -> str:
    # Only call on an already type-validated registered FinalCellAddress.
    return ('{"codec":' + json.dumps(valid_address.codec)
        + ',"coordinates":[' + ','.join(decimal_exact(v) for v in valid_address.coordinates)
        + '],"frame":' + json.dumps(valid_address.frame)
        + ',"schema":' + json.dumps(SCHEMA)
        + ',"version":' + decimal_exact(valid_address.version) + '}')

def test_local():
    assert decimal_exact(0) == '0'
    for i in range(-10000,10001,97): assert parse_int_exact(decimal_exact(i)) == i
    L=sys.get_int_max_str_digits() if hasattr(sys,'get_int_max_str_digits') else 0
    L=max(L+1,4301)
    dec='1'+'0'*L
    number=10**L
    assert parse_int_exact(dec) == number
    assert decimal_exact(number) == dec
    class MinimalAddress:
        @staticmethod
        def from_wire(record):
            assert record['coordinates'] == [0,number,1,0,0,0]
            return record
    wire='{"schema":"EM_CELL_ADDRESS_V1","codec":"three_region_slice_v1","version":1,"frame":"X6_FIXED_E1_E2_CHART","coordinates":[0,'+dec+',1,0,0,0]}'
    assert exact_from_json(wire, MinimalAddress)['coordinates'][1] == number
    obj=type('Address',(),{'codec':'three_region_slice_v1','frame':'X6_FIXED_E1_E2_CHART','version':1,'coordinates':(0,number,1,0,0,0)})()
    wire2=exact_to_json(obj,'EM_CELL_ADDRESS_V1')
    assert exact_from_json(wire2, MinimalAddress)['coordinates'][1] == number
    for bad in ('{"a":1,"a":2}', '{"coordinates":[0,1.0]}'):
        try: exact_from_json(bad,MinimalAddress)
        except ValueError: pass
        else: raise AssertionError(bad)
    print('PASS: positive/negative exact arithmetic, default-limit-bypassing parse and emit, duplicate/fraction rejection; decimal digits=',L+1)

if __name__=='__main__':test_local()
