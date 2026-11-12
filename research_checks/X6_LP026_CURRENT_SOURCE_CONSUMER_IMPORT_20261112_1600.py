#!/usr/bin/env python3
"""Current-source X6 LP026 consumer integration test (no canonical source edit).

Requires sibling experiments/x6_signed_native_spatial_v16_20260905 Python source.
The Git blob SHA-1 checks pin exactly the current inspected consumers. All counts
are exact integers/rationals. No mathematical admission or formal native claim.
"""
from __future__ import annotations
from collections import defaultdict
from fractions import Fraction
from hashlib import sha1
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "experiments" / "x6_signed_native_spatial_v16_20260905"
PINS = {
    "x6_signed.py": "ac32f6d82a91db99297e587cf63b0df95cece514",
    "signed_brc.py": "300a96e3dc24bf6fff73743037a0347a8bc83176",
}
for filename, pin in PINS.items():
    data = (SOURCE / filename).read_bytes()
    blob = sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    assert blob == pin, (filename, blob)
sys.path.insert(0, str(SOURCE))
from x6_signed import canonical, relative_endpoint_multiplicity  # noqa: E402
from signed_brc import endpoint_multiplicity, endpoint_weight  # noqa: E402

E = [tuple(int(j == i) for j in range(5)) for i in range(5)] + [(-1,) * 5]
Z = (0,) * 5


def add(x, y):
    return tuple(a+b for a,b in zip(x,y))


def relative_dp(max_n, positive_only=False):
    states = {Z: 1}
    for n in range(max_n+1):
        yield n, states
        nxt = defaultdict(int)
        for q, count in states.items():
            for e in E:
                nxt[add(q,e)] += count
                if not positive_only:
                    nxt[add(q,tuple(-u for u in e))] += count
        states = dict(nxt)


def relative_address(q):
    return canonical(q+(0,))


def native_fiber(n, q):
    # Independent native endpoint histogram with exact cancellation pairs.
    return sum(endpoint_multiplicity(n, tuple(v+h for v in q)+(h,))
               for h in range(-n,n+1))


def main():
    pos_tests = 0
    for n, states in relative_dp(9, positive_only=True):
        assert sum(states.values()) == 6**n
        for q, value in states.items():
            # Real, imported current Source consumer, not a local reimplementation.
            assert relative_endpoint_multiplicity(n,relative_address(q)) == value, (n,q)
            pos_tests += 1
    signed_tests = 0
    for n, states in relative_dp(6):
        assert sum(states.values()) == 12**n
        for q, value in states.items():
            # Real, imported signed-native endpoint consumer.
            assert value == native_fiber(n,q), (n,q)
            signed_tests += 1
    p0 = relative_endpoint_multiplicity(6,(0,)*6)
    s0 = dict(relative_dp(6)) [6][Z]
    n0 = endpoint_multiplicity(6,(0,)*6)
    assert (p0,s0,n0) == (720,21360,19920)
    a = (0,1,1,2,3,5)
    assert dict(relative_dp(8))[8][tuple(x-a[5] for x in a[:5])] == 4200
    assert relative_endpoint_multiplicity(8,a) == 0
    # Weighted kernel actual Source consumer, in its strictly-positive contract.
    wp=(Fraction(1),Fraction(1,2),Fraction(2),Fraction(1),Fraction(3,2),Fraction(2))
    wm=(Fraction(1),Fraction(3,2),Fraction(1,3),Fraction(2),Fraction(1),Fraction(3))
    assert endpoint_weight(2,(0,)*6,wp,wm) == Fraction(143,6)
    for bad in [(-1,0,0,0,0,0),(1,1,1,1,1,1)]:
        try: relative_endpoint_multiplicity(1,bad)
        except ValueError: pass
        else: raise AssertionError("legacy positive consumer accepted invalid observer")
    print("PASS X6_LP026_CURRENT_SOURCE_CONSUMER_IMPORT")
    print("source_blob_pins", PINS)
    print("positive_actual_consumer_state_length_tests",pos_tests)
    print("signed_actual_native_fiber_state_length_tests",signed_tests)
    print("observer_n6:positive,signed,native_zero",p0,s0,n0)
    print("signed_relative_n8_median_witness",4200)
    print("weighted_native_n2_zero",Fraction(143,6))


if __name__ == '__main__':
    main()
