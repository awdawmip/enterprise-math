#!/usr/bin/env python3
"""Exact native X6 and 3-axis fiber norm/depth recovery and BRC collision."""
from itertools import product
from math import isqrt
from pathlib import Path
import importlib.util
import hashlib
import json


def rho(z):
    h = min(z)
    return tuple(x - h for x in z)


def D(r):
    return sum((x - y) ** 2 for i, x in enumerate(r) for y in r[i+1:])


def recover(r, G):
    n = len(r)
    s0 = sum(r)
    t = n * G - D(r)
    if t < 0 or isqrt(t) ** 2 != t:
        return ()
    q = isqrt(t)
    results = set()
    for signed_sum in (q, -q):
        if (signed_sum - s0) % n == 0:
            h = (signed_sum - s0) // n
            results.add(tuple(x + h for x in r))
    return tuple(sorted(results))


def run():
    counts = {}
    for n, R in ((3, 5), (6, 2)):
        num = unique = double = 0
        for d in product(range(-R, R+1), repeat=n):
            r = rho(d)
            G = sum(x*x for x in d)
            answers = recover(r, G)
            assert d in answers
            assert len(answers) in (1, 2)
            assert len(answers) == (2 if 2*sum(r) % n == 0 and sum(d) != 0 else 1)
            assert D(r) == n * sum(x*x for x in r) - sum(r)**2
            assert n*G == D(r) + sum(d)**2
            num += 1
            unique += len(answers) == 1
            double += len(answers) == 2
        counts[str(n)] = {"points":num,"unique":unique,"double":double}

    A = (0,0,0,0,0,3)
    B = (-1,-1,-1,-1,-1,2)
    assert rho(A) == rho(B) and sum(v*v for v in A) == sum(v*v for v in B) == 9
    assert recover(rho(A),9) == (B,A)

    source = Path(__file__).resolve().parents[1] / "experiments/x6_signed_native_spatial_v16_20260905/signed_brc.py"
    data = source.read_bytes()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    assert blob == "300a96e3dc24bf6fff73743037a0347a8bc83176"
    spec = importlib.util.spec_from_file_location("frozen_native_signed_brc",source)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    assert m.shortest_event_count(A) == 3
    assert m.shortest_event_count(B) == 7
    assert m.shortest_path_multiplicity(A) == 1
    assert m.shortest_path_multiplicity(B) == 2520
    assert recover((0,1,4),17) == ((0,1,4),)  # n=3 has non-resonant residue 5 mod 3.
    assert recover((0,0,0),1) == ()
    return {"status":"PASS","point_domains":counts,
            "native_x6_same_observer_and_norm_witness":{"r":list(rho(A)),"G":9,"A":list(A),"B":list(B),"brc_A":1,"brc_B":2520},
            "source_blob":blob}


if __name__ == "__main__":
    print(json.dumps(run(),sort_keys=True))
