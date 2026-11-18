#!/usr/bin/env python3
"""Exact Hasse-jet integral-lattice repair on the R762FH q9 six-branch model."""
import json
import math
import R762FH_VERIFY as H

def terminal_states():
    targets = {36} | {36 + 18*3**(h-3) for h in range(3, 9)}
    vector = [0]*729
    vector[0] = 1
    saved = {}
    for n in range(1, max(targets)+1):
        following = [0]*729
        for shift in H.SHIFTS:
            for i, value in enumerate(vector):
                if value:
                    following[shift[i]] += value
        vector = following
        if n in targets:
            den = 3**(n//3-2)
            assert all(v % den == 0 for v in vector)
            saved[n] = [v//den for v in vector]
    return saved

def pascal_jets_mod(coefficients, modulus):
    data = [int(x) % modulus for x in coefficients]
    for axis in range(3):
        output = [0]*729
        for idx, value in enumerate(data):
            if not value:
                continue
            x, y, z = idx//81, idx//9 % 9, idx % 9
            coords = [x, y, z]
            for degree in range(coords[axis]+1):
                changed = coords.copy()
                changed[axis] = degree
                pos = 81*changed[0]+9*changed[1]+changed[2]
                output[pos] = (output[pos] + math.comb(coords[axis], degree)*value) % modulus
        data = output
    return data

def verify():
    states = terminal_states()
    records = []
    mod3_profile = None
    mod9_profile = None
    for h in range(3, 9):
        L = 18*3**(h-3)
        delta = [x-y for x,y in zip(states[36+L], states[36])]
        scalar = 3**(h-2)
        assert all(x % scalar == 0 for x in delta)
        quotient = [x//scalar for x in delta]
        profile3 = [x%3 for x in quotient]
        assert sum(bool(x) for x in profile3) == 729
        if mod3_profile is None:
            mod3_profile = profile3
        assert mod3_profile == profile3
        if h >= 4:
            profile9 = [x%9 for x in quotient]
            if mod9_profile is None:
                mod9_profile = profile9
            assert mod9_profile == profile9
        modulus=3**h
        jets=pascal_jets_mod(delta, modulus)
        support=[i for i,x in enumerate(jets) if x]
        minimal_degree=min(i//81+(i//9)%9+i%9 for i in support)
        J=jets[0*81+4*9+6]
        assert len(support)==227
        assert minimal_degree==10
        assert J==3**(h-1)
        records.append(dict(h=h, L=L, n=36, nonzero_hasse_jets=len(support),
                            minimum_total_degree=minimal_degree,
                            jet_0_4_6_mod_3h=J,
                            scaled_full_terminal_profile_mod3_nonzero=729,
                            scaled_full_terminal_profile_mod3_same_as_h3=True,
                            scaled_full_terminal_profile_mod9_same_as_h4=h>=4))
    return dict(schema='R762FI_Q9_HASSE_JET_REPAIR_EVIDENCE_V1',
                frozen_model=H.__doc__, all_hasse_jets=729,
                scope='full 729-terminal integer convolution h=3..8 at n=36',
                arithmetic='exact integer convolution; Pascal/Hasse transforms modulo 3^h',
                results=records, result='PASS', reviewed='NOT_REVIEWED')

if __name__ == '__main__':
    print(json.dumps(verify(),indent=2,ensure_ascii=False))
