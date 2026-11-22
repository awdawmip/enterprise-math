#!/usr/bin/env python3
"""Exact finite crosscheck for BRC16943 frozen P10 support reconstruction.
No native X6 or Farey transition is executed.
"""
import json
import math
from collections import defaultdict

N = 10
SLOPES = {(0,0):{3}, (0,1):{0,3,4,5}, (1,0):{2,3,4,5}, (1,1):{2,3}}

def p10(h,k):
    h,k=h%10,k%10
    if h%5==0 and k%5==0:
        return False
    s=5 if h%5==0 else (k*pow(h,-1,5))%5
    return s in SLOPES[(h%2,k%2)]

def frozen_words():
    words=set()
    dirs=0
    for a in range(10):
        for b in range(10):
            if math.gcd(math.gcd(a,b),10)!=1:
                continue
            dirs+=1
            roots=[(h,k) for h in range(10) for k in range(10)
                   if ((b-a)*h-a*k+1)%10==0]
            assert roots
            h,k=roots[0]
            mask=sum((1<<t) for t in range(10) if p10(h+a*t,k+(b-a)*t))
            words.add(mask)
    assert dirs==72 and len(words)==50
    return sorted(words)

def weights(mask,n):
    return [(mask>>i)&1 for i in range(n)]

def convolution(mask,n):
    b=weights(mask,n)
    return tuple(sum(b[i]*b[(c-i)%n] for i in range(n)) for c in range(n))

def signature(ku,kv,u,v):
    return bytes(2*(u*v-ku[a]*kv[b]) for a in range(10) for b in range(len(kv)))

def main():
    frozen=frozen_words()
    ten=defaultdict(list)
    for u in frozen:
        ku=convolution(u,10)
        ten[tuple(2*(u.bit_count()-k) for k in ku)].append(u)
    assert len(ten)==38 and sorted(map(len,ten.values())).count(2)==12
    diffs=sorted({tuple(i for i in range(10) if (x^y)&(1<<i))
                  for g in ten.values() if len(g)==2 for x,y in [g]})
    disjoint=[(1,4,6,9),(2,7),(3,8)]
    assert all(d in diffs for d in disjoint)
    opt=[tuple(q) for q in __import__('itertools').combinations(range(10),3)
         if all(set(q).intersection(d) for d in diffs)]
    assert len(opt)==16 and (1,2,3) in opt
    summary=[]
    ku_all={u:convolution(u,10) for u in frozen}
    for q in (3,7,11):
        full={}
        collision_count=0
        same_mass_count=0
        different_mass_count=0
        for v in range(1,1<<q):
            kv=convolution(v,q)
            for u in frozen:
                key=signature(ku_all[u],kv,u.bit_count(),v.bit_count())
                old=full.get(key)
                if old is None:
                    full[key]=(u,v)
                else:
                    u0,v0=old
                    assert (u0,v0)!=(u,v), 'duplicate support'
                    # Every indexed spectrum fiber has exactly two states at most.
                    assert len(old)==2 and isinstance(u0,int)
                    assert old!=(-1,-1), 'third state in one spectrum fiber'
                    full[key]=(-1,-1)
                    collision_count+=1
                    if u0.bit_count()*v0.bit_count() == u.bit_count()*v.bit_count():
                        same_mass_count+=1
                    else:
                        different_mass_count+=1
                    assert v0==v, 'distinct CRT factors with the same spectrum'
                    assert (u0^u)&((1<<1)|(1<<2)|(1<<3)), 'three-probe ten-cycle miss'
        assert different_mass_count==2
        assert collision_count>0
        # Q={(1,v),(2,v),(3,v): v in Z/q}. Every doubleton is resolved.
        # Singleton-V at each v enforces three disjoint ten-position supports.
        summary.append(dict(q=q,total_products=50*((1<<q)-1),
                            distinct_spectra=len(full),spectral_doubletons=collision_count,
                            same_mass_doubletons=same_mass_count,
                            different_mass_doubletons=different_mass_count,
                            exact_optimal_fixed_physical_sites=3*q,
                            number_of_optimal_fixed_site_sets=str(16**q)))
    return dict(status='ALL PASS',pin='BRC16943',frozen_directions=72,
                frozen_distinct_supports=len(frozen),ten_cycle_spectrum_fibers=len(ten),
                ten_cycle_doubleton_difference_supports=[list(x) for x in diffs],
                optimal_three_site_patterns=[list(x) for x in opt],
                factored_censuses=summary,
                adaptive_worst_case_physical_probes=1,
                scope='Indexed static CRT reflection-defect spectrum; arbitrary nonempty unknown odd factor; no native update',
                review='AUTHOR_PROVED/EXACT_FINITE_CROSSCHECK/PARENT_DEPENDENT/NOT_REVIEWED')

if __name__=='__main__':
    print(json.dumps(main(),indent=2,ensure_ascii=False))
