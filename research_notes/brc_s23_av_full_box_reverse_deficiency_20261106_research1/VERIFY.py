#!/usr/bin/env python3
"""Exact certificates for the full lawful AV-box reverse deficiency, 2026-11-06."""
from fractions import Fraction as F

HALF = F(1, 2)
A_LO, A_HI = F(1, 2), F(7, 8)
C_LO, C_HI = F(1, 2), F(7, 8)
V, D = F(88, 105), F(9, 70)
K_YES = (F(0), F(1), F(0))
K_NO = (V, F(0), 1 - V)
checks = 0

def chk(condition, message):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def av(a, c):
    z = (1-a)*c
    return (a, z, 1-a-z)

def binary(a, c):
    z = (1-a)*c
    return (z, 1-z)

def reconstruct(b):
    return tuple(b[0]*K_YES[j] + b[1]*K_NO[j] for j in range(3))

def tv(p,q):
    return sum(abs(x-y) for x,y in zip(p,q))/2

def bayes(p0,p1,t):
    return sum(min((1-t)*x,t*y) for x,y in zip(p0,p1))

chk(sum(K_YES)==1 and sum(K_NO)==1, 'kernel row sums')
for k in (K_YES,K_NO):
    for p in k:
        chk(F(0)<=p<=1,'kernel entry legal')

corners = ((A_LO,C_LO), (A_LO,C_HI), (A_HI,C_LO), (A_HI,C_HI))
expected = (D, -F(1,35), -F(5,56), -D)
for (a,c), exp in zip(corners,expected):
    p,b = av(a,c),binary(a,c)
    rec=reconstruct(b)
    err=rec[0]-p[0]
    chk(err==exp,'exact corner signed first error')
    chk(rec[1]==p[1], 'stop3 exactly preserved')
    chk(rec[2]-p[2]==-err, 'opposite stop4 residual')
    chk(tv(p,rec)==abs(exp), 'TV at corner')
    chk(abs(exp)<=D, 'sharp uniform corner bound')

chk(expected[0]==D and expected[3]==-D,'two sharp corners')
P0,P1=av(A_LO,C_LO),av(A_HI,C_HI)
B0,B1=binary(A_LO,C_LO),binary(A_HI,C_HI)
t=F(16,35)
rA=bayes(P0,P1,t)
rB=bayes(B0,B1,t)
chk(P0 == (F(1,2),F(1,4),F(1,4)), 'full first witness distribution')
chk(P1 == (F(7,8),F(7,64),F(1,64)), 'full second witness distribution')
chk(B0 == (F(1,4),F(3,4)), 'binary first witness distribution')
chk(B1 == (F(7,64),F(57,64)), 'binary second witness distribution')
chk(rA==F(23,70),'complete experiment Bayes risk')
chk(rB==F(16,35),'coarsened experiment Bayes risk')
chk(rB-rA==D,'matching lower bound')
# A finite exact grid is supplementary; analytic multiaffine corner lemma proves continuum coverage.
for a in (F(1,2),F(9,16),F(5,8),F(3,4),F(7,8)):
    for c in (F(1,2),F(9,16),F(5,8),F(3,4),F(7,8)):
        p=av(a,c)
        b=binary(a,c)
        chk(tv(p,reconstruct(b))<=D,'interior grid check')
print('PASS_EXACT_S23_AV_FULL_BOX_REVERSE_DEFICIENCY_20261106')
print('checker_assertions=',checks)
print('kernel_yes=',','.join(map(str,K_YES)))
print('kernel_no=',','.join(map(str,K_NO)))
print('corner_signed_errors=',','.join(map(str,expected)))
print('witness_prior=',t,'full_risk=',rA,'binary_risk=',rB,'deficiency=',D)
print('scope=all_real_a_c_in_[1/2,7/8]^2_analytic_proof;finite_rational_grid_supplementary')
