#!/usr/bin/env python3
"""Exact Farey certificate for sharp uniform floor stability of alpha bounds.
Uses the previously certified rational 45-term log bounds; this script certifies
integer inequalities only and does NOT redo the transcendental enclosure proof.
"""
from fractions import Fraction as F
EL,EU = 262921775619052595806,262921775619052595885
DL,DU = 153966341169532252075,153966341169532632370
lo,hi=F(DL,EU),F(DU,EL)
a,b=8236616,14065319
c,d=13134135,22428604
L,R=F(a,b),F(c,d)
p,q=a+c,b+d
assert b*c-a*d==1
assert L<lo<F(p,q)<hi<R
assert p==21370751 and q==36493923
assert (q*lo).__floor__()==p-1
assert (q*hi).__floor__()==p
assert q*(hi-lo)<1
# Ten fixed sample indices, including the sharp boundary, check exact interval floors.
for i in [1,2,390,391,400,401,1000,100000,1000000,q-1]:
    assert (i*lo).__floor__()==(i*hi).__floor__(),i
print('PASS_FAREY_SHARP_UNIFORM_FLOOR_CERT')
print('L',a,b,'R',c,d,'det',b*c-a*d)
print('alpha_bracket',str(lo),str(hi))
print('first_uncertified_index',q,'rational_witness',p,'/',q)
print('floor_lower_at_q',(q*lo).__floor__(),'floor_upper_at_q',(q*hi).__floor__())
print('guaranteed_uniform_indices',1,q-1)
