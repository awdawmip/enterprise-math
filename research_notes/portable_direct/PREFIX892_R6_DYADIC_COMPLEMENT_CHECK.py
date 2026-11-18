#!/usr/bin/env python3
"""PREFIX-892: exact 16-row strict-19-bit dyadic completion census.
Frozen scientific-input pin: f42f2906d77f24085c123f3ccfe9667d41caa96d.
Python 3 standard library, exact integers; same JSON schema as the C++ run.
"""
import json
from math import gcd

P, N = 32, 1 << 32
Q = range(262145, 524288, 2)
PANEL = (262147, 280001, 300001, 320003, 340007, 360007, 380003,
         400009, 420001, 440003, 460001, 480007, 500383, 510007,
         520001, 524285)


def axis(q):
    return any(pow(2, h, q) in (1, q-1) for h in range(1, P))


def zero_flip(q1, q2, inv):
    if inv is None:
        return False
    K, r = (N-1)//q1, inv
    for i in range(P):
        b = 1 << i
        if r <= K or (q2-r)*q1+b < N:
            return True
        r = (2*r) % q2
    return False


def completion(q1, q2, inv):
    if inv is None:
        return None
    assert q1*q2 > N
    k = (N*inv) % q2
    if k == 0 or k*q1 >= N:
        return None
    a = k*q1
    assert (N-a) % q2 == 0
    ell = (N-a)//q2
    assert ell > 0
    return k, ell, a, N-a


def witness(q1, q2, k, ell, a, c):
    b = N//2
    if a > b:
        x, y = (0, b), (a, a-b)
    else:
        assert c > b
        x, y = (b, 0), (c-b, c)
    assert 0 <= min(*x, *y) and max(*x, *y) < N
    assert x[0] != y[0]
    assert (x[0] ^ b) == x[1] and (y[0] ^ b) == y[1]
    assert (x[0] % q1, x[1] % q2) == (y[0] % q1, y[1] % q2)
    assert k*q1+ell*q2 == N
    return (x, y)


def run():
    A = {q for q in Q if axis(q)}
    assert len(A) == 24 and all(q not in A for q in PANEL)
    rows = []
    for q1 in PANEL:
        z = pos = overlap = new = left = right = 0
        sample = None
        for q2 in Q:
            inv = pow(q1, -1, q2) if gcd(q1, q2) == 1 else None
            zf = zero_flip(q1, q2, inv)
            w = completion(q1, q2, inv)
            z += bool(zf)
            if w is None:
                continue
            pos += 1
            k, ell, a, c = w
            witness(q1, q2, *w)
            if a > N//2:
                left += 1
            else:
                right += 1
            if zf:
                overlap += 1
            else:
                assert q2 not in A
                new += 1
                if sample is None:
                    sample = dict(q2=q2, k=k, ell=ell, a=a, c=c)
        assert pos == left+right == overlap+new
        rows.append(dict(q1=q1, pairs=len(Q), zero_flip=z,
                         positive_completion=pos, completion_already_zero_flip=overlap,
                         new_axis_and_zero_flip_free=new,
                         left_orientation=left, right_orientation=right,
                         sample=sample))
    keys = ('zero_flip', 'positive_completion', 'new_axis_and_zero_flip_free',
            'left_orientation', 'right_orientation')
    totals = {'pairs': len(PANEL)*len(Q)}
    totals.update({k: sum(row[k] for row in rows) for k in keys})
    return dict(schema='PREFIX892_R6_DYADIC_COMPLEMENT_V1',
                frozen_scientific_pin='f42f2906d77f24085c123f3ccfe9667d41caa96d',
                p=P, modulus_range=[min(Q), max(Q)], odd_moduli=len(Q),
                axis_moduli=len(A), rows=rows, totals=totals)


if __name__ == '__main__':
    print(json.dumps(run(), indent=2, ensure_ascii=False, sort_keys=True))
