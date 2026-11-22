#!/usr/bin/env python3
"""Frozen R5 m=2, O(N) coefficient period: two exact independent constructions.

Python 3 standard library, no external packages. This is a scalar frozen
partition count, not a claim of native X6 dynamics or project review.
"""
from math import lcm
import json

PRICES = tuple(range(214, 315))
EVENTS = (
    frozenset(range(214, 219)),
    frozenset((214, 216, 217, 218, 219, 220, 221)),
    frozenset((215, 216, 217, 218, 219, 220, 221)),
    frozenset(range(223, 291)),
    frozenset(range(296, 313)),
)
WITNESS_ORDERS = (7, 9, 11, 13, 17, 19, 23, 25, 27, 29, 31, 32, 37, 43)
EXPECTED_L = 229746052653717600


def cyclic_shift(v, p):
    j = p % len(v)
    return v[-j:] + v[:-j] if j else v[:]


def add(a, b):
    return [u + v for u, v in zip(a, b)]


def sub(a, b):
    return [u - v for u, v in zip(a, b)]


def cyclic_mul(a, b):
    n = len(a)
    out = [0] * n
    for j, u in enumerate(a):
        if u:
            for k, v in enumerate(b):
                if v:
                    out[(j + k) % n] += u * v
    return out


def phi(d):
    if d in (9, 25, 27):
        step = {9: 3, 25: 5, 27: 9}[d]
        return [int(j % step == 0) for j in range(d-step+1)]
    if d == 32:
        return [1] + [0]*15 + [1]
    assert d in (7, 11, 13, 17, 19, 23, 29, 31, 37, 43)
    return [1] * d


def cyclotomic_reduce(a, d):
    f = phi(d)
    out = a[:]
    for i in range(len(out)-1, len(f)-2, -1):
        x = out[i]
        if x:
            for j, c in enumerate(f):
                out[i-len(f)+1+j] -= x*c
    return out[:len(f)-1]


def data_for(mask):
    chosen = [EVENTS[i] for i in range(5) if mask & (1 << i)]
    union = tuple(sorted(set().union(*chosen)))
    signatures = {p: sum(1 << i for i in range(5) if mask & (1 << i) and p in EVENTS[i]) for p in union}
    assert all(signatures.values())
    return union, signatures


def prod_factor_jet(q, dq, union):
    """Multiply by prod_{p in union}(1-q^p), and differentiate exactly."""
    for p in union:
        shifted = cyclic_shift(q, p)
        dshifted = cyclic_shift(dq, p)
        q, dq = (sub(q, shifted),
                 [u-v-p*x for u,v,x in zip(dq, dshifted, shifted)])
    return q, dq


def mask_jets_occupancy(d, mask):
    """Method A: sequential DP on occupied failure-event bits (capacity 1)."""
    union, signatures = data_for(mask)
    one = [1] + [0]*(d-1)
    zeros = [0]*d
    dp = {0: (one, zeros)}
    for p in union:
        sig = signatures[p]
        nxt = {bits: (v[:], dv[:]) for bits,(v,dv) in dp.items()}
        for bits,(v,dv) in dp.items():
            if bits & sig:
                continue
            newbits = bits | sig
            a = cyclic_shift(v, p)
            b = [u + p*x for u,x in zip(cyclic_shift(dv,p), a)]
            if newbits not in nxt:
                nxt[newbits] = (a,b)
            else:
                x,y = nxt[newbits]
                nxt[newbits] = (add(x,a),add(y,b))
        dp = nxt
    q = [0]*d
    dq = [0]*d
    for v,dv in dp.values():
        q = add(q,v)
        dq = add(dq,dv)
    return prod_factor_jet(q,dq,union)


def partitions(mask):
    """Every set partition of the specified labeled event set, exactly once."""
    if mask == 0:
        yield ()
        return
    b = mask & -mask
    rest = mask ^ b
    sub = rest
    while True:
        block = b | sub
        for tail in partitions(mask ^ block):
            yield (block,) + tail
        if sub == 0:
            break
        sub = (sub - 1) & rest


