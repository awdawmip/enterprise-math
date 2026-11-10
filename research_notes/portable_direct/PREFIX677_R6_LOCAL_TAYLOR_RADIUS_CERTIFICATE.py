#!/usr/bin/env python3
"""Exact Fraction implication checker for PREFIX-677-R6 BRC crossover.
Pointwise b-jets come from frozen exact 189-layer predecessor at
d344451396a9bace91a9cbcdb14475c6641a9223; no clock recursion rerun.
"""
from fractions import Fraction as Q
import json

N,M=189,188
D2=2*M*(M-1)
mu0,mu1=3*N,4*N*M
mu2=N*(4*D2+2*M*M)
H0,H1=3*N*N,4*N*N*M
H2=N*N*(4*D2+2*M*M)
W0=2*H0+mu0**2
W1=2*H1+2*mu0*mu1
W2=2*H2+2*(mu1**2+mu0*mu2)
A2,B2=2*W2,2*mu2
assert (D2,mu2,W2)==(70312,66515904,140972783616)
assert (A2,B2)==(281945567232,133031808)

# Predecessor exact jet (reused, not checked from original A_n here):
# 11/25<A(b)<441/1000, 789/100<B(b)<79/10,
# -1681<A'(b)<-1680, 128<B'(b)<129;
# 17948788665/10^9<q0(b)<17948788666/10^9.
Alo,Ahi=Q(11,25),Q(441,1000)
Blo,Bhi=Q(789,100),Q(79,10)
R0=Alo*128+Blo*1680
assert R0==Q(332788,25)
rho=Q(1,170000000)
dA=1681*rho+Q(A2,2)*rho**2
dB=129*rho+Q(B2,2)*rho**2
Amin,Amax=Alo-dA,Ahi+dA
Bmin,Bmax=Blo-dB,Bhi+dB
L=B2*Amax+A2*Bmax
Rmin=R0-L*rho
assert Amin>Q(439,1000) and Amax<Q(442,1000)
assert Bmin>0 and Bmax<8 and Rmin>200
assert Bmin>Q(1789,100)*Amax
assert Bmax<Q(449,25)*Amin
assert Q(200)/(Q(442,1000)**2)>1000
q0lo,q0hi=Q(17948788665,10**9),Q(17948788666,10**9)
qlo,qhi=Q(17948783,10**6),Q(17948794,10**6)
assert q0hi-1000*rho<qlo<qhi<q0lo+1000*rho
assert qlo>Q(1789,100) and qhi<Q(449,25)
assert rho/Q(1,40000000000)==Q(4000,17)
result={'science_pin':'f42f2906d77f24085c123f3ccfe9667d41caa96d',
'prior_jet_commit':'d344451396a9bace91a9cbcdb14475c6641a9223',
'previous_radius_commit':'3e6943a4350e168d62681a62bed140cb23216d86',
'b':'53/1000','rho':str(rho),'gain':str(rho/Q(1,40000000000)),
'Amin':str(Amin),'Amax':str(Amax),'Bmin':str(Bmin),'Bmax':str(Bmax),
'Rlower':str(Rmin),'A2':A2,'B2':B2,'q0_prime_lower_strict':'1000',
'fixed_q_band':['17948783/1000000','17948794/1000000'],
'result':'unique diagonal-edge crossing in I for each real q in fixed_q_band; left D>0, right D<0',
'checks':'ALL_CHECKS_PASS',
'status':'AUTHOR_DERIVED_EXACT_FRACTION_IMPLICATION_CHECKED_UNREVIEWED_NOT_ADMITTED'}
print(json.dumps(result,indent=2))
