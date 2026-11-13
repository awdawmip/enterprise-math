#!/usr/bin/env python3
"""Exact Fraction arithmetic certificate for the Gamma(max) binary64 forward-error bound.
Scope: frozen 189-layer survivor recurrence; standard correctly-rounded binary64
normal arithmetic, verified relative input rounding, dot-product gamma_189.
This script proves the global forward bound; it is not a replacement for a grid scan.
"""
from fractions import Fraction as Q

N=189
u=Q(1, 1<<53)
def gam(k):
    assert k*u<1
    return k*u/(1-k*u)

# Relative errors of positive sums; TCT and TDT two-stage matmuls.
r_sum=(1+u)*(1+gam(N))-1
r_x=(1+u)**3*(1+gam(N))**2-1
r_y=(1+u)**4*(1+gam(N))**2-1
max_x=Q(N*N,2)
max_y=Q(N*N*(2*N-1),2)
max_b=Q(N*(N+1),2)
max_mu=2*N
max_m2=4*max_b

# mu = fl(fl(A_i + A_j) - (T C T^t)_ij)
e_mu=(2*N*r_sum+max_x*r_x+2*N*(1+r_sum)*u
      +u*(2*N*(1+r_sum)*(1+u)+max_x*(1+r_x)))
# M2 = fl(2*fl(B_i + B_j) - (T D T^t)_ij)
e_m2=(4*max_b*r_sum+4*max_b*(1+r_sum)*u
      +max_y*r_y+u*(4*max_b*(1+r_sum)*(1+u)+max_y*(1+r_y)))
# W(e) = fl(M2(e) - fl(mu(e)^2))
e_w=(e_m2+2*max_mu*e_mu+e_mu**2+u*(max_mu+e_mu)**2
     +u*(max_m2+e_m2+(max_mu+e_mu)**2*(1+u)))
e_sq=2*max_mu*e_mu+e_mu**2+u*(max_mu+e_mu)**2
# Max is 1-Lipschitz, division by two is exact for normal binary64.
e_pen=e_mu+u*(max_mu+e_mu)
# G = W(e) - M2(h) + mu(a)^2 - max(0,(mu(e)-mu(a))/2)
e_g=(e_w+e_m2+e_sq+e_pen
     +gam(3)*(2*max_m2+e_w+e_m2
             +(max_mu+e_mu)**2*(1+u)+max_mu+e_mu))

assert e_mu<Q(1,10**8)
assert e_m2<Q(1,10**6)
assert e_w<Q(1,10**6)
assert e_g<Q(1,100000)
for k,v in [('sum_relative',r_sum),('cross_C_relative',r_x),
            ('cross_D_relative',r_y),('mu_abs',e_mu),
            ('M2_abs',e_m2),('We_abs',e_w),('G_abs',e_g)]:
    print(k,format(float(v),'.17g'))
print('ALL_CHECKS_PASS PREFIX754-R6, uniform |G_hat-G| < 1/100000')
