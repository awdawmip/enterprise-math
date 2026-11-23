#!/usr/bin/env python3
"""R284FE exact finite checker; Python 3 standard library only."""
from itertools import combinations
import json
from pathlib import Path

def masks(n, radius):
    return [sum(1 << j for j in c)
            for r in range(min(n, radius) + 1)
            for c in combinations(range(n), r)]

def decode(y, n, q, u):
    w = y.bit_count()
    if w <= q + u:
        return 0
    if w >= n - q - u:
        return 1
    return None

def gray(k):
    return [i ^ (i >> 1) for i in range(1 << k)]

def check_one(q, u):
    K = 2*q + 4*u + 1
    errors = masks(K, u)
    omissions = masks(K, q)
    top = (1 << K) - 1
    endpoint_checks = 0
    supports_checked = 0
    for x in range(1 << K):
        poss = {decode(x ^ err, K, q, u) for err in errors}
        if x.bit_count() <= q:
            assert poss == {0}, ('old endpoint', q, u, x, poss)
            endpoint_checks += 1
        if (x ^ top).bit_count() <= q:
            assert poss == {1}, ('new endpoint', q, u, x, poss)
            endpoint_checks += 1
        assert not ({0, 1} <= poss), ('simultaneous labels', q, u, x, poss)
        supports_checked += 1

    prefixes = 0
    for old in (0, top):
        for residue in omissions:
            start = old ^ residue
            for j in range(K + 1):
                prefix = (1 << j) - 1
                for miss in masks(j, q):
                    effective = prefix & ~miss
                    after = (start | effective) if old == 0 else (start & ~effective)
                    if old == 0:
                        assert after.bit_count() >= start.bit_count()
                    else:
                        assert after.bit_count() <= start.bit_count()
                    prefixes += 1

    N = K - 1
    if N == 0:
        witness = dict(x=0,old_observation=0,new_observation=0,
                       old_distance=0,new_distance=0)
    else:
        obs_errors = masks(N, u)
        target = (1 << N) - 1
        witness = None
        for j in range(N + 1):
            x = (1 << j) - 1
            old_read = next((x ^ e for e in obs_errors
                             if (x ^ e).bit_count() <= q + u), None)
            new_read = next((x ^ e for e in obs_errors
                             if ((x ^ e) ^ target).bit_count() <= q + u), None)
            if old_read is not None and new_read is not None:
                witness = dict(x=x,old_observation=old_read,
                               new_observation=new_read,
                               old_distance=(x ^ old_read).bit_count(),
                               new_distance=(x ^ new_read).bit_count())
                break
        assert witness is not None, (q, u, N)
    return dict(q=q,u=u,sharp_block_bits=K,lower_witness_length=N,
                lower_witness=witness,checked_physical_words=supports_checked,
                checked_endpoint_words=endpoint_checks,
                checked_prefix_residues=prefixes)

def main():
    cases = [(0,0),(1,0),(2,0),(0,1),(1,1),(2,1)]
    checks = [check_one(q,u) for q,u in cases]
    cycles = {}
    for k in range(1,6):
        g=gray(k)
        assert len(set(g)) == (1 << k)
        assert all((g[i] ^ g[(i + 1) % len(g)]).bit_count() == 1
                   for i in range(len(g)))
        cycles[str(k)] = dict(period=len(g),cycle=g)
    horizons = {}
    for H in range(20):
        k=(H+1).bit_length()
        assert (1<<k)>=H+2 and (1<<(k-1))<H+2
        horizons[str(H)] = dict(H=H,minimum_k=k,period=1<<k,
                                minimum_bank_count=H+2)
    result=dict(title="R284FE_GRAY_EPOCH_LOCAL_SHARPNESS",
        status="EXACT_FINITE_CHECKS_WITH_ANALYTICAL_GENERAL_PROOF",
        cases=checks,gray_cycles=cycles,horizons=horizons,
        totals=dict(physical_words=sum(x["checked_physical_words"] for x in checks),
                    endpoint_words=sum(x["checked_endpoint_words"] for x in checks),
                    prefix_residue_states=sum(x["checked_prefix_residues"] for x in checks)))
    target=Path(__file__).with_name("R284FE_gray_epoch_certificate.json")
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2,sort_keys=True)+"\n",
                      encoding="utf-8")
    assert result["totals"] == dict(physical_words=714,endpoint_words=152,
                                    prefix_residue_states=18084)
    print(result["totals"])
    print("six block tests and five Gray cycles passed")

if __name__ == "__main__":
    main()
