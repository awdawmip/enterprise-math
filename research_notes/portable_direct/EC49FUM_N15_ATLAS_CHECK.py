#!/usr/bin/env python3
"""EC49FUM: exact rational checks for the full n=15 clipped observer atlas.
No external dependencies. Existing component-phase certificates remain separate."""
from fractions import Fraction as Q
from math import comb

N=15
BETA=Q(3,637)
ETA=Q(141024,1653649)
U_E=Q(4822040484,8132285009)
U_I=Q(21829245984,45529434409)

def T(x, end):
    return (1-x)*(1+ETA*x if end=='E' else 1-BETA*x)

def tail(j,z):
    return sum(Q(comb(N,k))*(1-z)**k*z**(N-k) for k in range(j))

def disc(j,x,end):
    z=T(x,end)
    u=U_E if end=='E' else U_I
    return tail(j,z)-tail(j,u*z)

def signed_mass(k,x,end):
    z=T(x,end)
    u=U_E if end=='E' else U_I
    return Q(comb(N,k))*z**(N-k)*((1-u*z)**k*u**(N-k)-(1-z)**k)

def switch_sign(k,x):
    z=T(x,'E'); p=1-z; r=1-U_E*z
    return r**k*U_E**(N-k)-p**k

# Brackets from the immutable cited phase certificates, checked in this program.
assert disc(1,Q(2797,10**7),'E') < disc(1,Q(2797,10**7),'I')
assert disc(1,Q(2798,10**7),'E') > disc(1,Q(2798,10**7),'I')
BRACKETS={
 1:(Q(2956,10**7),Q(2957,10**7)),
 2:(Q(15172,10**6),Q(15174,10**6)),
 3:(Q(59034,10**6),Q(59035,10**6)),
 4:(Q(121675,10**6),Q(121676,10**6)),
 5:(Q(194151,10**6),Q(194152,10**6)),
 6:(Q(271729,10**6),Q(271731,10**6)),
 7:(Q(351933,10**6),Q(351935,10**6)),
 8:(Q(433404,10**6),Q(433407,10**6)),
 9:(Q(515356,10**6),Q(515360,10**6)),
 10:(Q(597317,10**6),Q(597321,10**6)),
 11:(Q(678992,10**6),Q(678996,10**6)),
 12:(Q(760196,10**6),Q(760200,10**6)),
 13:(Q(840810,10**6),Q(840814,10**6)),
 14:(Q(920760,10**6),Q(920764,10**6)),
}
for j,(left,right) in BRACKETS.items():
    assert 0<left<right<1
    assert switch_sign(j,left)>0, (j,'left')
    assert switch_sign(j,right)<0, (j,'right')
    if j>1: assert BRACKETS[j-1][1]<left

# Rational endpoint margin near b_1, from the second-count phase certificate.
for x in BRACKETS[1]:
    gap=disc(2,x,'I')-disc(2,x,'E')
    assert gap>Q(1,20000),('second-count gap',x,gap)
    assert disc(1,x,'E')>disc(1,x,'I')
    assert signed_mass(1,x,'I')<0

# Strict uniform constants for the monotonicity argument.
assert 15*Q(999,1000)**14*Q(9,10)*(1-Q(3,5)**15)>13
assert 420*(Q(1,1000)+Q(3,5)**14)<1
assert U_E<Q(3,5) and U_I<Q(3,5)
assert ETA<Q(1,10) and BETA<Q(1,200)

# Adjacent threshold discrimination differs by signed count-j mass.
for j in range(1,15):
    for x in BRACKETS[j]:
        assert disc(j,x,'E')-disc(j+1,x,'E')==signed_mass(j,x,'E')

# At x=0 the negative hypothesis never hits; at x=1 both always hit.
assert U_E**15/2<Q(1,4000)
assert disc(1,Q(0),'E')==1-U_E**15
assert disc(15,Q(1),'E')==0

print('PASS: exact nuisance crossover and 14 switch brackets;')
print('      count identity, rational derivative bounds and end cases.')
print('V(0) =', float(U_E**15/2))
