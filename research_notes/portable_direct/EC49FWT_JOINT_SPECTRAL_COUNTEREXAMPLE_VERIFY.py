#!/usr/bin/env python3
"""Independent two-sided Farey joint-spectrum collision, frozen BRC16943.
Run alongside EC49FWT_TWO_SIDED_ANCHOR_REALIZATION_VERIFY.py.
"""
from EC49FWT_TWO_SIDED_ANCHOR_REALIZATION_VERIFY import normalized, c11, spectrum, FULL
import json


def signature(a, b):
    branches = [normalized(a, b-a, s) for s in (-1, 1)]
    def factor(hole):
        return FULL if hole is None else FULL ^ (1 << hole)
    return tuple(spectrum(mask, factor(hole)) for mask, hole, h, n in branches), branches


def main():
    s1, branches1 = signature(7, 11)
    s2, branches2 = signature(9, 17)
    assert s1 == s2
    assert [(x[0], x[1]) for x in branches1] == [(789, 1), (327, 0)]
    assert [(x[0], x[1]) for x in branches2] == [(327, 1), (789, 0)]
    assert s1[0] != s1[1]
    observations = []
    for (a, b), branches in [((7, 11), branches1), ((9, 17), branches2)]:
        for sign, (mask, hole, h, n) in zip((-1, 1), branches):
            assert all(c11(h+a*t, n+(b-a)*t) ==
                       (bool(mask >> (t%10) & 1) and (hole is None or t%11 != hole))
                       for t in range(110))
        h, n = branches[0][2:4]
        observations.append(int(c11(h+a*44, n+(b-a)*44)))
    assert observations == [1, 0]
    return {'status':'ALL PASS', 'anchors':['7/11','9/17'],
            'left_states': [[789,1],[327,1]], 'right_states': [[327,0],[789,0]],
            'same_joint_complete_indexed_reflection_spectra':True,
            'left_probe_t_44': observations,
            'site_crt':{'t_mod_10':4,'t_mod_11':0},
            'claim':'two-sided complete indexed reflection spectra do not uniquely determine the normalized pair even for real Farey anchors'}


if __name__ == '__main__':
    print(json.dumps(main(), indent=2))
