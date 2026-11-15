#!/usr/bin/env python3
"""Exact finite-Sturmian phase-signature parity repair checker.
No floating-point arithmetic. Exhausts ALL binary strings of lengths 1..14.
Optional --max-n N (1<=N<=17) increases the exhaustive range.
"""
import argparse
import json
from collections import defaultdict
from fractions import Fraction
from itertools import product


def signature(word):
    n = len(word)
    p = [0]
    for bit in word:
        p.append(p[-1] + bit)
    alpha = Fraction(0)
    beta = Fraction(1)
    for i in range(n):
        for j in range(i + 1, n + 1):
            k = j - i
            q = p[j] - p[i]
            lo = Fraction(q - 1, k)
            hi = Fraction(q + 1, k)
            if lo > alpha:
                alpha = lo
            if hi < beta:
                beta = hi
    if not alpha < beta:
        return None
    A = min(Fraction(p[i]) - i*alpha for i in range(n + 1))
    B = max(Fraction(p[i]) - i*beta for i in range(n + 1))
    U = alpha.denominator * (1 + A)
    V = beta.denominator * B
    assert U.denominator == 1 and V.denominator == 1
    return (alpha.numerator, alpha.denominator, beta.numerator, beta.denominator, int(U), int(V))


def parity(word):
    n = len(word)
    return sum((n - i) * bit for i,bit in enumerate(word)) % 2


def prefix_parity(word):
    total = 0
    result = 0
    for bit in word:
        total += bit
        result += total
    return result % 2


def sketch(word):
    return (len(word) % 2, sum(word) % 2, parity(word))


def combine(a,b):
    m1,n1,h1 = a
    m2,n2,h2 = b
    return ((m1+m2)%2,(n1+n2)%2,(h1+h2+m2*n1)%2)


def check(max_n):
    summary = []
    aliases = 0
    append_tests = 0
    associativity_tests = 0
    terminal_aliases = []
    for n in range(1,max_n + 1):
        families = defaultdict(list)
        for x in range(1 << n):
            w = tuple((x >> i)&1 for i in range(n-1,-1,-1))
            assert parity(w) == prefix_parity(w)
            s = signature(w)
            if s is not None:
                families[s].append(w)
        doubles=0
        for s,ws in families.items():
            assert len(ws) <= 2, (n,s,ws)
            assert len({parity(w) for w in ws}) == len(ws), (n,s,ws)
            if len(ws)==2:
                doubles += 1
                aliases += 1
                w,v=ws
                p=q=0
                mismatch=[]
                for i,(a,b) in enumerate(zip(w,v),1):
                    p+=a;q+=b
                    if p!=q:mismatch.append(i)
                assert (len(mismatch)==1 and abs(p-q)==0) or (n==1 and len(mismatch)==1), (n,mismatch,w,v)
                if mismatch[0]==n:
                    terminal_aliases.append((n, ''.join(map(str,w)),''.join(map(str,v))))
                if n <= 12:
                    for ell in range(5):
                        for tail in product((0,1), repeat=ell):
                            assert sketch(w+tail)==combine(sketch(w),sketch(tail))
                            assert sketch(v+tail)==combine(sketch(v),sketch(tail))
                            append_tests += 2
        for a in product((0,1),repeat=2):
            for b in product((0,1),repeat=2):
                for c in product((0,1),repeat=2):
                    assert combine(combine(sketch(a),sketch(b)),sketch(c)) == combine(sketch(a),combine(sketch(b),sketch(c)))
                    associativity_tests += 1
        summary.append(dict(length=n,binary_candidates=2**n,admitted=sum(map(len,families.values())),signatures=len(families),doubleton_signatures=doubles,terminal_aliases=sum(k==n for k,_,_ in terminal_aliases)))
    return {'marker':'R170_UNIVERSAL_PARITY_REPAIR_EXACT_PASS','max_length':max_n,'total_binary_candidates':sum(x['binary_candidates'] for x in summary),'total_admitted':sum(x['admitted'] for x in summary),'distinct_signatures_summed':sum(x['signatures'] for x in summary),'doubleton_signatures':aliases,'append_cocycle_pair_checks':append_tests,'associativity_checks':associativity_tests,'terminal_alias_examples':terminal_aliases,'by_length':summary}


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=14)
    parser.add_argument('--json-path', default='R170_parity_verification.json')
    args = parser.parse_args()
    assert 1 <= args.max_n <= 17
    result=check(args.max_n)
    with open(args.json_path, 'w', encoding='utf8') as f:
        json.dump(result,f,indent=2,ensure_ascii=False)
        f.write('\n')
    print(result['marker'])
    print('candidates', result['total_binary_candidates'], 'admitted',result['total_admitted'],'aliases',result['doubleton_signatures'])
    print('tails',result['append_cocycle_pair_checks'],'associativity',result['associativity_checks'])
    print('terminal aliases',result['terminal_alias_examples'])
