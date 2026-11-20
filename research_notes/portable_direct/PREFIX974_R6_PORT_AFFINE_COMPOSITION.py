#!/usr/bin/env python3
"""PREFIX-974: affine bit-port quotient, positive BRC port relation counts.
Pure integer exact calculations; no native X6 or physical dynamics execution.
"""
from bisect import bisect_left
from collections import Counter, defaultdict
from hashlib import sha256
from math import gcd
import json

FROZEN_PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
EXPECTED = {1:(442,614,'ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71'),
            3:(839,1286,'1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3'),
            5:(3,3,'c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b')}

def masks(p):
    out = defaultdict(lambda:[0,0])
    for i in range(p):
        for j in range(p):
            out[(1<<i)-(1<<j)][0] |= 1<<j
            out[(1<<i)+(1<<j)][1] |= 1<<j
    return {c:tuple(z) for c,z in out.items()}

def ports(z,x):
    plus,minus=z
    return (plus & ~x) | (minus & x)

def pair_metrics(p, l, r):
    equality=(l&r).bit_count()
    next_port=(l & ((r>>1)|((r&1)<<(p-1)))).bit_count()
    return equality,next_port

def ceildiv(a,b):
    return -((-a)//b)

def bounded_candidates(p,k,m,ms):
    H=1<<(p-1);lo=H+1;hi=2*H-1
    right={r:sorted((c,ms[c]) for c in ms if c%2==r) for r in (0,1)}
    bucket_cache={}; left_cache={}
    for t in range(1,2*k+1):
        g=gcd(k,t); par=(1-t)%2; d=2*t-k*m; q=abs(d)//g
        if (g,par) not in left_cache:
            left_cache[(g,par)]=[(c,ms[c]) for c in sorted(ms) if c%g==0 and c%2==par]
        key=(q,t%2)
        if key not in bucket_cache:
            table=defaultdict(list)
            for C,z in right[t%2]:table[C%q].append((C,z))
            bucket_cache[key]=table
        inv=pow(k//g,-1,q) if q>1 else 0
        dl,dh=sorted((d*lo,d*hi))
        for c,cm in left_cache[(g,par)]:
            lower=max(ceildiv((k+2)*c+dl,k),ceildiv((t+m)*c+dl,t))
            upper=min(((k+2)*c+dh)//k,((t+m)*c+dh)//t)
            if lower>upper:continue
            bucket=bucket_cache[key][((k+2)*(c//g)*inv)%q]
            for C,Cm in bucket[bisect_left(bucket,(lower,)):bisect_left(bucket,(upper+1,))]:
                bn=k*C-(k+2)*c;an=t*C-(t+m)*c
                assert bn%d==an%d==0
                b=bn//d;a=an//d
                assert lo<=a<=hi and lo<=b<=hi and a%2 and b%2
                yield (a,b,t,t+m,c,C,cm,Cm)

def mask_statistics(p,k,m):
    ms=masks(p)
    hist=Counter(); pair_set=set(); port_relation=Counter(); joint_masks=Counter(); candidate_count=0
    for a,b,t,T,c,C,cm,Cm in bounded_candidates(p,k,m,ms):
        candidate_count+=1
        if a==b:continue
        left=ports(cm,k*a);right=ports(Cm,(k+2)*a)
        mass=left.bit_count()*right.bit_count()
        eq,nxt=pair_metrics(p,left,right)
        hist[mass]+=1
        port_relation['equal']+=eq
        port_relation['next_cyclic']+=nxt
        port_relation['all_named']+=mass
        port_relation['port_product_zero']+=int(mass==0)
        if mass:pair_set.add((a,b))
        joint_masks[(left,right)]+=1
    return dict(candidate_count=candidate_count,nondiagonal=sum(hist.values()),named=port_relation['all_named'],
                pair_count=len(pair_set),equal_port=port_relation['equal'],next_cyclic=port_relation['next_cyclic'],
                zero_mass=port_relation['port_product_zero'],
                weight_histogram={str(w):n for w,n in sorted(hist.items())},
                distinct_joint_port_masks=len(joint_masks))

def named_reference(p,k,m):
    sd=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1,1):sd[(1<<i)-s*(1<<j)].append((i,j,s))
    sides={r:sorted((c,sl) for c,sl in sd.items() if c%2==r) for r in (0,1)}
    H=1<<(p-1);lo=H+1;hi=2*H-1
    named=[]
    for t in range(1,2*k+1):
        d=2*t-k*m;tab=defaultdict(list)
        for C,Cs in sides[t%2]:tab[(k*C)%abs(d)].append((C,Cs))
        for c,cs in sides[(1-t)%2]:
            for C,Cs in tab[((k+2)*c)%abs(d)]:
                bn=k*C-(k+2)*c
                if bn%d:continue
                b=bn//d
                if not(lo<=b<=hi):continue
                an=t*C-(t+m)*c
                if an%d:continue
                a=an//d
                if not(lo<=a<=hi) or a==b:continue
                L=[(i,j) for i,j,s in cs if ((k*a>>j)&1)==(1 if s==-1 else 0)]
                R=[(I,J) for I,J,S in Cs if (((k+2)*a>>J)&1)==(1 if S==-1 else 0)]
                for i,j in L:
                    for I,J in R:
                        assert (((k*a)^(1<<j))-(1<<i))==t*b
                        assert ((((k+2)*a)^(1<<J))-(1<<I))==(t+m)*b
                        named.append((a,b,t,t+m,i,j,I,J))
    named.sort()
    return named

def direct_small(p,k,m):
    H=1<<(p-1);lo=H+1;hi=2*H-1
    named=[]
    for a in range(lo,hi+1,2):
        L=defaultdict(list);R=defaultdict(list)
        for i in range(p):
            for j in range(p):
                x=((k*a)^(1<<j))-(1<<i)
                y=(((k+2)*a)^(1<<j))-(1<<i)
                if x>0:L[x].append((i,j))
                if y>0:R[y].append((i,j))
        for x,ls in L.items():
            for y,rs in R.items():
                diff=y-x
                if diff<=0 or diff%m:continue
                b=diff//m
                if b==a or not(lo<=b<=hi) or not(b&1) or x%b:continue
                t=x//b
                if t<1:continue
                for i,j in ls:
                    for I,J in rs:named.append((a,b,t,t+m,i,j,I,J))
    return sorted(named)

def verify_affine():
    cases=0
    for p in range(4,10):
        for c,z in masks(p).items():
            P,M=z;A=P^M
            for x in range(1<<p):
                v=ports(z,x)
                assert v == P ^ (A&x)
                for j in range(p):
                    assert ports(z,x^(1<<j)) == (v ^ (A&(1<<j)))
                cases+=1
    return cases

def main():
    affine=verify_affine()
    small=0
    for p in range(4,9):
        for k in range(1,(1<<(p-1))-2,2):
            for m in (1,3,5):
                ref=direct_small(p,k,m)
                assert named_reference(p,k,m)==ref,(p,k,m,'named')
                x=mask_statistics(p,k,m)
                assert x['named']==len(ref),(p,k,m,'named_mass')
                assert x['pair_count']==len({r[:2] for r in ref}),(p,k,m,'pair')
                assert x['equal_port']==sum(j==J for a,b,t,T,i,j,I,J in ref),(p,k,m,'same')
                assert x['next_cyclic']==sum(J==(j+1)%p for a,b,t,T,i,j,I,J in ref),(p,k,m,'cyclic')
                small+=1
    q19=[]
    for m,(pairs,named,expected_sha) in EXPECTED.items():
        x=mask_statistics(19,21,m)
        ref=named_reference(19,21,m)
        digest=sha256(''.join(','.join(map(str,r))+'\n' for r in ref).encode()).hexdigest()
        assert len(ref)==named and len({r[:2] for r in ref})==pairs and digest==expected_sha,m
        assert x['named']==named and x['pair_count']==pairs
        assert x['equal_port']==sum(row[5]==row[7] for row in ref)
        assert x['next_cyclic']==sum(row[7]==(row[5]+1)%19 for row in ref)
        x.update(m=m,named_sha256_reference=digest)
        q19.append(x)
    p=4;c=6;z=masks(p)[c]
    assert ports(z,9)==ports(z,11)
    assert ((9^(1<<1))-(1<<3))==9-c
    assert ((11^(1<<1))-(1<<2))==11-c
    result={'schema':'PREFIX974_AFFINE_PORT_BRC_V1','frozen_pin':FROZEN_PIN,
            'test_scope':{'affine_all_c_x_p4_to_p9':affine,'independent_raw_xor_cases_p4_to_p8':small,
                          'p19_k21_gaps':[1,3,5]},
            'counterexample':{'p':4,'residual':6,'x_evenfree_odd_1':9,'x_evenfree_odd_2':11,
                              'common_port_mask':ports(z,9),'x9_source':[3,1,1],'x11_source':[2,1,-1]},
            'q19':q19,
            'status':'AUTHOR_PROOF_EXACT_INTEGER_CHECKED_NOT_INDEPENDENTLY_REVIEWED',
            'scope':'auxiliary named XOR observer; positive BRC port relation counts only'}
    with open('PREFIX974_R6_EXACT_RESULTS.json','w',encoding='utf-8') as f:
        json.dump(result,f,ensure_ascii=False,indent=2)
        f.write('\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
