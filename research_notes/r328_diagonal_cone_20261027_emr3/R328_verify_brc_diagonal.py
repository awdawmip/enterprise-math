#!/usr/bin/env python3
"""R328 exact BRC Newton difference certificate, full signed recurrence.

Model and 12-term kernel are those of the immutable R325/R327 source.
Only integer arithmetic is used; no truncation of off-domain coefficients.
The finite scan checks all Newton differences through `--max-q` and the
five universal diagonal formulas proved separately in the accompanying note.
"""
import argparse
import hashlib
import json
import time
from math import comb

PRIOR_R327_D_SHA = 'ace585095c2606cb7e5c07d54640a8fe586fe669ae8d37503e2d6042ea9fb2ec'
PRIOR_R327_TRIANGLE_SHA = 'fd37e0fe67867da8ba63c44999e92ee83a4e1ceabfd7e32e2780381b9cd536b9'


def C(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def kernel(i):
    d = (-C(4, i) + C(2, i-1), C(5, i-1) - C(5, i-2),
         C(7, i-2), -C(9, i-3))
    a = [0] * (2*i+1)
    for j, val in enumerate(d, start=1):
        if val:
            p = i + 1 - j
            assert p >= 0
            for k in range(p+1):
                a[i-1+k] -= val * C(p, k)
    while a and not a[-1]:
        a.pop()
    return a


def source(s):
    if s > 10:
        return []
    out = [0] * (2*s+2)
    for val, p in ((-C(3, s-1), s), (-C(6, s-1), s-1), (C(8, s-2), s-2)):
        if val:
            for k in range(p+1):
                out[s+k] += val * C(p, k)
    while out and not out[-1]:
        out.pop()
    return out


def predicted_diagonal(q, r):
    assert 0 <= r <= min(4, q)
    polys = (
        (1, 1),
        (6*q, 1),
        (2*(45*q*q - 27*q - 46), 5),
        (4*(45*q**3 - 81*q*q - 82*q - 40), 5),
        (2*(675*q**4 - 2430*q**3 - 51*q*q - 2386*q + 4080), 25),
    )
    num, den = polys[r]
    assert num > 0, (q, r, num)
    num *= 5**(q-r)
    assert num % den == 0, (q, r, num, den)
    return num // den


def run(max_q):
    t0 = time.monotonic()
    assert max_q >= 64
    K = [None] + [kernel(i) for i in range(1, 13)]
    assert K[1] == [2, 3] and K[2] == [0, -1, 4, 4]
    # Matrix of exact integer samples N_(q,u), 0<=u<=q.
    samples = [[] for _ in range(max_q+1)]
    history = {0: [1, 1]}
    sha_triangle = hashlib.sha256()
    sha_d = hashlib.sha256()
    sha_diag = hashlib.sha256()
    prefix_triangle_match = None
    prefix_d_match = None
    triangle_count = 0
    diag_count = 0
    min_d = None
    min_d_at = None
    negative_offdomain = 0
    boundary = {}
    for s in range(2*max_q+1):
        if s == 0:
            b = history[0]
        else:
            b = source(s)
            b.extend([0] * (2*s+2-len(b)))
            for i in range(1, min(s,12)+1):
                prev = history[s-i]
                for shift, kv in enumerate(K[i]):
                    if kv:
                        for j, bv in enumerate(prev):
                            b[j+shift] += kv * bv
            while b and not b[-1]:
                b.pop()
            history[s] = b
            if s >= 12:
                del history[s-12]
        assert len(b) <= 2*s+2, (s, len(b))
        assert b[0] == 2**s
        for iq in range(s+1):
            v = b[iq] if iq < len(b) else 0
            assert v > 0, ('DOMAIN_NEGATIVE', s, iq, v)
            sha_triangle.update(str(v).encode('ascii')+b'\n')
            triangle_count += 1
        for iq in range((s+1)//2, min(max_q,s)+1):
            assert iq <= s <= 2*iq
            samples[iq].append(b[iq] << (2*iq-s))
        negative_offdomain += sum(v < 0 for v in b[s+1:])
        if s == 1280:
            prefix_triangle_match = sha_triangle.hexdigest() == PRIOR_R327_TRIANGLE_SHA
            assert prefix_triangle_match, ('R327_TRIANGLE_HASH', sha_triangle.hexdigest())
        if s in (0, 3, 13, 1280, 1408, 1536):
            boundary[str(s)] = {
                'b_s0': str(b[0]),
                'b_ss': str(b[s]) if s < len(b) else '0',
                'negative_outside': sum(v < 0 for v in b[s+1:]),
            }
    diffs = 0
    for iq in range(max_q+1):
        row = samples[iq]
        assert len(row) == iq+1, (iq,len(row))
        for k in range(iq+1):
            val = row[0]
            assert val > 0, ('DIFFERENCE_NEGATIVE', iq,k,val)
            sha_d.update(f'{iq}|{k}|{val}\n'.encode('ascii'))
            if min_d is None or val < min_d:
                min_d, min_d_at = val, [iq,k]
            r = iq-k
            if r <= 4:
                expected = predicted_diagonal(iq,r)
                assert val == expected, ('DIAGONAL_IDENTITY',iq,k,r,val,expected)
                sha_diag.update(f'{iq}|{r}|{val}\n'.encode('ascii'))
                diag_count += 1
            row = [row[u+1]-row[u] for u in range(len(row)-1)]
            diffs += 1
        if iq == 640:
            prefix_d_match = sha_d.hexdigest() == PRIOR_R327_D_SHA
            assert prefix_d_match, ('R327_DIFFERENCE_HASH',sha_d.hexdigest())
    assert triangle_count == (2*max_q+1)*(2*max_q+2)//2
    assert diffs == (max_q+1)*(max_q+2)//2
    assert diag_count == sum(min(5,iq+1) for iq in range(max_q+1))
    out = {
        'schema':'ENTERPRISE_MATH_R328_EXACT_EVIDENCE_V1',
        'status':'PASS',
        'scope':'R325 ordered-six-edge auxiliary BRC Newton observation',
        'arithmetic':'Python arbitrary-precision exact integers (no float signs)',
        'max_q':max_q, 'max_s_direct':2*max_q,
        'finite_certificate':{'triangle_positive_count':triangle_count,
            'triangle_sha256':sha_triangle.hexdigest(),
            'forward_d_positive_count':diffs,'forward_d_sha256':sha_d.hexdigest(),
            'top_five_diagonal_equalities':diag_count,
            'top_five_diagonal_sha256':sha_diag.hexdigest(),
            'minimum_positive_difference':str(min_d),
            'minimum_difference_at':min_d_at,
            'negative_offdomain_count':negative_offdomain,
            'r327_s1280_triangle_sha256_match':prefix_triangle_match,
            'r327_q640_d_sha256_match':prefix_d_match,
            'samples':boundary},
        'unbounded_strip_consequence':f'0<=q<={max_q}, all s>=q, conditional on R326 structural lemma',
        'analytic_new_result':'for every fixed r>=0, D_(q,q-r)/5^(q-r) = (6^r/r!)*q^r + O_r(q^(r-1)), hence eventually positive; r=0..4 formulas are positive for all q>=r',
        'verification_limit':'finite recomputation and symbolic identities are author-side; independent Driver and native Result absent',
        'elapsed_seconds':round(time.monotonic()-t0,3),
    }
    return out


if __name__ == '__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--max-q',type=int,default=768)
    p.add_argument('--json',required=True)
    args=p.parse_args()
    answer=run(args.max_q)
    with open(args.json,'w',encoding='utf-8') as fd:
        json.dump(answer,fd,ensure_ascii=False,indent=2)
        fd.write('\n')
    print(json.dumps({k:v for k,v in answer.items() if k!='finite_certificate'},ensure_ascii=False,indent=2))
    print(json.dumps(answer['finite_certificate'],ensure_ascii=False,indent=2))
