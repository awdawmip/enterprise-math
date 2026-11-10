#!/usr/bin/env python3
"""R689: exact native-X6 E* plaquette-holonomy & BRC branch verifier.
All arithmetic is integer or fractions.Fraction; no non-BRC phase/heartbeat arithmetic.
"""
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product, permutations
from json import dumps
from pathlib import Path

N=6; ID=(0,1,2)
TABLE={(0,0):(0,1,2),(1,0):(0,1,3),(2,0):(0,1,4),
       (0,1):(0,2,3),(1,1):(1,2,3),(2,1):(0,1,3)}
EVEN=(0,2,4); ODD=(1,3,5)

def phase(z):
    return (sum(z[k] for k in EVEN)%3,sum(z[k] for k in ODD)%2)
def triad(z): return TABLE[phase(z)]
def step(z,i,sign):
    assert 0<=i<N and sign in (-1,1)
    out=list(z);out[i]+=sign;return tuple(out)
def move(F,S,T):
    assert set(F)==set(S) and len(set(S)&set(T))==2
    gone=next(iter(set(S)-set(T)))
    arrived=next(iter(set(T)-set(S)))
    return tuple(arrived if x==gone else x for x in F)
def transport(z,path,F=None):
    start=z;S=triad(z)
    F=S if F is None else F
    for i,sign in path:
        zz=step(z,i,sign)
        F=move(F,triad(z),triad(zz));z=zz
    return z,F
def closed_holonomy(z,path):
    end,F=transport(z,path)
    assert end==z
    S=triad(z)
    return tuple(S.index(x) for x in F)
def square(i,j,si,sj):
    return ((i,si),(j,sj),(i,-si),(j,-sj))
def product_perm(q,p):return tuple(q[x] for x in p)
def inverse_perm(p):return tuple(p.index(i) for i in ID)
def parity(p):return (-1)**sum(p[i]>p[j] for i in ID for j in range(i+1,3))
def class_label(p):
    if p==ID:return 'identity'
    return 'transposition' if parity(p)==-1 else '3cycle'

