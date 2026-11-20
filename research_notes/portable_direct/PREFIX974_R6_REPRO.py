#!/usr/bin/env python3
"""PREFIX-974 self-contained exact verifier (Python 3.10+, stdlib only)."""
from collections import Counter, defaultdict
from hashlib import sha256
import json

PIN = 'f42f2906d77f24085c123f3ccfe9667d41caa96d'
EXPECTED = {1:(442,614,'ccbccc30c4171a809f7270ce59f0b72b368839e93ffeeed8df9ba1045720da71'),
            3:(839,1286,'1360a9ca274b357d0b87058d35ef6ccd059d0c5aef995e4d93b0d1363e1aaae3'),
            5:(3,3,'c429ef59749f36ef295b4ac9171fb5171ab3a706beaa270563728d4962649c1b')}

def sources(p):
    ds=defaultdict(list)
    for i in range(p):
        for j in range(p):
            for s in (-1,1):
                ds[(1<<i)-s*(1<<j)].append((i,j,s))
    return ds

def port_masks(ds):
    return {c:(sum(1<<j for i,j,s in ls if s==1),
               sum(1<<j for i,j,s in ls if s==-1)) for c,ls in ds.items()}

def V(z,x):
    P,M=z
    return (P&~x)|(M&x)

def named(p,k,m):
    ds=sources(p)
    side={r:sorted((c,ls) for c,ls in ds.items() if c%2==r) for r in (0,1)}
    H=1<<(p-1);lo=H+1;hi=2*H-1
    out=[]
    for t in range(1,2*k+1):
        d=2*t-k*m
        assert d%2
        buckets=defaultdict(list)
        for C,cs in side[t%2]:
            buckets[(k*C)%abs(d)].append((C,cs))
        for c,ls in side[(1-t)%2]:
            for C,rs in buckets[((k+2)*c)%abs(d)]:
                bn=k*C-(k+2)*c;an=t*C-(t+m)*c
                if bn%d or an%d:continue
                b=bn//d;a=an//d
                if not(lo<=a<=hi and lo<=b<=hi and a!=b):continue
                L=[(i,j) for i,j,s in ls if ((k*a>>j)&1)==(s==-1)]
                R=[(I,J) for I,J,S in rs if (((k+2)*a>>J)&1)==(S==-1)]
                for i,j in L:
                    for I,J in R:
                        assert (k*a^(1<<j))-(1<<i)==t*b
                        assert ((k+2)*a^(1<<J))-(1<<I)==(t+m)*b
                        out.append((a,b,t,t+m,i,j,I,J))
    return sorted(out)

def direct_small(p,k,m):
    H=1<<(p-1);lo=H+1;hi=2*H-1
    out=[]
    for a in range(lo,hi+1,2):
        L=defaultdict(list);R=defaultdict(list)
        for i in range(p):
            for j in range(p):
                x=(k*a^(1<<j))-(1<<i)
                y=((k+2)*a^(1<<j))-(1<<i)
                if x>0:L[x].append((i,j))
                if y>0:R[y].append((i,j))
        for x,ls in L.items():
            for y,rs in R.items():
                if y<=x or (y-x)%m:continue
                b=(y-x)//m
                if not(lo<=b<=hi and b!=a and b%2 and x%b==0):continue
                t=x//b
                if t<1:continue
                out.extend((a,b,t,t+m,i,j,I,J) for i,j in ls for I,J in rs)
    return sorted(out)

def ports_from_named(p,rows):
    groups=defaultdict(lambda:[set(),set()])
    for a,b,t,T,i,j,I,J in rows:
        z=groups[(a,b,t,T)]
        z[0].add(j);z[1].add(J)
    return groups

def main():
    affine_checks=0
    for p in range(4,10):
        for c,z in port_masks(sources(p)).items():
            P,M=z;A=P^M
            for x in range(1<<p):
                u=V(z,x)
                assert u==P^(A&x)
                for j in range(p):assert V(z,x^(1<<j))==u^(A&(1<<j))
                affine_checks+=1
    small_cases=0
    for p in range(4,9):
        for k in range(1,(1<<(p-1))-2,2):
            for m in (1,3,5):
                assert named(p,k,m)==direct_small(p,k,m)
                small_cases+=1
    q19=[]
    for m,(pairs,mass,digest) in EXPECTED.items():
        rows=named(19,21,m)
        assert len(rows)==mass
        h=sha256(''.join(','.join(map(str,r))+'\n' for r in rows).encode()).hexdigest()
        assert h==digest
        groups=ports_from_named(19,rows)
        assert len({r[:2] for r in rows})==pairs
        eq=sum(len(L&R) for L,R in groups.values())
        cyc=sum(sum(((j+1)%19) in R for j in L) for L,R in groups.values())
        assert eq==sum(j==J for a,b,t,T,i,j,I,J in rows)
        assert cyc==sum(J==(j+1)%19 for a,b,t,T,i,j,I,J in rows)
        q19.append(dict(m=m,named=mass,pairs=pairs,equal_port=eq,next_cyclic=cyc,
                        named_sha256_reference=h))
    assert V(port_masks(sources(4))[6],9)==V(port_masks(sources(4))[6],11)==2
    assert (9^2)-8==3 and (11^2)-4==5
    print(json.dumps(dict(schema='PREFIX974_R6_REPRO_V1',frozen_pin=PIN,
                          exhaustive_affine_states=affine_checks,
                          independent_raw_xor_cases=small_cases,q19=q19),indent=2))
if __name__=='__main__':main()
