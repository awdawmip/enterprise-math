"""Exact-author verifier: BRC N4 lawful G4 stop-time and noisy BU provenance."""
from fractions import Fraction as F
from itertools import product

q={'AU':F(1,6),'AV':F(1,3),'BU':F(1,4),'BV':F(1,4)}
r={'AU':(F(9,10),F(11,10)),'AV':(F(1,4),F(1,4)),
   'BU':(F(1,5),F(9,5)),'BV':(F(2),F(2))}

def add(d,k,v):d[k]=d.get(k,F(0))+v

def src(law):
    t={(s,j,k):q[s]/4*(r[s][j] if law=='P' else 1)
       for s in q for j,k in product(range(2),repeat=2)}
    assert len(t)==16 and all(v>0 for v in t.values()) and sum(t.values())==1
    return t

def actual(law,eps):
    out={}
    for (s,j,k),mass in src(law).items():
        if s in ('AV','BV'):add(out,('E',None,'E'),mass)
        elif s=='AU':add(out,('A',None,'A'),mass)
        else:
            y='B3' if j==0 else ('B4','Q',k)
            for z,pr in ((j,1-eps),(1-j,eps)):add(out,('B',z,y),mass*pr)
    assert sum(out.values())==1
    return out

def observed(joint):
    d={}
    for (c,z,y),mass in joint.items():add(d,(c,z),mass)
    return d

def decoder(joint,alpha,beta):
    out={}
    for (c,z),mass in observed(joint).items():
        if c in ('E','A'):add(out,(c,z,c),mass)
        else:
            x=alpha if z==0 else beta
            add(out,(c,z,'B3'),mass*x)
            for k in range(2):add(out,(c,z,('B4','Q',k)),mass*(1-x)/2)
    assert sum(out.values())==1
    return out

def tv(p,q):
    return sum((abs(p.get(k,F(0))-q.get(k,F(0)))
                for k in p.keys()|q.keys()),F(0))/2

def drop_z(joint):
    d={}
    for (c,z,y),m in joint.items():add(d,(c,y),m)
    return d

def bounds(p,eps):
    a=p+(1-2*p)*eps;b=1-a
    em=(1-2*p)*eps/(1+2*a)
    ej=(1-2*p)*eps*(1-eps)/(b*(1+2*a))
    beta=p*eps/b;alpha=1-beta-2*ej
    assert 0<=p*(1-eps)/a<=alpha<=1-eps and 0<=beta<=eps
    return em,ej,alpha,beta

assert sum(m for (s,j,k),m in src('P').items() if s=='BU' and j==0)==F(1,40)
assert sum(m for (s,j,k),m in src('Q').items() if s=='BU' and j==0)==F(1,8)
assert sum(m for (s,j,k),m in src('P').items() if s=='BU')==F(1,4)
assert sum(m for (s,j,k),m in src('Q').items() if s=='BU')==F(1,4)

print('PASS_BRC_N4_G4_NOISY_PROVENANCE_JOINT_AND_MARGINAL_SHARP_20261030')
print('eps | marginal unconditional radius | joint unconditional radius | alpha joint | beta joint')
for eps in [F(0),F(1,20),F(1,10),F(1,4),F(1,2)]:
    P,Q=actual('P',eps),actual('Q',eps)
    em,ej,alpha,beta=bounds(F(1,10),eps)
    assert tv(P,Q)==F(1,10)
    assert tv(P,decoder(P,alpha,beta))==tv(Q,decoder(Q,alpha,beta))==ej/4
    pm=decoder(P,1-2*em,F(0));qm=decoder(Q,1-2*em,F(0))
    assert tv(drop_z(P),drop_z(pm))==tv(drop_z(Q),drop_z(qm))==em/4
    for x,y in product([F(0),F(1,5),F(1,2),F(4,5),F(1)],repeat=2):
        assert max(tv(P,decoder(P,x,y)),tv(Q,decoder(Q,x,y)))>=ej/4
        assert max(tv(drop_z(P),drop_z(decoder(P,x,y))),
                   tv(drop_z(Q),drop_z(decoder(Q,x,y))))>=em/4
    print(eps,em/4,ej/4,alpha,beta)
for p,eps in product([F(1,10),F(1,5),F(2,5)],
                     [F(0),F(1,11),F(1,4),F(2,5),F(1,2)]):
    em,ej,alpha,beta=bounds(p,eps)
    a=p+(1-2*p)*eps;b=1-a
    pe=abs(a*alpha-p*(1-eps))+abs(b*beta-p*eps)
    qe=(abs(alpha-(1-eps))+abs(beta-eps))/2
    assert pe==qe==ej
    for x,y in product([F(0),F(1,7),F(1,3),F(2,3),F(6,7),F(1)],repeat=2):
        pe=abs(a*x-p*(1-eps))+abs(b*y-p*eps)
        qe=(abs(x-(1-eps))+abs(y-eps))/2
        assert max(pe,qe)>=ej
        assert max(abs(a*x+b*y-p),abs((x+y)/2-F(1,2)))>=em
print('Verified: 16 positive leaves/law; 5 exact sensors x25 decoder grid; 15 prior-sensor pairs x36 grid')
print('Universal scope: analytic LP dual + explicit common-kernel attainment in PROOF.md')
