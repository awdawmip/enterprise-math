#!/usr/bin/env python3
"""Exact one-group adversarial-write/read check for R284FC.
State: old codeword repeated K times, up to q initial wrong bits;
each target bit is attempted once, up to q omitted attempts, and each
read has at most u transient bit flips. The other Gray group stays stable.
"""
import itertools, json
from math import comb


def subsets_upto(n, r):
    for s in range(r+1):
        for ids in itertools.combinations(range(n), s):
            yield sum(1 << i for i in ids)


def run(q, u):
    K = 2*q+4*u+1
    full = (1 << K)-1
    init_err = list(subsets_upto(K, q))
    miss = list(subsets_upto(K, q))
    noise = list(subsets_upto(K, u))
    checks = 0
    read_checks = 0
    for target in [0, 1]:
        old = 1-target
        initial_code = full if old else 0
        for E in init_err:
            init_x = initial_code ^ E
            for M in miss:
                x = init_x
                target_seen = False
                for prefix in range(K+1):
                    outputs = set()
                    for R in noise:
                        observed = x ^ R
                        w = observed.bit_count()
                        ans = 0 if w <= q+u else (1 if w >= K-q-u else -1)
                        if ans >= 0:
                            outputs.add(ans)
                        read_checks += 1
                    assert len(outputs) <= 1, (q,u,target,E,M,prefix,outputs)
                    if target_seen:
                        assert old not in outputs, (q,u,target,E,M,prefix,outputs)
                    if target in outputs:
                        target_seen = True
                    if prefix == 0:
                        assert outputs == {old}, (q,u,target,E,M,outputs)
                    if prefix == K:
                        assert outputs == {target}, (q,u,target,E,M,outputs)
                    if prefix < K:
                        if not (M >> prefix) & 1:
                            if target:
                                x |= 1 << prefix
                            else:
                                x &= ~(1 << prefix)
                    checks += 1
    return dict(q=q, u=u, K=K, n=2*K, initial_states=len(init_err), miss_patterns=len(miss), read_noise_patterns=len(noise), prefix_checks=checks, read_checks=read_checks)

if __name__ == '__main__':
    print(json.dumps([run(q,u) for q,u in [(0,0),(0,1),(0,2),(1,0),(1,1),(2,0),(2,1)]],ensure_ascii=False,indent=2))
