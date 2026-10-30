#!/usr/bin/env python3
"""Exact source/observer checks for TWO declared finite X6 candidate operations.

T(z)=z+p^e*(z6^p)*e1 and U(z)=z+delta, mod p^L. Not native X6.
Two probing words T and T∘U are separate source experiments, not one path.
"""
from collections import defaultdict
from hashlib import sha256
from json import dumps
from pathlib import Path


def case(p,L,e):
    N=p**L
    n=L-e
    modH=p**n
    k=max(1,n-1)
    classes=defaultdict(list)
    T_only=defaultdict(list)
    for h in range(N):
        a=pow(h,p,modH)
        b=pow((h+1)%N,p,modH)
        classes[(a,b)].append(h)
        T_only[a].append(h)
    assert len(classes)==p**k
    assert len({h%p**k for h in range(N)})==p**k
    assert all(len(vals)==p**(L-k) for vals in classes.values())
    assert all(len(set(h%p**k for h in vals))==1 for vals in classes.values())
    assert len({(a,b) for a,b in classes})==p**k
    assert all(len(set((pow(h,p,modH),pow((h+1)%N,p,modH)) for h in vals))==1
               for vals in classes.values())
    for h in range(N):
        for h2 in [ (h+p**k)%N, (h+2*p**k)%N ]:
            assert pow(h2,p,modH)==pow(h,p,modH)
            assert pow((h2+1)%N,p,modH)==pow((h+1)%N,p,modH)

    # Finite-source detection of the strict refinement induced by adding U.
    strict=(n>=3)
    assert (len(T_only)<len(classes))==strict
    split_witness=None
    if strict:
        d=p**((n+p-1)//p)
        h,h2=0,d%N
        assert pow(h,p,modH)==pow(h2,p,modH)==0
        assert pow((h+1)%N,p,modH)!=pow((h2+1)%N,p,modH)
        assert h%p**k!=h2%p**k
        split_witness=dict(h=h,h_prime=h2,power_before=0,
            power_after_U=(pow(1,p,modH),pow((h2+1)%N,p,modH)))

    # Actual six-coordinate operations + original five-factor observer,
    # not just precomputed power signatures. Exhaust all h for three q rows.
    updates=0
    rows=0
    for qseed in [0,1,N-1]:
        q=tuple((qseed+(i+1)**2)%N for i in range(5))
        obs_map=defaultdict(set)
        for h in range(N):
            z=tuple((t+h)%N for t in q)+(h,)
            def O(v): return tuple((v[i]-v[5])%N for i in range(5))
            def T(v): return ((v[0]+p**e*pow(v[5],p,N))%N,)+v[1:]
            def U(v): return tuple((u+1)%N for u in v)
            assert O(z)==q
            a=O(T(z)); b=O(T(U(z)))
            updates+=3  # one T, one U and one T after U
            assert a[0]==(q[0]+p**e*pow(h,p,modH))%N
            assert b[0]==(q[0]+p**e*pow((h+1)%N,p,modH))%N
            assert a[1:]==q[1:] and b[1:]==q[1:]
            obs_map[(a,b)].add(h%p**k)
            rows+=1
        assert len(obs_map)==p**k
        assert all(len(v)==1 for v in obs_map.values())

    return dict(p=p,L=L,e=e,n=n,height_source_count=N,
                minimum_congruence_memory_digits=k,
                T_only_future_classes=len(T_only),
                T_and_U_future_classes=len(classes),
                all_two_operator_fibers_have_size=p**(L-k),
                two_operator_strict_refinement=strict,
                actual_source_rows=rows,actual_declared_updates=updates,
                split_witness=split_witness)


def main():
    cases=[]
    for p,maxL in [(3,7),(5,5),(7,4),(11,3)]:
        for L in range(2,maxL+1):
            for e in range(1,L):
                cases.append(case(p,L,e))
    assert len(cases)==40
    raw={'schema':'D25_X6_TWO_OPERATOR_HEIGHT_QUOTIENT_AUTHOR_CHECK_V1',
         'status':'AUTHOR_EXACT_CHECKED_NOT_NATIVE',
         'claims':'Finite declared T/U candidate, exhaustive heights and two probing words, no native time or experiment',
         'pass':True,'configuration_count':len(cases),
         'actual_source_rows':sum(c['actual_source_rows'] for c in cases),
         'actual_declared_updates':sum(c['actual_declared_updates'] for c in cases),
         'cases':cases}
    dest=Path(__file__).with_name('d25_x6_two_operator_height_closure_author_check_20261030.json')
    dest.write_text(dumps(raw,sort_keys=True,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS cases=',len(cases),'source_rows=',raw['actual_source_rows'],
          'updates=',raw['actual_declared_updates'], 'json_sha256=',sha256(dest.read_bytes()).hexdigest())
    for p,L,e in [(3,5,1),(5,4,1),(3,3,1)]:
        c=next(x for x in cases if (x['p'],x['L'],x['e'])==(p,L,e))
        print('example',(p,L,e),'T_classes',c['T_only_future_classes'],
              'TU_classes',c['T_and_U_future_classes'],
              'fiber_size',c['all_two_operator_fibers_have_size'],
              'witness',c['split_witness'])

if __name__=='__main__': main()
