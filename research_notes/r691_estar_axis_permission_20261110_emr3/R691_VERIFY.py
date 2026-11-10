#!/usr/bin/env python3
"""R691 exact positive-source BRC static-axis mask verifier.
Reuses R690 E* V17 signed native squares and group convolution semantics.
Only integer counts and exact Fraction values; branch labels are (i,j,si,sj).
"""
from collections import Counter, defaultdict
from itertools import permutations, product
from fractions import Fraction
from pathlib import Path
import json

G=sorted(permutations(range(3)))
ID=(0,1,2); TAU=(0,2,1); C=(1,2,0); C2=(2,0,1)
E=(0,2,4); O=(1,3,5)
TAB={(0,0):(0,1,2),(1,0):(0,1,3),(2,0):(0,1,4),
     (0,1):(0,2,3),(1,1):(1,2,3),(2,1):(0,1,3)}

def phase(z):
    return sum(z[i] for i in E)%3,sum(z[i] for i in O)%2
def move(f,s,t):
    old=next(iter(set(s)-set(t)))
    new=next(iter(set(t)-set(s)))
    return tuple(new if x==old else x for x in f)
def sq(z,i,j,si,sj):
    initial=z
    f=TAB[phase(z)]
    for axis,d in ((i,si),(j,sj),(i,-si),(j,-sj)):
        v=list(z); v[axis]+=d; nxt=tuple(v)
        f=move(f,TAB[phase(z)],TAB[phase(nxt)])
        z=nxt
    assert z==initial
    return tuple(TAB[phase(z)].index(v) for v in f)
def prod(q,p):
    return tuple(q[x] for x in p)
def group(support):
    seen={ID}; pending=[ID]
    for p in pending:
        for q in support:
            r=prod(q,p)
            if r not in seen:
                seen.add(r); pending.append(r)
    return frozenset(seen)
def axes(mask):
    return tuple(i for i in range(6) if mask&(1<<i))
def name(g):
    return ''.join(map(str,g))
def group_name(h):
    return {1:'TRIVIAL',2:'C2',3:'A3',6:'S3'}[len(h)]

def verify():
    base={}
    for a,b in product(range(3),range(2)):
        z=(a,b,0,0,0,0)
        base[a,b]={(i,j,si,sj):sq(z,i,j,si,sj)
            for i in range(6) for j in range(i+1,6)
            for si,sj in product((-1,1),repeat=2)}
        assert len(base[a,b])==60
    evidence={
        'schema':'R691_ESTAR_STATIC_AXIS_PERMISSION_BRC_V1',
        'date':'2026-11-10',
        'frozen_R462_pin':'18783e01e3646c72b7aab3b16d3f565e83e6446f',
        'frozen_scientific_source':'a72226e2430ffa4786321ac86e7f0c599d5f0389',
        'E_star_source':'028d5612f9562bc22ac7593f03426fc32b1a9259',
        'reused_R690':'513309982f816b1e3b89d513e00fecd010be7c33',
        'scope':'Static U subset signed 6 native axes, four-step returning squares, 6 starts x 64 masks',
        'observer':'full V17 S3 group; positive BRC sources preserve signed square labels',
        'kernel':{}, 'census':{}, 'witness':{}
    }
    for a in range(3):
        census=defaultdict(Counter)
        for mask in range(64):
            U=axes(mask); n=len(U)
            ee=set(U)&set(E); oo=set(U)&set(O)
            s=len(ee)*(len(ee)-1)//2+len(oo)*(len(oo)-1)//2
            m=len(ee)*len(oo)
            L=sum(i<j for i in ee for j in oo)
            R=m-L
            expected={
                0:Counter({ID:4*s,TAU:2*m,C:2*R,C2:2*L}),
                1:Counter({ID:4*s+2*m,C:2*L,C2:2*R}),
                2:Counter({ID:4*s+2*m,TAU:2*m})
            }[a]
            expected=+expected  # remove zero entries
            for b in range(2):
                src={k:v for k,v in base[a,b].items()
                    if k[0] in U and k[1] in U}
                count=Counter(src.values())
                assert count==expected,(a,b,U,count,expected)
                assert len(src)==4*n*(n-1)//2
                h=group(count)
                label=group_name(h)
                assert label==('TRIVIAL' if m==0 else ('S3','A3','C2')[a])
                # Independent bounded word exploration of all enabled macro sources
                reached={ID}
                for _ in range(6):
                    reached={prod(q,p) for p in reached for q in count} if count else reached
                assert reached==h
            census[n][label]+=1
            evidence['kernel'][f'{a}:{mask}']={
                'axes':U,'s':s,'m':m,'L':L,'R':R,
                'n':4*n*(n-1)//2,
                'counts':{name(g):expected[g] for g in G if expected[g]},
                'reachable_group':label}
        evidence['census'][str(a)]={str(n):dict(census[n]) for n in range(7)}
        assert [census[n][('S3','A3','C2')[a]] for n in range(7)]==[0,0,9,18,15,6,1]
        assert [census[n]['TRIVIAL'] for n in range(7)]==[1,6,6,2,0,0,0]
    # Match the whole-mask native R690 kernel and support the observer counterexample.
    assert evidence['kernel']['0:63']['counts']=={'012':24,'021':18,'120':6,'201':12}
    assert evidence['kernel']['1:63']['counts']=={'012':42,'120':12,'201':6}
    assert evidence['kernel']['2:63']['counts']=={'012':42,'021':18}
    for a in range(3):
        u01=evidence['kernel'][f'{a}:3']
        u12=evidence['kernel'][f'{a}:6']
        u02=evidence['kernel'][f'{a}:5']
        assert u01['reachable_group']==u12['reachable_group']
        assert u01['counts']!=u12['counts'] if a!=2 else True
        assert u02['reachable_group']=='TRIVIAL'
        evidence['witness'][str(a)]={'U01':u01,'U12':u12,'U02':u02}
    # Exact rational normalized positive BRC kernel: four sources U={0,1}.
    assert {k:Fraction(v,4) for k,v in evidence['kernel']['0:3']['counts'].items()}=={
        '021':Fraction(1,2),'201':Fraction(1,2)}
    # A static signed-direction mask enables Q iff both axes admit both signs.
    directed=defaultdict(Counter)
    for bits in range(1<<12):
        U=tuple(i for i in range(6)
            if bits&(1<<(2*i)) and bits&(1<<(2*i+1)))
        has_mixed=any(i in E for i in U) and any(j in O for j in U)
        directed[len(U)]['FULL' if has_mixed else 'TRIVIAL']+=1
    assert [directed[n]['FULL'] for n in range(7)]==[0,0,729,486,135,18,1]
    assert [directed[n]['TRIVIAL'] for n in range(7)]==[729,1458,486,54,0,0,0]
    assert sum(v['FULL'] for v in directed.values())==37**2==1369
    assert sum(v['TRIVIAL'] for v in directed.values())==2727
    evidence['directed_static_masks']={str(n):dict(directed[n]) for n in range(7)}
    evidence['verification_marker']='R691_ESTAR_AXIS_PERMISSION_BRC_EXACT_PASS'
    Path(__file__).with_name('R691_EVIDENCE.json').write_text(
        json.dumps(evidence,indent=2,ensure_ascii=False,sort_keys=True)+'\n',encoding='utf-8')
    print(evidence['verification_marker'])

if __name__=='__main__':
    verify()
