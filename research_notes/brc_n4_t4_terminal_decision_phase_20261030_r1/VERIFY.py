from fractions import Fraction as F
from itertools import product

q = dict(AU=F(1,6), AV=F(1,3), BU=F(1,4), BV=F(1,4))
r = dict(AU=(F(9,10),F(11,10)), AV=(F(1,4),)*2,
         BU=(F(1,5),F(9,5)), BV=(F(2),)*2)

def put(a,k,v): a[k] = a.get(k,F(0))+v

def obs(L,u,v,d0,d1):
    y,c,z={},{},{}
    for s in q:
        for j,k in product(range(2),repeat=2):
            m=q[s]/4*(r[s][j] if L=='P' else 1)
            if s in ('AV','BV'): a=('E',)
            elif s=='AU': a=('A',)
            else: a=('B',)
            put(c,a,m)
            put(z,(a[0],j) if s=='BU' else a,m)
            if s!='BU': put(y,a,m); continue
            t,d=(u,d0) if j==0 else (v,d1)
            put(y,('B3',),m*(1-t))
            put(y,('B4P',k),m*t*d)
            put(y,('B4Q',k),m*t*(1-d))
    assert sum(y.values())==sum(c.values())==sum(z.values())==1
    return y,c,z

def TV(p,q):
    return sum((abs(p.get(i,F(0))-q.get(i,F(0))) for i in p.keys()|q.keys()),F(0))/2

def run(u,v,d0,d1):
    p,pc,pz=obs('P',u,v,d0,d1)
    q,qc,qz=obs('Q',u,v,d0,d1)
    assert pc==qc=={('E',):F(7,12),('A',):F(1,6),('B',):F(1,4)}
    assert (pz['B',0],pz['B',1],qz['B',0],qz['B',1])==(F(1,40),F(9,40),F(1,8),F(1,8))
    target=(abs(v-u)+abs(v*d1-u*d0)+abs(v*(1-d1)-u*(1-d0)))/20
    assert TV(p,q)==target and target<=F(1,10)
    mid={i:(p.get(i,F(0))+q.get(i,F(0)))/2 for i in p.keys()|q.keys()}
    assert TV(p,mid)==TV(q,mid)==target/2
    for L,z,actual in (('P',pz,p),('Q',qz,q)):
        reconstructed={}
        for a,m in z.items():
            if a[0]!='B': put(reconstructed,a,m); continue
            j=a[1]; t,d=(u,d0) if j==0 else (v,d1)
            put(reconstructed,('B3',),m*(1-t))
            for k in range(2):
                put(reconstructed,('B4P',k),m*t*d/2)
                put(reconstructed,('B4Q',k),m*t*(1-d)/2)
        assert TV(actual,reconstructed)==0
    return target,target/2

for L in ('P','Q'):
    raw=[q[s]/4*(r[s][j] if L=='P' else 1) for s in q for j,k in product(range(2),repeat=2)]
    assert len(raw)==16 and min(raw)>0 and sum(raw)==1
values=[F(0),F(1,4),F(1,2),F(3,4),F(1)]
for args in product(values,repeat=4): run(*args)
assert run(F(1),F(1),F(0),F(1))==(F(1,10),F(1,20))
assert run(F(1),F(1),F(0),F(0))==(F(0),F(0))
for t in values: assert run(t,t,F(0),F(1))==(t/10,t/20)
print('PASS_BRC_N4_T4_TERMINAL_DECISION_EXACT_20261030; 16+16 positive source leaves; 625 rational profiles; sharp witness 1/10,1/20; equality phase checked')
