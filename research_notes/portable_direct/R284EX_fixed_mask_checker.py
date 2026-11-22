#!/usr/bin/env python3
"""R284EX: fixed-across-transition tag fault mask, transient read flips.
Exact independent tests for the four-cycle construction and adjacent sharp boundary.
Uses arbitrary-precision integer Hamming distances; no floating arithmetic.
"""
from itertools import combinations
import json
from pathlib import Path


def masks(n, radius):
    yield 0
    for k in range(1, radius + 1):
        for positions in combinations(range(n), k):
            m = 0
            for p in positions:
                m |= 1 << p
            yield m


def encode(u, q):
    a, b, c = u + q, 3 * u + 2 * q + 1, u + q + 1
    A = (1 << a) - 1
    B = ((1 << b) - 1) << a
    C = ((1 << c) - 1) << (a + b)
    return (0, B | C, A | C, A | B), (a, b, c), (A, B, C)


def path(codes, lengths, edge, u, q):
    a, b, c = lengths
    lo = a
    mid = range(a, a + b)
    al = range(0, a)
    ch = range(a + b, a + b + c)
    if edge % 2 == 0:  # B and C
        cutoff = 2 * u + q
        sequence = list(mid[:cutoff])
        for cbit, bbit in zip(ch, mid[cutoff:]):
            sequence.extend((cbit, bbit))
    else:  # B and A
        cutoff = 2 * u + q + 1
        sequence = list(mid[:cutoff])
        for abit, bbit in zip(al, mid[cutoff:]):
            sequence.extend((abit, bbit))
    assert set(sequence) == set(p for p in range(sum(lengths)) if (codes[edge] ^ codes[(edge + 1) % 4]) >> p & 1)
    x = codes[edge]
    ans = [x]
    for bit in sequence:
        x ^= 1 << bit
        ans.append(x)
    assert x == codes[(edge + 1) % 4]
    return ans


def decode(y, codes, radius):
    hits = [i for i, c in enumerate(codes) if (y ^ c).bit_count() <= radius]
    assert len(hits) <= 1, (y, hits)
    return hits[0] if hits else None


def verify(u, q):
    codes, lengths, _ = encode(u, q)
    n = sum(lengths)
    v = u + q
    a_edge = 4*u + 3*q + 1
    b_diag = 2*u + 2*q + 1
    assert n == 5*u + 4*q + 2
    for i in range(4):
        for j in range(i + 1, 4):
            d = (codes[i] ^ codes[j]).bit_count()
            assert d >= (a_edge if (j-i in (1,3)) else b_diag)
    # u=q=0 has a separate Gray construction.
    if u == q == 0:
        codes = (0, 1, 3, 2)
    faults = list(masks(n, q))
    noise = list(masks(n, u))
    comparisons = 0
    prefix_count = 0
    for i in range(4):
        ps = path(codes, lengths, i, u, q) if u+q else [codes[i], codes[(i+1)%4]]
        old, new = i, (i+1)%4
        for F in faults:
            seen_new = False
            for p, x in enumerate(ps):
                prefix_count += 1
                for R in noise:
                    label = decode(x ^ F ^ R, codes, v)
                    comparisons += 1
                    assert label in (None, old, new), (u, q, i, p, F, R, label)
                    if p in (0, len(ps)-1):
                        assert label == (old if p == 0 else new), (u,q,i,p,F,R,label)
                    if label == old:
                        assert not seen_new, (u, q, i, p, F, R, "ROLLBACK")
                    if label == new:
                        seen_new = True
    return {"u":u,"q":q,"n":n,"edge_required":a_edge,"diagonal_required":b_diag,
            "fixed_masks":len(faults),"transient_masks":len(noise),
            "prefix_fault_states":prefix_count,"exact_read_decodings":comparisons,
            "result":"PASS"}


def boundary_witness(u,q):
    if u == q == 0: return {"u":u,"q":q,"kind":"distinctness: edge distance at least one"}
    v = u + q
    d = 4*u + 3*q  # one less than necessary edge distance
    assert d >= 2*v+1
    j = d - 2*v
    assert 0 <= j <= 2*u+q
    F = sum(1 << i for i in range(j,j+q))
    prefix_1 = (1 << j)-1
    prefix_2 = (1 << (j+q))-1
    old, new = 0, (1 << d)-1
    act_1,act_2=prefix_1 ^ F,prefix_2 ^ F
    assert (act_1 ^ new).bit_count() <= 2*u+q
    assert (act_2 ^ old).bit_count() <= 2*u+q
    # The radius-v ball of each endpoint intersects the radius-u ball
    # of the corresponding actual word; construct literal read words.
    def bridge(a,b):
        z = a
        for i in range(d):
            if (z^b)>>i&1 and (z^a).bit_count()<u:
                z ^= 1<<i
        assert (z^a).bit_count()<=u and (z^b).bit_count()<=v
        return z
    y1,y2=bridge(act_1,new),bridge(act_2,old)
    assert (y1^new).bit_count() <= v and (y2^old).bit_count() <= v
    return {"u":u,"q":q,"edge_distance":d,"time_indices":[j,j+q],
            "fixed_fault_mask":hex(F),"read_new":hex(y1),"read_old":hex(y2),
            "old_code":hex(old),"new_code":hex(new),"kind":"literal-new-then-old"}

if __name__ == '__main__':
    rows=[verify(u,q) for u in range(3) for q in range(3)]
    witnesses=[boundary_witness(u,q) for u in range(3) for q in range(3)]
    out={"record":"R284EX_FIXED_MASK_4TAG_EXACT","model":"one fixed <=q bit XOR fault mask per entire transition; independent <=u read flips; stateless unique-radius (u+q) decoder", "verified_cases":rows,"edge_lower_bound_witnesses":witnesses,
         "source":"script identical to checked artifact; all integer-exact", "review":"NOT_REVIEWED"}
    fp=Path('/mnt/data/R284EX_fixed_mask_certificate.json')
    fp.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    print(json.dumps({"cases":rows,"total_read_decodings":sum(r['exact_read_decodings'] for r in rows),"certificate":str(fp)},ensure_ascii=False))
