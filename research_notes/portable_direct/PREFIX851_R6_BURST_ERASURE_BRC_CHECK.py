#!/usr/bin/env python3
"""Exact finite certificates for PREFIX-851 named BRC burst-erasure readout.
Only the declared auxiliary positive-integer BRC Q observer is considered.
No native X6 transition or physical model is computed.
"""
from itertools import combinations, product
from math import comb
import json, hashlib
from pathlib import Path


def signed_witnesses(p, r):
    """All allowed nonzero integer differences with at most 2r changed names.
    Values are indexed by absolute differences, with shortest-support witnesses.
    A witness (x,y,z) has dist(x,y)<=2r and x,z,y in the same r-ball.
    """
    differences = {}
    for k in range(1, min(p, 2*r)+1):
        for indices in combinations(range(p), k):
            for signs in product((-1, 1), repeat=k):
                x = sum(1 << i for i,s in zip(indices, signs) if s == 1)
                y = sum(1 << i for i,s in zip(indices, signs) if s == -1)
                d = abs(x-y)
                if not d: raise AssertionError('distinct binary powers cannot cancel')
                if d not in differences or k < differences[d][0]:
                    flipmask = sum(1 << i for i in indices[:k//2])
                    z = x ^ flipmask
                    assert (x^z).bit_count() <=r and (y^z).bit_count() <=r
                    differences[d] = (k,x,y,z)
    return differences


def exclusions(differences):
    bad = {}
    for d, record in differences.items():
        i = 1
        while i*i <= d:
            if d % i == 0:
                for q in (i, d//i):
                    if q>1 and q%2:
                        if q not in bad or record[0]<bad[q]['support']:
                            bad[q] = {'difference':d,'support':record[0],
                                      'x':record[1],'y':record[2],'common_old_state':record[3]}
            i += 1
    return bad


def brute_injectivity(p,r,q):
    # Independent direct exhaustive check: every old state and every reachable state.
    for old in range(1<<p):
        observed={}
        for x in range(1<<p):
            if (x^old).bit_count() <=r:
                residue=x%q
                if residue in observed:
                    return False,(old,observed[residue],x)
                observed[residue]=x
    return True,None


def exact_case(p,r):
    d = signed_witnesses(p,r)
    bad = exclusions(d)
    q=3
    while q in bad: q+=2
    N=1<<p
    assert q<=N+1
    if 2*r>=p:
        assert q==N+1
    if 2*r==p-1:
        assert q==N-1
    sphere=sum(comb(p,i) for i in range(min(p,r)+1))
    assert q>=sphere
    if p<=8:
        mods = list(range(3,q+1,2)) if p<=6 else [q,max(3,q-2)]
        for mod in mods:
            actual,witness=brute_injectivity(p,r,mod)
            expected=mod not in bad
            assert actual==expected,(p,r,mod,actual,expected,witness)
    return {
        'p':p,'erased_heartbeats':r,'possible_named_states':N,
        'hamming_ball_size':sphere,'minimal_fixed_odd_raw_modulus':q,
        'minimal_fixed_port_bits':(q-1).bit_length(),
        'signed_difference_count':len(d),
        'smaller_odd_moduli_excluded':sum(1 for x in range(3,q,2) if x in bad),
        'excluded_modulus_witness_samples':{str(m):bad[m] for m in sorted(set([3,5,7,q-2]) & set(range(3,q,2)))},
        'excluded_modulus_witness_sha256':hashlib.sha256(json.dumps({str(m):bad[m] for m in range(3,q,2)},sort_keys=True,separators=(',',':')).encode()).hexdigest()
    }


def main():
    cases=[]
    for p in range(1,14):
        for r in range(1,min(3,p)+1):
            cases.append(exact_case(p,r))
    examples=[]
    for p,r in [(5,1),(5,2),(5,3),(6,2),(7,2),(7,3),(8,2),(9,2),(10,2),(13,2),(13,3)]:
        a=next(t for t in cases if t['p']==p and t['erased_heartbeats']==r)
        examples.append({k:a[k] for k in ['p','erased_heartbeats','hamming_ball_size','minimal_fixed_odd_raw_modulus','minimal_fixed_port_bits']})
    result={'schema':'PREFIX851_R6_EXACT_BRC_BURST_RECOVERY_V1',
            'model':'positive integer BRC Q-only modular named-state observer; x_i in {0,1}; each step flips <=1 bit; a=2,b=1; c_t=2^floor(t/2); one post-burst read; known pre-burst state',
            'scope':'author finite exact enumeration, mathematical proof separate; no native X6 correspondence',
            'finite_coverage':'p=1..13, r=1..min(3,p); direct old-state crosscheck for all odd q<=qopt if p<=6, and at qopt and qopt-2 if 7<=p<=8',
            'case_count':len(cases), 'examples':examples,'cases':cases,
            'status':'ALL_EXACT_ASSERTIONS_PASSED'}
    # Stable digest of all exclusion witnesses for lightweight independent integrity check.
    witness_blob=json.dumps([c['excluded_modulus_witness_sha256'] for c in cases],sort_keys=True,separators=(',',':')).encode()
    result['witnesses_sha256']=hashlib.sha256(witness_blob).hexdigest()
    path=Path(__file__).with_name('PREFIX851_R6_BURST_ERASURE_BRC_RESULTS.json')
    with open(path,'w',encoding='utf-8') as f:json.dump(result,f,ensure_ascii=False,indent=2)
    print(json.dumps({'cases':len(cases),'witness_hash':result['witnesses_sha256'],'examples':examples,'status':result['status'],'bytes':len(open(path,'rb').read())},indent=2))

if __name__=='__main__':main()
