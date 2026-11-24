from math import gcd, prod, lcm
from pathlib import Path
from collections import Counter, defaultdict
from functools import cache
import json
from enumerate import *
S=11356718000553566643685496313583434507970452519839503606327232707476034989690
R=9807947978443488306255509703402695727949968778703073231931137913705883712843
P=(7,17,31,41,71,97,113,127,151,241,257,281,337,641,673,1321,14449,29191,65537,6700417)
table={int(d):row for d,row in json.load(open('inventory.json')).items()}
lucas={int(q):row for q,row in json.load(open('lucas.json')).items()}
def divisors(n):return [p for p in range(2,n+1) if n%p==0 and all(p%k for k in range(2,1+int(p**.5)))]
@cache
def prime(q):
    if q==2:return True
    a,f=lucas[q];fs={int(p):e for p,e in f.items()}
    assert prod(p**e for p,e in fs.items())==q-1
    return all(prime(p) and gcd(pow(a,(q-1)//p,q)-1,q)==1 for p in fs) and pow(a,q-1,q)==1
def strip(a,b):
    while (g:=gcd(a,b))>1:a//=g
    return a
G=defaultdict(list)
for d in range(1,421):
    f=d//gcd(d,12)
    if f not in (1,3,6,*F):continue
    a=strip(strip(2**d-1,prod(2**(d//p)-1 for p in divisors(d))),S)
    if a==1:
        assert d not in table
        continue
    tf,ta,qs=table[d]
    assert (f,a)==(tf,ta) and prod(qs)==a and all(prime(q) for q in qs)
    G[f].extend(qs)
assert dict(caps)=={f:len(qs) for f,qs in G.items()}
assert len(set(q for qs in G.values() for q in qs))==sum(caps.values())
def order(q):
    v=2; d=1
    while v!=1:v=2*v%q;d+=1
    return d
old=(*P,5,13)
assert all(S%q==0 for q in (*old,19,73,433,38737))
l=lcm(*(order(q) for q in (*old,19,73,433,38737)),420)
res=[n for n in range(1,l+1) if all((R*R*pow(2,n,q)-1)%q for q in old)]
assert all(n%12==8 for n in res)
assert set(res)=={n for n in range(1,l+1) if n%12==8 and (n-8)//12%35 in A}
assert all({v%f for v in range(f) if (R*R*pow(2,8+12*v,q)-1)%q==0}==bs for q,f,bs in [(19,3,{0}),(73,3,{1}),(433,6,set()),(38737,6,{5})])
# Separate direct enumeration using the analytic W exclusion: both W imply phase 2 only.
cats=tuple(x for x in X if x==(6,5) or x[0] not in (3,7,14,35) and (x[0]%3 or x[1]%3==2))
V=tuple(v for v in range(PER) if v%35 in A and v%3==2)
VM={x:sum(1<<i for i,v in enumerate(V) if v%x[0]==x[1]) for x in cats}
vf=(1<<len(V))-1
def direct():
    for k in (3,4):
        for xs in combinations(cats,k):
            if not valid(xs): continue
            m=[VM[x] for x in xs]
            if sum_union(m)==vf and all(sum_union(m[:i]+m[i+1:])!=vf for i in range(k)):
                yield tuple(sorted((*xs,(3,0),(3,1))))
    for b in range(1,6):
        rows=tuple((7,r) for r in range(1,6) if r!=b)
        g=tuple((35,r) for r in sorted(A) if r%7==b)
        yield tuple(sorted((*rows,(14,b),(14,b+7))))
        if len(g)==2:yield tuple(sorted((*rows,*g)))
t=tuple(sorted(set(classes())))
assert set(t)==set(direct())
D=json.load(open('templates.json'))
assert t==tuple(tuple(map(tuple,s)) for s in D['types'])
def crt(a,m,b,n):
    return a+m*((b-a)*pow(m,-1,n)%n),m*n
witness={}
for key,(xx,tt) in D['essential_f'].items():
    f=int(key);x=tuple(xx);ts=tuple(map(tuple,tt))
    for q in G[f]:
        assigned={x:q}
        for slot in ts:
            if slot not in FIX and slot!=x:assigned[slot]=next(p for p in G[slot[0]] if p not in assigned.values())
        def root(toggle):
            a,m=R,S
            phases={p:b for slot,p in assigned.items() for _,b in [slot] if toggle or slot!=x}
            for p0 in [p for qs in G.values() for p in qs]:
                a,m=crt(a,m,pow(2,-(4+6*phases[p0]),p0) if p0 in phases else 0,p0)
            return a,m
        on,mo=root(True);off,mm=root(False)
        assert mo==mm and on>=R and off>=R and (on-off)%(mo//q)==0 and on%q!=off%q
        # Read hit categories from the actual root and use literal exponent classes.
        check=lcm(PER,l//12)
        def holes(a,qs):
            Q=tuple((p,order(p)//gcd(12,order(p))) for p in qs)
            classes=[(f, b) for p,f in Q for b in range(f) if (a*a*pow(2,8+12*b,p)-1)%p==0]
            return sum(1 for v in range(check) if v%35 in A and all(v%f!=b for f,b in classes))
        onh=holes(on,set(assigned.values())|{19,73,38737})
        offh=holes(off,set(assigned.values())|{19,73,38737})
        assert onh==0 and offh>0
        witness[q]={'f':f,'phase':x[1],'on':str(on),'off':str(off),'off_holes':offh,'v_period':check}
with open('witnesses.json','w') as out:json.dump(witness,out,sort_keys=True,separators=(',',':'))
print('verified',len(G),'groups',len(witness),'ordinary pairs',len(t),'templates by two enumerations')
