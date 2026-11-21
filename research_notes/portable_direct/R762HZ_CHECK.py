#!/usr/bin/env python3
"""R762HZ: exact rational verification of the third term of Port/BRC local limit.
Requires Python 3 and sympy. All mathematical assertions use exact rationals.
"""
import itertools
import random
import functools
from collections import defaultdict
import sympy as S

axes=range(6)
ports=list(itertools.combinations(axes,2))
triples=list(itertools.combinations(axes,3))
tri_id={t:i for i,t in enumerate(triples)}
N=len(ports)
Adj=S.zeros(N)
edge={}
for i,p in enumerate(ports):
    for j,q in enumerate(ports):
        if i!=j and len(set(p)&set(q))==1:
            Adj[i,j]=1
            edge[i,j]=tri_id[tuple(sorted(set(p)|set(q)))]
A=Adj/8
J=S.ones(N,N)/15
R=S.Rational(16,15)*(S.eye(N)+A-2*J)
ones=S.ones(N,1)
assert R*ones==S.zeros(N,1)
assert R*(S.eye(N)-A)==S.eye(N)-J

def eigen_coeffs(u):
    x=[sum(u[i] for i in t) for t in triples]
    C=S.zeros(N); D=S.zeros(N); E=S.zeros(N)
    for (i,j),k in edge.items():
        v=S.Integer(x[k])
        C[i,j]=-v**2/S.Integer(16)
        D[i,j]=v**4/S.Integer(192)
        E[i,j]=-v**6/S.Integer(5760)
    c=C*ones; d=D*ones; e=E*ones
    rc=R*c
    l2=(ones.T*c)[0]/N
    l4=(ones.T*d)[0]/N+(c.T*rc)[0]/N
    l6=(ones.T*e)[0]/N+2*(d.T*rc)[0]/N
    l6+=(c.T*R*C*rc)[0]/N-l2*(c.T*R*rc)[0]/N
    return [S.factor(v) for v in (l2,l4,l6)]

def partitions(n,lo=1):
    if n==0:
        yield ()
    else:
        for k in range(lo,n+1):
            for tail in partitions(n-k,k):
                yield (k,)+tail

basis={n:list(partitions(n)) for n in (2,4,6)}

def features(u,n):
    powers={k:sum(S.Integer(x)**k for x in u)
            for k in range(1,n+1)}
    return [S.prod(powers[k] for k in part) for part in basis[n]]

# S6 invariance and homogeneous degree imply the finite partition bases
# span ALL possible degree-2/4/6 coefficient polynomials.
rng=random.Random(76290)
samples=[]
rows={n:[] for n in basis}
while len(samples)<11:
    u=tuple(rng.randrange(-3,4) for _ in range(6))
    row=features(u,6)
    if S.Matrix(rows[6]+[row]).rank()>len(rows[6]):
        samples.append(u)
        for n in basis:
            rows[n].append(features(u,n))
coeff_samples=[eigen_coeffs(u) for u in samples]
fits={}
for j,n in enumerate((2,4,6)):
    M=S.Matrix(rows[n])
    assert M.rank()==len(basis[n])
    target=S.Matrix([v[j] for v in coeff_samples])
    beta=list((M.T*M).inv()*M.T*target)
    fits[n]={k:v for k,v in zip(basis[n],beta) if v}
    for _ in range(4):
        u=tuple(rng.randrange(-5,6) for __ in range(6))
        assert eigen_coeffs(u)[j]==sum(a*b for a,b in zip(beta,features(u,n)))

zero=(0,)*6
def mul(p,q):
    out=defaultdict(lambda:S.Integer(0))
    for a,v in p.items():
        for b,w in q.items():
            out[tuple(x+y for x,y in zip(a,b))]+=v*w
    return {a:v for a,v in out.items() if v}
def add(p,q):
    out=p.copy()
    for a,v in q.items():
        out[a]=out.get(a,S.Integer(0))+v
    return {a:v for a,v in out.items() if v}
def scale(p,c):
    return {a:v*c for a,v in p.items() if v*c}
def ps(k):
    return {tuple(k if i==j else 0 for j in range(6)):S.Integer(1)
            for i in range(6)}
def polynomial(n):
    out={}
    for part,c in fits[n].items():
        term={zero:S.Integer(1)}
        for k in part:
            term=mul(term,ps(k))
        out=add(out,scale(term,c))
    return out

l2,l4,l6=(polynomial(n) for n in (2,4,6))
cov=[[S.Rational(10,3)*int(i==j)-S.Rational(4,9)
      for j in range(6)] for i in range(6)]
@functools.lru_cache(None)
def gaussian_moment(exp):
    n=sum(exp)
    if n==0:return S.Integer(1)
    if n%2:return S.Integer(0)
    i=next(i for i,x in enumerate(exp) if x)
    total=S.Integer(0)
    for j in range(6):
        count=exp[j]-int(i==j)
        if count<=0:continue
        e=list(exp); e[i]-=1; e[j]-=1
        total+=count*cov[i][j]*gaussian_moment(tuple(e))
    return total
def mean(p):
    return S.factor(sum(v*gaussian_moment(e) for e,v in p.items()))

Q=scale(l2,-2)
Q2=mul(Q,Q); Q3=mul(Q2,Q); Q4=mul(Q2,Q2)
T4=add(l4,scale(Q2,-S.Rational(1,8)))
T6=add(add(l6,scale(mul(Q,l4),S.Rational(1,2))),
       scale(Q3,-S.Rational(1,24)))
expected={
    'lambda6':(mean(l6),S.Rational(-1921,90)),
    'Q_lambda4':(mean(mul(Q,l4)),S.Rational(275,3)),
    'Q_cube':(mean(Q3),S.Integer(480)),
    'lambda4_squared':(mean(mul(l4,l4)),S.Rational(13631,60)),
    'lambda4_Q_squared':(mean(mul(l4,Q2)),S.Integer(1100)),
    'Q_fourth':(mean(Q4),S.Integer(5760)),
    'T4':(mean(T4),S.Rational(19,6)),
    'T6':(mean(T6),S.Rational(202,45)),
    'T4_squared':(mean(mul(T4,T4)),S.Rational(2531,60))
}
for name,(actual,reference) in expected.items():
    assert actual==reference,(name,actual,reference)
beta=S.factor(mean(T6)+mean(mul(T4,T4))/2)
assert beta==S.Rational(9209,360)
print('PASS R762HZ')
for name,(value,_) in expected.items():
    print(name,str(value))
print('third_term',beta)
