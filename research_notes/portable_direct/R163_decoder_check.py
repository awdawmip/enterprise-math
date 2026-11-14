#!/usr/bin/env python3
"""R163: quadratic exact inverse of fixed-length Sturmian phase signatures."""
from collections import defaultdict
from fractions import Fraction
import json


def signature(word):
    m = len(word)
    p = [0]
    for c in word:
        p.append(p[-1] + int(c))
    alpha, beta = Fraction(0), Fraction(1)
    for i in range(m):
        for j in range(i+1, m+1):
            q, k = p[j]-p[i], j-i
            alpha = max(alpha, Fraction(q-1, k))
            beta = min(beta, Fraction(q+1, k))
    if alpha >= beta:
        return None
    A = min(Fraction(p[j])-j*alpha for j in range(m+1))
    B = max(Fraction(p[j])-j*beta for j in range(m+1))
    return (alpha, beta, alpha.denominator*(1+A), beta.denominator*B)


def decode(m, s):
    """Return all valid words with the exact signature s; O(m^2) arithmetic."""
    alpha, beta, U, V = s
    if not 0 <= alpha < beta <= 1:
        return []
    x0 = Fraction(U, alpha.denominator)
    B = Fraction(V, beta.denominator)
    t = (B-x0)/(beta-alpha)
    prefix = []
    ambiguous = []
    for i in range(m+1):
        z = x0 + i*alpha
        v = t+i
        if z.denominator != 1:
            prefix.append(z.numerator//z.denominator)
        elif v > 0:
            prefix.append(int(z))
        elif v < 0:
            prefix.append(int(z)-1)
        else:
            ambiguous.append((i, int(z)))
            prefix.append(None)
    assert len(ambiguous) <= 1
    variants = [dict()] if not ambiguous else [
        {ambiguous[0][0]: ambiguous[0][1]-1},
        {ambiguous[0][0]: ambiguous[0][1]},
    ]
    result = []
    for variant in variants:
        p = [variant.get(i, prefix[i]) for i in range(m+1)]
        if p[0] != 0:
            continue
        bits = [p[i]-p[i-1] for i in range(1, m+1)]
        if any(x not in (0,1) for x in bits):
            continue
        word = ''.join(map(str, bits))
        if signature(word) == s:
            result.append(word)
    return sorted(set(result))


def main():
    by_length=[]
    candidates=0
    admitted=0
    signatures=0
    pairs=0
    for m in range(1, 16):
        groups=defaultdict(list)
        for n in range(1<<m):
            w=format(n, f'0{m}b')
            s=signature(w)
            if s is not None:
                groups[s].append(w)
        for s, original in groups.items():
            reconstructed=decode(m, s)
            assert reconstructed == sorted(original), (m,s,original,reconstructed)
            assert len(reconstructed) <= 2
        admitted_m=sum(map(len, groups.values()))
        pair_m=sum(len(v)==2 for v in groups.values())
        candidates += 1<<m
        admitted += admitted_m
        signatures += len(groups)
        pairs += pair_m
        by_length.append({"m":m,"candidates":1<<m,"admitted":admitted_m,
                          "signatures":len(groups),"two_word_fibers":pair_m})
    assert candidates==65534
    assert signatures==1760
    assert pairs==146
    return {"marker":"R163_EXACT_DECODER_PASS", "arithmetic":"Fraction, integer, no floats",
            "m_range":[1,15], "candidates":candidates,"admitted":admitted,
            "signature_classes":signatures, "two_word_fibers":pairs,
            "by_length":by_length}


if __name__=="__main__":
    print(json.dumps(main(), indent=2, sort_keys=True))