def mask_jets_partition(d, mask):
    """Method B: disjoint-block set partitions, using exact membership classes.

    Each selected price occupies exactly the event block B equal to its
    membership signature. The selected blocks form a partition of the set of
    activated events, giving an independent formula for Q_{I,2}(q).
    """
    union, signatures = data_for(mask)
    h = {}
    dh = {}
    for p,sig in signatures.items():
        if sig not in h:
            h[sig],dh[sig] = [0]*d,[0]*d
        h[sig][p%d] += 1
        dh[sig][p%d] += p
    one = [1] + [0]*(d-1)
    zero = [0]*d
    q,dq = zero[:],zero[:]
    H = mask
    while True:
        for blocks in partitions(H):
            v,dv = one[:],zero[:]
            for B in blocks:
                if B not in h:
                    v,dv = zero[:],zero[:]
                    break
                ov = v
                v = cyclic_mul(ov,h[B])
                dv = add(cyclic_mul(dv,h[B]),cyclic_mul(ov,dh[B]))
            q,dq = add(q,v),add(dq,dv)
        if H == 0:
            break
        H = (H-1) & mask
    return prod_factor_jet(q,dq,union)


def numerator_jets(d, method):
    r,dr = [0]*d, [0]*d
    for mask in range(1, 32):
        q,dq = method(d,mask)
        sign = 1 if mask.bit_count() % 2 else -1
        if sign == 1:
            r,dr = add(r,q),add(dr,dq)
        else:
            r,dr = sub(r,q),sub(dr,dq)
    return cyclotomic_reduce(r,d),cyclotomic_reduce(dr,d)


def verify():
    candidate = tuple(d for d in range(2,315) if sum(p%d==0 for p in PRICES) >=3)
    assert len(candidate)==39 and lcm(*candidate)==EXPECTED_L
    results = []
    for d in WITNESS_ORDERS:
        A = numerator_jets(d,mask_jets_occupancy)
        B = numerator_jets(d,mask_jets_partition)
        assert A == B, (d,"independent full-vector mismatch")
        v0,v1 = A
        j = 0 if any(v0) else 1
        assert any(A[j]), (d,"jet zero")
        n = sum(p%d==0 for p in PRICES)
        assert n-j >= 3, (d,"pole too small")
        coordinate = next(i for i,c in enumerate(A[j]) if c)
        results.append({"d":d,"denominator_zero_order":n,"first_nonzero_jet":j,
                        "surviving_pole_order":n-j,"first_nonzero_coordinate":coordinate,
                        "coefficient":A[j][coordinate],
                        "zero_jet_vector":v0,"first_jet_vector":v1})
    assert lcm(*(row["d"] for row in results)) == EXPECTED_L
    certificate={"schema":"R5_M2_O1_EXACT_PERIOD_V1", "date":"2026-11-22",
                 "frozen_model":"R5_TRUE_EVENT_SCALAR_M2","threshold_m":2,
                 "claim":"M_2(O(N)) = 229746052653717600",
                 "candidate_orders":list(candidate),"ceiling":str(EXPECTED_L),
                 "method_A":"occupancy-bit DP over exact event overlaps",
                 "method_B":"all set partitions of activated-event subsets; signature-specific q-polynomials",
                 "arithmetic":"integer cyclic ring with cyclotomic reduction; exact q d/dq jets",
                 "witnesses":results,"review":"NOT_REVIEWED"}
    return certificate


if __name__ == '__main__':
    cert=verify()
    print("UPPER",cert["ceiling"],"39 candidates")
    print("d  n_d  j  pole  coord  coefficient")
    for r in cert["witnesses"]:
        print(r["d"],r["denominator_zero_order"],r["first_nonzero_jet"],r["surviving_pole_order"],r["first_nonzero_coordinate"],r["coefficient"])
    print("ALL CHECKS PASS")
    with open('R5_M2_O1_CERTIFICATE_FULL.json','w',encoding='utf-8') as f:
        json.dump(cert,f,ensure_ascii=False,indent=2)
