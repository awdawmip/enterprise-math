#!/usr/bin/env python3
"""Exact finite corroboration of R165 terminal-alias theorem and swap test.
Usage: python R165_terminal_alias_check.py --max-length 14 --output path.json
No floating point; exhaustive over every binary word of specified lengths.
"""
import argparse
import json
from collections import defaultdict
from fractions import Fraction as Q
from itertools import product


def signature(w):
    m = len(w)
    p = [0]
    for bit in w:
        p.append(p[-1] + bit)
    alpha, beta = Q(0), Q(1)
    for i in range(m):
        for j in range(i+1, m+1):
            q = p[j]-p[i]
            alpha = max(alpha, Q(q-1, j-i))
            beta = min(beta, Q(q+1, j-i))
    if alpha >= beta:
        return None
    A = min(Q(p[i])-i*alpha for i in range(m+1))
    B = max(Q(p[i])-i*beta for i in range(m+1))
    return (alpha.numerator, alpha.denominator,
            beta.numerator, beta.denominator,
            int(alpha.denominator*(1+A)), int(beta.denominator*B))


def proposed_twin(w, s):
    """Necessary modular index, integer chord and adjacent swap; verify exactly."""
    m = len(w)
    a,b,c,d,U,V = s
    D = b*c-a*d
    N = d*U-b*V
    if N%D:
        return None
    j = N//D
    if not 1 <= j < m or (U+a*j)%b:
        return None
    q = (U+a*j)//b
    if w[j-1] == w[j]:
        return None
    p = [0]
    for v in w:
        p.append(p[-1]+v)
    if p[j] not in (q-1, q):
        return None
    v = list(w)
    v[j-1], v[j] = v[j], v[j-1]
    v = tuple(v)
    return v if signature(v)==s else None


def run(max_length):
    counts = []
    total_candidates = 0
    total_pairs = 0
    for m in range(1, max_length+1):
        fibers = defaultdict(list)
        for w in product((0,1), repeat=m):
            s = signature(w)
            total_candidates += 1
            if s is not None:
                fibers[s].append(w)
        assert all(len(v)<=2 for v in fibers.values())
        pairs = 0
        terminal_pairs = 0
        for s, words in fibers.items():
            if len(words)==2:
                pairs += 1
                w,v = words
                wp=[0]; vp=[0]
                for bit in w: wp.append(wp[-1]+bit)
                for bit in v: vp.append(vp[-1]+bit)
                differing=[j for j in range(1,m+1) if wp[j]!=vp[j]]
                assert len(differing)==1
                if differing[0]==m:
                    terminal_pairs += 1
                if m>=2:
                    assert proposed_twin(w,s)==v
                    assert proposed_twin(v,s)==w
            else:
                assert proposed_twin(words[0],s) is None
        if m>=2:
            assert terminal_pairs==0
        total_pairs += pairs
        counts.append({"length":m,"candidate_words":2**m,
                       "admitted_words":sum(len(z) for z in fibers.values()),
                       "signatures":len(fibers),"two_preimage_classes":pairs,
                       "terminal_alias_classes":terminal_pairs})
    s2 = signature((0,1))
    assert s2==signature((1,0))==(0,1,1,1,1,0)
    sx = signature((0,1,0))
    sy = signature((1,0,0))
    assert sx != sy
    assert sx==(0,1,2,3,1,0)
    assert sy==(0,1,1,2,1,1)
    same = signature((1,0,1,0,0,1,0))
    assert same==signature((1,0,0,1,0,1,0))
    return {
        "status":"R165_TERMINAL_ALIAS_EXACT_PASS",
        "arithmetic":"Python Fraction exact rational and integer arithmetic",
        "validation":"all 2^m binary words for each 1<=m<=max_length",
        "max_length":max_length,"total_binary_candidates":total_candidates,
        "total_two_preimage_classes":total_pairs,
        "lengths":counts,
        "right_append_separation":{
            "initial_words":["01","10"], "initial_signature":list(s2),
            "suffix":"0", "after_signatures":{"010":list(sx),"100":list(sy)}
        },
        "right_append_alias_persistence":{"words":["101001","100101"],"suffix":"0","same_signature":list(same)},
        "independent_review":"NOT_REVIEWED",
        "proof_scope":"Symbolic terminal-alias impossibility for all m>=2; finite checks corroborate only lengths checked"
    }


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-length',type=int,default=14)
    parser.add_argument('--output',default='R165_verification.json')
    args=parser.parse_args()
    assert 1<=args.max_length<=20
    data=run(args.max_length)
    with open(args.output,'w',encoding='utf-8') as fp:
        json.dump(data,fp,ensure_ascii=False,indent=2)
        fp.write('\n')
    print(data['status'], data['total_binary_candidates'], data['total_two_preimage_classes'])
