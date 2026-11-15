#!/usr/bin/env python3
"""Exact one-vertex update observer quotient for a binary cycle."""
import json
from itertools import product


def q(u):
    n = len(u)
    return sum(u[i] * u[(i+1) % n] for i in range(n))


def signature(u):
    v0 = (0,) + u[1:]
    v1 = (1,) + u[1:]
    return (q(u), q(v0), q(v1))


def expected(k):
    return 5 if k == 3 else 5*k - 11


def main():
    data = []
    for k in range(3, 15):
        masks = list(product((0,1), repeat=k))
        signatures = {signature(u) for u in masks}
        num = len(signatures)
        assert num == expected(k), (k, num, expected(k))
        # Formula c=q(Set_j(0)), t=q(Set_j(1))-q(Set_j(0));
        # signature determines every possible future q readout.
        for x, q0, q1 in signatures:
            assert 0 <= q1-q0 <= 2
            assert x in (q0, q1)
        data.append({'cycle_length':k, 'original_masks':len(masks),
                     'exact_future_observer_classes':num})
    print(json.dumps({'status':'PASS_R5_ONE_VERTEX_FUTURE_QUOTIENT',
                      'model':'named Set_j(0/1) commands at one fixed cycle vertex',
                      'frozen_science_pin':'435e77af0d180eac32bd1f9c4c464bc4010b7551',
                      'exhaustive_lengths':list(range(3,15)),
                      'classes':data,
                      'review':'NOT_REVIEWED'},indent=2,sort_keys=True))

if __name__ == '__main__':
    main()
