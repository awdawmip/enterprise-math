#!/usr/bin/env python3
"""Exact asymptotic jet collision certificate for cutoffs 74 and 76."""
import json
from pathlib import Path
from math import factorial
import sympy as s
N,x=s.symbols('N x')
e,d,E,D=s.symbols('e d E D')
W=(1,1,2,3,6)

def conv(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out

def block(weights):
    a=[1]
    for w in weights:a=conv(a,[int(k%w==0) for k in range(7-w)])
    return a

QC=block((*W,1))
QT=conv([0,1],block((1,1,1,1,2,3,6)))
S=18*N**4+54*N**3-345*N**2+2070*N-16315

def fall(t,k):return s.prod(t-i for i in range(k))/factorial(k)

def quasi(r):
    c=s.expand(sum(a*fall((N-1-i)/6+5,5) for i,a in enumerate(QC) if (r-1-i)%6==0))
    t=s.expand(sum(a*fall((N-1-i)/6+6,6) for i,a in enumerate(QT) if (r-1-i)%6==0))
    return c,t

def yjet(r,ee,dd):
    c,t=quasi(r)
    cp,tp=s.Poly(c,N),s.Poly(t,N)
    K=9
    a=[cp.nth(5-i) if i<=5 else s.Integer(0) for i in range(K+1)]
    b=[tp.nth(6-i) if i<=6 else s.Integer(0) for i in range(K+1)]
    a[5]+=dd;b[6]+=ee
    ratio=[]
    for k in range(K+1):
        ratio.append(s.expand((b[k]-sum(a[i]*ratio[k-i] for i in range(1,k+1)))/a[0]))
    sub={-4:s.Rational(18,108),-3:s.Rational(54,108),-2:s.Rational(-345,108),-1:s.Rational(2070,108),0:s.Rational(-16315,108)}
    assert all(ratio[k+4]==sub[k] for k in [-4,-3,-2,-1])
    return [s.factor(ratio[k+4]-sub.get(k,0)) for k in range(6)]

def shift(a,q):
    # x=(6j)^-1, n=q+6j, so n^-h=x^h(1+qx)^-h
    return [s.expand(a[0] if k==0 else sum(a[h]*s.binomial(-h,k-h)*q**(k-h) for h in range(1,k+1))) for k in range(6)]

left,right=shift(yjet(2,e,d),74),shift(yjet(4,E,D),76)
assert left[0]==right[0]==-s.Rational(25,36)
cs=[s.factor(left[k]-right[k]) for k in range(1,6)]
A,b=s.linear_eq_to_matrix(cs[:4],[e,d,E,D])
assert A.det()!=0
sol=s.solve(cs[:4],[e,d,E,D],dict=True)[0]
expected={d:-s.Rational(656227,472068),e:s.Rational(69402481,101966688),D:-s.Rational(755303,472068),E:s.Rational(194725627,101966688)}
assert sol==expected
assert all(-2<sol[t]<2 for t in (e,d,E,D))
assert all(s.cancel(z.subs(sol))==0 for z in cs[:4])
fifth=s.cancel(cs[4].subs(sol))
assert fifth==s.Rational(55842420440,39339)
# Independent combinatorial counts for multiple phases and n values.
parts=[0]*241;parts[0]=1
for w in W:
    for k in range(w,241):parts[k]+=parts[k-w]
C,T=[0]*241,[0]*241
for k in range(1,241): C[k]=C[k-1]+parts[k-1];T[k]=T[k-1]+C[k-1]
for r in (2,4):
    c,t=quasi(r)
    for k in range(29,241):
        if k%6==r:assert c.subs(N,k)==C[k] and t.subs(N,k)==T[k]

def Y(n0,ee,dd):
    c,t=quasi(n0%6)
    return s.cancel(n0**3*(t.subs(N,n0)+ee)/(c.subs(N,n0)+dd)-S.subs(N,n0)/108)
samples=[]
for j in (0,1,10,100,1000,10000):
    delta=s.cancel(Y(74+6*j,sol[e],sol[d])-Y(76+6*j,sol[E],sol[D]))
    samples.append({'j':j,'sign':int(s.sign(delta)),'delta':str(s.N(delta,16)), 'scaled':str(s.N(delta*(6*j)**5,16)) if j>0 else None})
res={'unit':'R749STI','status':'AUTHOR_EXACT_NOT_REVIEWED','frozen_science':'a72226e2430ffa4786321ac86e7f0c599d5f0389','cutoffs':[74,76],'sampling':'n=74+6j versus 76+6j','model':'five labeled weights (1,1,2,3,6); four fixed parameters each in [-2,2]','common_limit':'-25/36','coefficient_order':'x=1/(6j)','linear_matrix':[[str(A[i,j]) for j in range(4)] for i in range(4)],'linear_rhs':[str(b[i]) for i in range(4)],'determinant':str(A.det()),'solution':{str(k):str(sol[k]) for k in (e,d,E,D)},'difference_jet_coefficients':[str(c) for c in cs],'first_nonzero_coefficient':str(fifth),'samples':samples,'coverage':'exact quasi-polynomial generating functions; independent partition-count check n=29..240, residues 2 and 4','unresolved':'native X6/BRC Port mapping and broader pair classification'}
out=Path(__file__).with_name('R749STI_JET_COLLISION_RESULTS.json')
out.write_text(json.dumps(res,indent=2,ensure_ascii=False,sort_keys=True)+'\n')
print('PASS four vanishing coefficients; unique legal rational parameters; fifth',fifth)
print('det',A.det(),'samples',samples,'saved',out,out.stat().st_size)
