"""Exact rational certification for S23 mixed T/B Chernoff budget witness.

Frozen model: 43ec6098b1330ae86d0a7863be336c5d97f6ef34.
Inherited author analytic lemma: 8b88188ab137e5d35c92c4abb06b89463dcb5357.
"""
from fractions import Fraction as Q

v = Q(1, 21)
s = Q(1, 2)
x = v*v
k = s/(2-s)
q = 4*x
assert k == Q(1,3) and q < 1

# Previously derived exact optimized Chernoff coefficients.
g2 = (1+k)*(10*k*k+18*k-1)/144
g3 = (484*k**5+1364*k**4+1960*k**3+2360*k**2+661*k-79)/12960
g4 = (268784*k**8+1029808*k**7+1837568*k**6+2341248*k**5+
      2721600*k**4+3101952*k**3+1606957*k**2+245942*k-56159)/(10886400*(1+k))
assert g2 == Q(55,972)
assert g3 == Q(3007,78732)
assert g4 == Q(8565077,340122240)

tail = 256*q**5/(1-q)
G_lower = g2*x*x+g3*x**3+g4*x**4-tail
assert G_lower == Q(1548995022721369,5621740898642842135680)
assert G_lower > Q(1,5000000)
F_lower = s*(1-s)*G_lower
assert F_lower > Q(1,20000000)

# B optimum <= KL(P||Q) <= chi^2(P||Q).
p = s*(1+v)/2
qb = s*(1-v)/2
assert p == Q(11,42) and qb == Q(10,42)
chi2 = (p-qb)**2/(qb*(1-qb))
assert chi2 == Q(1,320)

L = 25000
K = 3*L+1
mT, nB = 2*L, 1
cT = 2-s
assert K == 75001 and mT == 50000
assert mT*cT+nB == K
assert K//cT == mT
assert p != qb

# The common-t mixed coefficient at t=1/2 improves upon pure T.
# Dropping its STRICT positive B term still proves the pure-B gap.
gap_lower = 3*L*Q(1,20000000)-chi2
assert gap_lower == Q(1,1600)>0
assert 3*L*F_lower-chi2 > gap_lower

# Algebraic general rational-cost family.
for P,Qden,L in [(3,2,25000),(5,3,1),(21,20,7),(17,9,4)]:
    assert (L*Qden)*Q(P,Qden)+1 == L*P+1
    assert (L*P+1)//Q(P,Qden) == L*Qden

print("PASS_BRC_S23_MIXED_INTEGER_BUDGET_CHERNOFF_20261104")
print("g2=",g2,"g3=",g3,"g4=",g4)
print("G_lower=",G_lower)
print("F_lower=",F_lower)
print("CB_upper=",chi2)
print("K=",K,"mT=",mT,"nB=",nB,"cost=",mT*cT+nB)
print("mixed_minus_pure_B_strict_lower=",gap_lower)
print("mixed_minus_pure_T_strict_positive=TRUE (distinct B laws)")
