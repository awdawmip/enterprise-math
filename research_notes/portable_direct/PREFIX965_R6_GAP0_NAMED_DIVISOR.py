#!/usr/bin/env python3
"""PREFIX-965: exact m=0 named XOR witness reconstruction (integer arithmetic).

This is an auxiliary observer for Enterprise Math research, not a native X6 event
or formal theorem admission. The frozen scientific pin is preserved.
"""
import json
from math import isqrt
from pathlib import Path

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'


def odd_divisors_q(x, p):
    """All odd divisors of positive x in strict p-bit Q_p (sorted)."""
    if x <= 0:
        return []
    h = 1 << (p - 1)
    found = set()
    for d in range(1, isqrt(x) + 1):
        if x % d:
            continue
        for b in (d, x // d):
            if h < b < 2 * h and b & 1:
                found.add(b)
    return sorted(found)


def candidate_source_patterns(p):
    """Proved exhaustive configurations (a,c,C,i,j,I,J) for gap zero."""
    h = 1 << (p - 1)
    for r in range(1, p-1):
        a = h + (1 << r) - 1
        yield (a, 2 - (1 << (r+1)), 2*h, 1, r+1, p-1, p-1, 'B')
        if r <= p-3:
            yield (a, 2-h, h + (1 << (r+1)), 1, p-1, p-1, r+1, 'A1')
            yield (a, 2-h, h + (1 << (r+1)), 1, p-1, r+1, p-1, 'A2')


def named_gap0(p, k):
    assert p >= 4 and k >= 1 and (k & 1) and k+2 < (1 << (p-1))
    patterns = list(candidate_source_patterns(p))
    witnesses = []
    feasible_patterns = 0
    divisors_tested = 0
    for a, c, C, i, j, I, J, typ in patterns:
        x, y = k*a, (k+2)*a
        # c=2^i-2^j requires source bit 0; C positive sum requires source bit 1.
        if (x >> j) & 1 or not ((y >> J) & 1):
            continue
        feasible_patterns += 1
        for b in odd_divisors_q(x-c, p):
            divisors_tested += 1
            t = (x-c)//b
            if t < 1:
                continue
            if ((x ^ (1 << j))-(1 << i) != t*b or
                    (y ^ (1 << J))-(1 << I) != t*b):
                raise AssertionError('source pattern identity broken')
            witnesses.append((a,b,t,i,j,I,J))
    witnesses.sort()
    return {
        'p':p, 'k':k, 'numeric_residual_pairs':2*p-5,
        'source_slot_patterns':len(patterns),
        'actual_sign_feasible_patterns':feasible_patterns,
        'divisor_hits_before_output':divisors_tested,
        'named_joint_witnesses':len(witnesses),
        'distinct_ordered_pairs':len({(x[0],x[1]) for x in witnesses}),
        'witnesses':[list(x) for x in witnesses],
    }


def direct_full(p,k,only_rigid_a=False):
    """Independent original XOR enumeration, no c/C pattern construction.

    If only_rigid_a=True, a's are restricted by the PREVIOUSLY PROVED
    necessary-support lemma, but all source-slot pairs are traversed.
    """
    h = 1 << (p-1)
    aa = ([h+(1<<r)-1 for r in range(1,p-1)] if only_rigid_a
          else range(h+1,2*h,2))
    qq = range(h+1,2*h,2)
    out=[]
    for a in aa:
        left={}
        for i in range(p):
            for j in range(p):
                x=(k*a ^ (1<<j))-(1<<i)
                if x<=0: continue
                bs=(odd_divisors_q(x,p) if only_rigid_a else [b for b in qq if x%b==0])
                for b in bs:
                    left.setdefault((b,x//b),[]).append((i,j))
        for I in range(p):
            for J in range(p):
                y=((k+2)*a ^ (1<<J))-(1<<I)
                if y<=0: continue
                bs=(odd_divisors_q(y,p) if only_rigid_a else [b for b in qq if y%b==0])
                for b in bs:
                    for i,j in left.get((b,y//b),[]):
                        out.append((a,b,y//b,i,j,I,J))
    return sorted(out)


def run():
    rows=[]
    for p in range(4,8):
        h=1<<(p-1)
        for k in range(1,h-2,2):
            got=named_gap0(p,k)
            ref=direct_full(p,k)
            assert [tuple(w) for w in got['witnesses']] == ref, (p,k,got,ref)
            rows.append((p,k,len(ref)))
    # Larger controls use independent direct XOR on a full proven rigid support,
    # without relying on the new source pattern classification.
    for p in (8,9):
        h=1<<(p-1)
        for k in [1,7,21,23,h-3]:
            got=named_gap0(p,k)
            ref=direct_full(p,k,only_rigid_a=True)
            assert [tuple(w) for w in got['witnesses']] == ref,(p,k)
            rows.append((p,k,len(ref)))
    result=named_gap0(19,21)
    ref=direct_full(19,21,only_rigid_a=True)
    assert [tuple(w) for w in result['witnesses']]==ref
    assert result['named_joint_witnesses']==6
    assert result['distinct_ordered_pairs']==6
    data={
        'schema':'PREFIX965_R6_EXACT_NAMED_GAP_ZERO_DIVISOR_CERT_V1',
        'frozen_science_pin': PIN,
        'status':'AUTHOR_PROOF_AND_INDEPENDENT_ORIGINAL_XOR_TEST_NOT_REVIEWED',
        'numeric_residual_pairs_total_formula':'2*p-5',
        'named_source_slot_pattern_total_formula':'3*p-8',
        'algorithm':'enumerate exact source slot patterns; enforce true XOR sign bits; find Qp divisors of k*a-c and verify both original equations',
        'small_full_original_xor_checks':{'p':'4..7','core_parameters':len([x for x in rows if x[0]<=7]),'cases':rows[:sum(1 for x in rows if x[0]<=7)]},
        'larger_independent_original_xor_checks':{'p':'8 and 9, five cores per width; p19 core21','domain':'full original source slots over proven rigid a support', 'cases':[x for x in rows if x[0]>=8]},
        'p19_core21':result,
        'limits':'Auxiliary named XOR integer model; not P000 native X6 event/claim/review; divisor search complexity not claimed polynomial in bit length.'
    }
    Path('PREFIX965_R6_EXACT_RESULTS.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    print(json.dumps({'small_core_tests':len(rows),'p19_core21':result},indent=2))


if __name__ == '__main__':
    run()
