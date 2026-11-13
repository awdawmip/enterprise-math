#!/usr/bin/env python3
"""R762P: exact finite verification for optimal coded signed-source BRC observers."""
from itertools import combinations
import json


def source_symbols(law):
    # Four distinct named hidden-source edges of the three-sign cube.
    return tuple(((law >> (2*i)) & 1) + 2*((law >> (2*i+1)) & 1)
                 for i in range(4))


def encode5(x):
    assert len(x) == 4 and all(v in range(4) for v in x)
    return tuple(x) + (x[0] ^ x[1] ^ x[2] ^ x[3],)


def encode7(x):
    assert len(x) == 4 and all(v in range(4) for v in x)
    return tuple(x) + (x[0] ^ x[1] ^ x[3],
                       x[0] ^ x[2] ^ x[3],
                       x[1] ^ x[2] ^ x[3])


H_COLUMNS = ((1,1,0),(1,0,1),(0,1,1),(1,1,1),
             (1,0,0),(0,1,0),(0,0,1))


def syndrome7(y):
    assert len(y) == 7
    return (y[0] ^ y[1] ^ y[3] ^ y[4],
            y[0] ^ y[2] ^ y[3] ^ y[5],
            y[1] ^ y[2] ^ y[3] ^ y[6])


def decode7(y):
    y = list(y)
    syndrome = syndrome7(y)
    if any(syndrome):
        nonzero = set(v for v in syndrome if v)
        if len(nonzero) != 1:
            raise ValueError("not a one-channel error syndrome")
        value = nonzero.pop()
        column = tuple(int(v != 0) for v in syndrome)
        if column not in H_COLUMNS:
            raise ValueError("unrecognized error location")
        index = H_COLUMNS.index(column)
        y[index] ^= value
        assert syndrome7(y) == (0,0,0)
    return tuple(y[:4])


def distance(a, b):
    return sum(x != y for x,y in zip(a,b))


def verify():
    messages = [source_symbols(i) for i in range(256)]
    assert len(set(messages)) == 256
    code5 = [encode5(x) for x in messages]
    code7 = [encode7(x) for x in messages]
    assert len(set(H_COLUMNS)) == 7
    assert all(any(h) for h in H_COLUMNS)
    assert all(syndrome7(y) == (0,0,0) for y in code7)
    d5 = min(distance(a,b) for a,b in combinations(code5,2))
    d7 = min(distance(a,b) for a,b in combinations(code7,2))
    assert (d5,d7) == (2,3)
    tested5 = tested7 = 0
    for i,x in enumerate(messages):
        assert decode7(code7[i]) == x
        for j in range(5):
            for replacement in range(4):
                if replacement == code5[i][j]:
                    continue
                altered = list(code5[i])
                altered[j] = replacement
                assert altered[0] ^ altered[1] ^ altered[2] ^ altered[3] ^ altered[4]
                tested5 += 1
        for j in range(7):
            for replacement in range(4):
                if replacement == code7[i][j]:
                    continue
                altered = list(code7[i])
                altered[j] = replacement
                assert decode7(altered) == x
                tested7 += 1
    assert tested5 == 3840 and tested7 == 5376
    assert 256*(1+6*(4-1)) == 4864 > 4**6 == 4096
    assert 4**3 < 256 == 4**4
    return {"schema":"R762P_EXACT_VERIFICATION_V1",
            "messages":256,"alphabet_size":4,"source_channels":4,
            "unrestricted_single_substitution_tests":{"detect5":tested5,"correct7":tested7},
            "code5":{"length":5,"minimum_distance":d5,"single_error_detection":True},
            "code7":{"length":7,"minimum_distance":d7,
                     "single_error_correction":True,
                     "parity_check_columns":[list(h) for h in H_COLUMNS]},
            "bounds":{"detect_min_length":5,"correct_min_length":7,
                      "length6_ball_size":19,
                      "length6_required_volume":4864,
                      "length6_capacity":4096},
            "status":"all exact assertions passed"}


if __name__ == "__main__":
    print(json.dumps(verify(),indent=2,ensure_ascii=False))
