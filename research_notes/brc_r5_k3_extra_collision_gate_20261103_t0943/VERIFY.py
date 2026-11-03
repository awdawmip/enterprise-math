#!/usr/bin/env python3
"""Exact rational check of an additional genuine K3 seedless-LR collision."""
from fractions import Fraction as F
from itertools import product

ZERO, ONE = F(0), F(1)
c = F(2, 3)
alpha = (F(1, 2), F(2, 3), F(1, 2), F(3, 4))
r = (F(3, 4),) * 4
v = (F(1, 4), F(3, 4), F(1, 4), F(3, 4))
w_star = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
n = (ZERO, ZERO, F(-1, 2), F(4))
check_count = 0

def check(condition, label):
    global check_count
    assert condition, label
    check_count += 1

def observe(x, y, i, z, t, u):
    assert all(0 <= j <= 1 for j in (x, y, i)) and i <= 1 - x
    ws = (F(1, 4), (1 - x) / 4, y / 8, i / 8)
    d = y / 16 + 3 * i / 32
    M = tuple(ws[s] * alpha[s] * z[s] for s in range(4))
    S = tuple(c * M[s] * t[s] for s in range(4))
    U = tuple(S[s] * u[s] for s in range(4))
    eP = F(107, 128) - F(21, 128)*x + d/4 - sum(S)/2
    eQ = F(13, 64) + F(3, 64)*x - d/2 + sum(S)/8
    TP = F(3) + sum(M) + F(3, 2)*sum(S) + sum(r[s]*U[s] for s in range(4))
    TQ = F(3) + sum(M)/2 + F(3, 8)*sum(S) + sum(v[s]*U[s] for s in range(4))/4
    return (eP,eQ,TP,TQ)

def score(o):
    return sum(n[k]*o[k] for k in range(4))

# Independent support identity using sourcewise positive BRC mass.
g = tuple(v[s]-r[s]/2 for s in range(4))
check(g == (F(-1,8), F(3,8), F(-1,8), F(3,8)), "gate signed scores")
check(sum(w_star)==F(43,96), "mass total")
check(sum(w_star[s]*g[s] for s in range(4))==F(19,256), "signed gate sum")
check(sum(w_star[s]*max(ZERO,g[s]) for s in range(4))==F(25,256), "positive gate sum")
base = F(21, 2) + F(2)*sum(w_star)  # 3/2 + (2/3)(3/4) = 2
expected_FULL = base + c*F(25,256)
expected_LR = base + c*F(19,256)
check(expected_FULL-expected_LR==F(1,64), "gap formula")

FULL_best = None
FULL_arg = None
num_full = 0
for x,y in product((ZERO,ONE), repeat=2):
    for i in ((ZERO,ONE) if x==ZERO else (ZERO,)):
        for bits in product((ZERO,ONE), repeat=12):
            z,t,u = bits[:4], bits[4:8], bits[8:12]
            o = observe(x,y,i,z,t,u)
            val = score(o)
            if FULL_best is None or val>FULL_best:
                FULL_best,FULL_arg = val,(x,y,i,z,t,u,o)
            num_full+=1
check(num_full==24576, "complete FULL vertex count")
LR_best = None
LR_arg = None
num_lr=0
for x,y,z0,t0,u0 in product((ZERO,ONE), repeat=5):
    i=(1-x)*y
    o=observe(x,y,i,(z0,)*4,(t0,)*4,(u0,)*4)
    val=score(o)
    if LR_best is None or val>LR_best:
        LR_best,LR_arg=val,(x,y,z0,t0,u0,o)
    num_lr+=1
check(num_lr==32, "complete LR vertex count")
check(FULL_best==expected_FULL, "full support exhaustive")
check(LR_best==expected_LR, "LR support exhaustive")

W=observe(ZERO,ONE,ONE,(ONE,)*4,(ONE,)*4,(ZERO,ONE,ZERO,ONE))
V=observe(ZERO,ONE,ONE,(ONE,)*4,(ONE,)*4,(ONE,)*4)
check(W == (F(209,288),F(187,1152),F(773,192),F(2587,768)), "explicit FULL witness")
check(V == (F(209,288),F(187,1152),F(791,192),F(2593,768)), "explicit LR support witness")
check(score(W)==FULL_best and score(V)==LR_best, "both witnesses attain supports")
check(tuple(W[k]-V[k] for k in range(4)) == (ZERO,ZERO,F(-3,32),F(-1,128)), "time contrast")
check(score(W)-score(V)==F(1,64), "witness strict gap")
check((score(W)-LR_best)/sum(abs(j) for j in n)==F(1,288), "supnorm lower bound")

# Nonbinary strategy checks and source-wise exact physical clock increments.
for k in range(1,41):
    x=F(k%7,11); y=F((3*k)%11,13); i=(1-x)*F((5*k)%13,17)
    z=tuple(F((k+2*s)%17,19) for s in range(4))
    t=tuple(F((2*k+3*s)%19,23) for s in range(4))
    u=tuple(F((7*k+s)%23,29) for s in range(4))
    o=observe(x,y,i,z,t,u)
    o0=observe(x,y,i,z,t,(ZERO,)*4)
    ws=(F(1,4),(1-x)/4,y/8,i/8)
    U=tuple(c*ws[s]*alpha[s]*z[s]*t[s]*u[s] for s in range(4))
    check(o[:2]==o0[:2], "post-K3 gate does not change answers")
    check(o[2]-o0[2]==sum(r[s]*U[s] for s in range(4)), "P clock exact gate sum")
    check(o[3]-o0[3]==sum(v[s]*U[s] for s in range(4))/4, "Q clock exact gate sum")

print("PASS_EXACT_R5_NEW_K3_COLLISION_GATE")
print("assertions=",check_count)
print("enumerated_FULL_vertices=",num_full, "enumerated_LR_vertices=",num_lr)
print("positive_gate_sum=",F(25,256), "LR_signed_gate_sum=",F(19,256))
print("h_FULL=",FULL_best,"h_LR=",LR_best,"exact_gap=",FULL_best-LR_best)
print("FULL_W=",W)
print("LR_V=",V)
print("supnorm_distance_lower_bound=",F(1,288))
print("nonbinary_exact_flow_cases=",40)
