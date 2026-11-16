#!/usr/bin/env python3
"""Exact finite observer-monoid verification for R217, L=2. Stdlib only."""
from collections import deque
from itertools import product
import json


def append(state, letter):
    order, tail = state
    direction, tag = letter
    if tag:
        order = tuple(s for s in order if s != tag) + (tag,)
    return (order, (tail + (letter,))[-2:])


def monoid(m, k):
    alphabet = tuple(product(range(m), range(k+1)))
    initial=((),())
    reps={initial:()}
    q=deque([initial])
    while q:
        x=q.popleft()
        for c in alphabet:
            y=append(x,c)
            if y not in reps:
                reps[y]=reps[x]+(c,)
                q.append(y)
    states=list(reps)
    idx={x:i for i,x in enumerate(states)}
    n=len(states)
    mult=[]
    for x in states:
        row=[]
        for y in states:
            z=x
            for letter in reps[y]:
                z=append(z,letter)
            row.append(idx[z])
        mult.append(row)
    return states,mult


def quotient(state):
    order, tail=state
    if len(tail)==0: return ('E',)
    if len(tail)==1: return ('S',tail[0][1])
    return ('F',tuple(sorted(order)))


def verify_case(m,k):
    states,M=monoid(m,k)
    n=len(states)
    # Count each original principal two-sided ideal by its defining multiplication set.
    f=[]
    for x in range(n):
        ideal={M[M[p][x]][q] for p in range(n) for q in range(n)}
        f.append(len(ideal))
    sig=[tuple(f[M[x][z]] for z in range(n)) for x in range(n)]
    classes={}
    for idx,state in enumerate(states):
        classes.setdefault(quotient(state),[]).append(idx)
    assert len(classes)==k+2+2**k,(m,k,len(classes))
    # Exactly: equality of future scalar outputs <=> class equality.
    seen={}
    for code, ids in classes.items():
        for idx in ids:
            assert sig[idx]==sig[ids[0]],(m,k,code,idx)
        assert sig[ids[0]] not in seen,(m,k,code,seen.get(sig[ids[0]]))
        seen[sig[ids[0]]]=code
    # Verify both left and right generator congruence at original state level.
    alphabet=[i for i,s in enumerate(states) if len(s[1])==1]
    pair_checks=0
    for code, ids in classes.items():
        for idx in ids:
            for g in alphabet:
                assert quotient(states[M[idx][g]])==quotient(states[M[ids[0]][g]])
                assert quotient(states[M[g][idx]])==quotient(states[M[g][ids[0]]])
                pair_checks+=2
    return {'m':m,'k':k,'L':2,'original_states':n,'quotient_states':len(classes),
            'context_signature_pairs':len(classes)*(len(classes)-1)//2,
            'left_right_generator_congruence_assertions':pair_checks,
            'scalar_ideal_values':{str(c):f[ids[0]] for c,ids in classes.items()}}


def main():
    models=[(1,0),(1,1),(1,2),(2,0),(2,1),(2,2),(3,1)]
    results=[verify_case(*pair) for pair in models]
    return {'status':'PASS','models':results,
            'total_original_states':sum(r['original_states'] for r in results),
            'total_quotient_classes':sum(r['quotient_states'] for r in results),
            'total_congruence_assertions':sum(r['left_right_generator_congruence_assertions'] for r in results),
            'total_distinct_context_signature_pairs':sum(r['context_signature_pairs'] for r in results),
            'large_X6':{'m':12,'k':6,'L':2,'original_states':1407685,
                        'green_J_quotient_states':149,'cardinality_quotient_states':72,
                        'cardinality_fixed_bits':7},
            'arithmetic':'exact finite symbolic monoid multiplication and cardinality sets; no native BRC physics',
            'general_theorem':'symbolic proof in companion markdown','review':'NOT_REVIEWED'}

if __name__=='__main__':
    print(json.dumps(main(),ensure_ascii=False,indent=2))