def verify():
    full=Counter();cross=Counter();same=Counter();per_phase={};checks=0
    for a,b in product(range(3),range(2)):
        z=(a,b,0,0,0,0)
        counts=Counter()
        for i in range(N):
            for j in range(i+1,N):
                for si,sj in product((-1,1),repeat=2):
                    path=square(i,j,si,sj)
                    p=closed_holonomy(z,path)
                    rev=square(j,i,sj,si)
                    assert closed_holonomy(z,rev)==inverse_perm(p)
                    assert sum(1 for ax,_ in path if ax==i)==2
                    for f in permutations(triad(z)):
                        z_end,ff=transport(z,path,f)
                        assert z_end==z
                        old=tuple(triad(z).index(x) for x in f)
                        got=tuple(triad(z).index(x) for x in ff)
                        assert got==product_perm(p,old)
                        checks+=1
                    counts[p]+=1;full[p]+=1
                    if i%2==j%2:
                        same[p]+=1
                        assert p==ID
                    else:cross[p]+=1
        assert sum(counts.values())==60
        per_phase[f'{a},{b}']={''.join(map(str,p)):v for p,v in sorted(counts.items())}
    assert checks==2160
    assert sum(full.values())==360 and sum(cross.values())==216 and sum(same.values())==144
    assert same==Counter({ID:144})
    assert cross==Counter({ID:72,(0,2,1):72,(2,0,1):36,(1,2,0):36})
    assert full==Counter({ID:216,(0,2,1):72,(2,0,1):36,(1,2,0):36})

    expected={0:{-1:(0,2,1),+1:(2,0,1)},
              1:{-1:(1,2,0),+1:ID},
              2:{-1:ID,+1:(0,2,1)}}
    formulas=0
    for a,b in product(range(3),range(2)):
        z=(a,b,0,0,0,0)
        for i in EVEN:
            for j in ODD:
                for si,sj in product((-1,1),repeat=2):
                    p=closed_holonomy(z,square(i,j,si,sj))
                    assert p==expected[a][si]
                    assert closed_holonomy(z,square(j,i,sj,si))==inverse_perm(p)
                    formulas+=2
    assert formulas==6*9*4*2

    z0=(0,)*N
    generators=Counter(closed_holonomy(z0,square(i,j,si,sj))
                       for i in range(N) for j in range(i+1,N)
                       for si,sj in product((-1,1),repeat=2))
    assert generators==Counter({ID:24,(0,2,1):18,(2,0,1):12,(1,2,0):6})
    state=Counter({ID:1});spectrum={}
    for k in (1,2):
        nxt=Counter()
        for p,n in state.items():
            for q,m in generators.items(): nxt[product_perm(q,p)]+=n*m
        state=nxt
        spectrum[str(k)]={''.join(map(str,p)):n for p,n in sorted(state.items())}
        assert sum(state.values())==60**k
    assert spectrum['2']=={'012':1044,'021':864,'102':324,'120':432,'201':612,'210':324}
    assert len(state)==6
    masses={p:Fraction(n,3600) for p,n in state.items()}
    assert sum(masses.values(),Fraction(0,1))==1
    assert all(m>0 for m in masses.values())
    assert 3600==60*60
    data={
      'schema':'R689_NATIVE_X6_PLAQUETTE_CURVATURE_BRC_V1',
      'date':'2026-11-10',
      'frozen_task_science':'RS-X6-TRIADIC-CLOSURE-DYNAMICS@a72226e2430ffa4786321ac86e7f0c599d5f0389',
      'lineage_pin':'R462@18783e01e3646c72b7aab3b16d3f565e83e6446f',
      'parent_candidate':'R687@028d5612f9562bc22ac7593f03426fc32b1a9259',
      'native_scope':'Z^6 affine torsor; signed native one-axis steps, typed E* 3-force candidate',
      'phase_classes':6,'unordered_axis_pairs':15,'signed_square_orientations_per_pair':4,
      'based_phase_square_cases':360,'initial_frame_checks':checks,
      'same_parity_square_cases':sum(same.values()),
      'mixed_parity_square_cases':sum(cross.values()),
      'mixed_parity_holonomy':{''.join(map(str,p)):n for p,n in sorted(cross.items())},
      'full_holonomy':{''.join(map(str,p)):n for p,n in sorted(full.items())},
      'even_first_formula':{str(a):{str(si):list(p) for si,p in ps.items()} for a,ps in expected.items()},
      'root_60_macro_holonomy':{''.join(map(str,p)):n for p,n in sorted(generators.items())},
      'root_3600_two_macro_holonomy':spectrum['2'],
      'root_3600_two_macro_masses':{''.join(map(str,p)):f'{m.numerator}/{m.denominator}' for p,m in sorted(masses.items())},
      'smallest_full_S3_support_square_macro_steps':2,
      'BRC_positive_mass_total':'1/1',
      'arithmetics':'integer/Counter and exact fractions.Fraction',
      'analytic_scope':'all native X6 coordinate loops under R687 E* lookup; same-parity closed sublattice paths are flat; group holonomy generated by transported mixed-parity square defects',
      'limitations':'Candidate E* only. No native port/V29 or source-derived V39 j established. No formal CLAIM/Driver admission.',
      'verification_marker':'R689_NATIVE_X6_PLAQUETTE_CURVATURE_BRC_EXACT_PASS',
      'per_phase_squares':per_phase,
    }
    Path(__file__).with_name('R689_EVIDENCE.json').write_text(dumps(data,indent=2,sort_keys=True,ensure_ascii=False)+'\n',encoding='utf-8')
    print(data['verification_marker'])
    print('all',dict(full),'root',dict(generators),'k2',spectrum['2'])

if __name__=='__main__':verify()
