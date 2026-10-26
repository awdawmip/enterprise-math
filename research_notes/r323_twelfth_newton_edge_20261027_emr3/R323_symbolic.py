#!/usr/bin/env python3
"""R323, algebraic induction certificate for the q=11 edge of the ordered positive BRC polynomial."""
from functools import lru_cache
from sympy import S, Rational, symbols, binomial, factorial, diff, expand, Poly, cancel, expand_func
s,z,u=symbols('s z u')
def C(n,k): return binomial(n,k) if 0<=k<=n else S.Zero
def n(i): return -C(3,i-1)*z-C(6,i-1)*z**2+C(8,i-2)*z**3
def delta(i): return (-C(4,i)+C(2,i-1))*z + (C(5,i-1)-C(5,i-2))*z**2 + C(7,i-2)*z**3-C(9,i-3)*z**4
@lru_cache(None)
def M(i):
    if i==0: return S.One
    return expand(n(i)*(1-z)**i - sum(delta(j)*M(i-j)*(1-z)**(j-1) for j in range(1,min(i,12)+1)))
P=[S.One,
 3*(s+1)/4,
 (9*s**2+11*s-26)/16,
 3*(9*s**3+6*s**2-119*s+220)/64,
 3*(27*s**4-18*s**3-911*s**2+4070*s-6184)/256,
 3*(81*s**5-225*s**4-5295*s**3+43385*s**2-134746*s+162800)/1024,
 3*(243*s**6-1377*s**5-26055*s**4+348565*s**3-1709628*s**2+3668252*s-2031840)/4096,
 9*(243*s**7-2268*s**6-38052*s**5+780850*s**4-5472663*s**3+16271178*s**2-1634008*s-78016960)/16384,
 (6561*s**8-90396*s**7-1371006*s**6+41693400*s**5-395382351*s**4+1509433716*s**3+1771638636*s**2-36493134960*s+99723415680)/65536,
 (19683*s**9-373977*s**8-5078214*s**7+225467550*s**6-2791719189*s**5+13314869127*s**4+38834268264*s**3-860330966220*s**2+4551847454736*s-9191974659840)/262144,
 (59049*s**10-1476225*s**9-17452260*s**8+1134666630*s**7-17876052243*s**6+105293849535*s**5+500912600310*s**4-13511047863780*s**3+105842210675544*s**2-414136077320160*s+691268379379200)/1048576]
assert M(0).subs(z,1)==1
for r in range(1,11):
    assert diff(M(r),z,r).subs(z,1)==2**r*P[r].subs(s,r),r
    D=S.Zero
    for i in range(1,r+2):
      for a in range(r+2-i):
        if (i,a)==(1,0): continue
        h=r+1-i-a
        D += (-1)**i * factorial(r)/factorial(r+1-i)*binomial(r+1-i,a)*diff(delta(i),z,a).subs(z,1)*P[h].subs(s,s-i)/2**i
    assert expand(D-P[r]+P[r].subs(s,s-1))==0,r
print('PASS prior moments r=0..10: bases and polynomial induction')
r=11
D=S.Zero
for i in range(1,r+2):
  for a in range(r+2-i):
    if i==1 and a==0: continue
    h=r+1-i-a
    D += (-1)**i *factorial(r)/factorial(r+1-i)*binomial(r+1-i,a)*diff(delta(i),z,a).subs(z,1)*P[h].subs(s,s-i)/2**i
D=expand(D)
assert Poly(D,s).degree()==10
A=S.Zero;R=D
for d in reversed(range(11)):
    c=Poly(R,s).coeff_monomial(s**d)
    term=c*s**(d+1)/(d+1)
    A+=term
    R=expand(R-(term-term.subs(s,s-1)))
assert R==0
base=diff(M(11),z,11).subs(z,1)
A=expand(A+(base/2**11-A.subs(s,11)))
assert expand(A-A.subs(s,s-1)-D)==0
assert A.subs(s,11)==base/2**11
P.append(A)
q=11
recovered=cancel(expand(expand_func(sum((-1)**r*binomial(2*s+1-r,q-r)*P[r]/factorial(r) for r in range(q+1)))))
qden,qnum=Poly(recovered,s).clear_denoms(convert=True)
pden,pnum=Poly(A,s).clear_denoms(convert=True)
dden,dnum=Poly(D,s).clear_denoms(convert=True)
shift=Poly(expand(qnum.as_expr().subs(s,11+u)),u)
print('base_m11_11=',base)
print('P11_den=',pden,'P11_num=',list(map(int,pnum.all_coeffs())))
print('D11_den=',dden,'D11_num=',list(map(int,dnum.all_coeffs())))
print('Q11_den=',qden,'Q11_num=',list(map(int,qnum.all_coeffs())))
print('Q11shift=',list(map(int,shift.all_coeffs())))
print('minimum=',recovered.subs(s,11),'edge_a=',int(2**11*recovered.subs(s,11)))
assert qnum.degree()==11
assert all(c>0 for c in shift.all_coeffs())
assert recovered.subs(s,11)>0
print('PASS R323 exact infinite-s recurrence q=11 and positive-shift algebra')
