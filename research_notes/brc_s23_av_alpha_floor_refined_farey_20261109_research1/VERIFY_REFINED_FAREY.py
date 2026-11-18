#!/usr/bin/env python3
"""45-term exact logarithm remainder and sharp Farey floor-interval certificate."""
from fractions import Fraction as F

def atanh_log_interval(z):
    # Log ((1+z)/(1-z)) = 2 sum_{m>=0} z**(2*m+1)/(2*m+1).
    s=F(0); power=z
    for m in range(45):
        s+=2*power/(2*m+1)
        power*=z*z
    return s,s+2*power/(91*(1-z*z))
a,b=atanh_log_interval(F(1,3))
c,d=atanh_log_interval(F(1,9))
e,f=atanh_log_interval(F(1,15))
# ln7=3*ln2-ln(8/7); ln(10/7)=ln(5/4)+ln(8/7).
rlo,rhi=(3*a-f)/(d+f),(3*b-e)/(c+e)
assert 0<rlo<rhi
A,B,C,D=2074774,380295,79,431
assert C*A-B*D==1
alpha_of=lambda r:(A-B*r)/(C*r-D)
lo,hi=alpha_of(rhi),alpha_of(rlo) # decreasing in r
assert 0<lo<hi<1
# Farey parents from Euclidean algorithm, no claim their fractions were found by exhaustive scan.
a0,b0=23798916978108300,40640398818107773
c0,d0=4299092056600837,7341376748224820
p,q=a0+c0,b0+d0
assert b0*c0-a0*d0==1
assert p==28098009034709137 and q==47981775566332593
assert F(a0,b0)<lo<F(p,q)<hi<F(c0,d0)
assert q*(hi-lo)<1
assert (q*lo).__floor__()==p-1 and (q*hi).__floor__()==p
# The earlier 26-digit fixed bracket's first ambiguity is now decided unambiguously.
old_q=36493923
assert (old_q*lo).__floor__()==(old_q*hi).__floor__()==21370751
for i in [1,2,391,400,401,old_q-1,old_q,10**9,10**12,q-1]:
    assert (i*lo).__floor__()==(i*hi).__floor__(),i
print('PASS_REFINED_FAREY_UNIFORM_45_TERM_CERT')
print('derived_r_interval_strict',rlo<rhi,'alpha_interval_strict',lo<hi)
print('farey_parents',a0,b0,c0,d0,'det',b0*c0-a0*d0)
print('first_uncertified_index',q,'mediant_num',p)
print('floor_at_first_uncertified', (q*lo).__floor__(),(q*hi).__floor__())
print('old_index_resolved',old_q,'certified_floor',21370751)
print('uniform_certified_index_range',1,q-1)
