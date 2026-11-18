#!/usr/bin/env python3
"""Exact rational and critical-cell certificate for S23/AV plateau 20.
Uses Python stdlib only. Every assertion is an integer/Fraction test.
"""
from fractions import Fraction as F

Q = 10**26
LO = 545569623581288298975349314
HI = LO + 1
H = 7607279
M = 41880515


def log_bounds(z):
    total, term = F(0), z
    for k in range(45):
        total += 2 * term / (2 * k + 1)
        term *= z*z
    return total, total + 2*term/(91*(1-z*z))

# ln(7)/ln(10/7) = (3 ln 2 - ln(8/7))/(ln(5/4)+ln(8/7)).
a, b = log_bounds(F(1, 3))
c, d = log_bounds(F(1, 9))
e, f = log_bounds(F(1, 15))
assert F(LO, Q) < (3*a-f)/(d+f)
assert (3*b-e)/(c+e) < F(HI, Q)


def enc(A, B):
    """Return integer lower/upper numerators for A+B*r in units Q."""
    return (A*Q + B*(LO if B >= 0 else HI),
            A*Q + B*(HI if B >= 0 else LO))

EL, EU = enc(-431, 79)             # epsilon = 79r-431
TL, TU = enc(-60, 11)             # eta = 11r-60
GL, GU = enc(371, -68)           # gamma = eta-epsilon
DL, DU = enc(2074774, -380295)  # d = 2074774-380295r
assert 0 < DL < DU < EL < EU
assert TL > 4800*EU and GL > 6*EU
assert EU*(H+79) < 21*Q
assert 79*60-11*431 == -1

# If x=a*epsilon+b*eta is positive and <epsilon, the exact
# integer b=79*x-epsilon*dv satisfies -21<b<21. If b=0,
# x is an integer multiple of epsilon, hence is not in (0,epsilon).
# For each b != 0 the integer a is unique. Enumerate all 40 values.
narrow = []
for beta in range(-20, 21):
    if not beta:
        continue
    qlo = abs(beta)*TL//EU
    qhi = abs(beta)*TU//EL
    assert qlo == qhi, (beta, qlo, qhi)
    aa = -qlo if beta > 0 else qlo+1
    dv, dj = 79*aa+11*beta, 431*aa+60*beta
    wl, wu = enc(-dj, dv)
    assert 0 < wl < wu < EL
    cost = max(max(dv,0)+max(dj,0), max(-dv,0)+max(-dj,0))
    if cost <= H:
        assert (dv > 0 and dj > 0) or (dv < 0 and dj < 0)
        narrow.append((beta, aa, dv, dj, cost, wl, wu))
assert [z[:5] for z in narrow] == [
    (-3,14444,1141043,6225184,7366227),
    (-2,9630,760748,4150410,4911158),
    (-1,4815,380374,2075205,2455579),
    (1,-4814,-380295,-2074774,2455069),
    (2,-9629,-760669,-4149979,4910648),
    (3,-14443,-1140964,-6224753,7365717),
]
print('PASS_GLOBAL_NARROW_CLASSIFICATION', 'tested_beta', 40,
      'embeddable_types',len(narrow), 'H',H)

# Translated witness (K,L) produces prefix (K-j,L-v), of length
# K+L-(v+j), and positive gap offset delta=K-r*L.
witnesses = []
for i in range(1, 21):
    ai = i*DL//EU
    assert ai*EU < i*DL and i*DU < (ai+1)*EL
    L, K = 380295*i+79*ai, 2074774*i+431*ai
    dl, du = enc(K,-L)
    assert 0 < dl < du < EL
    witnesses.append((i,ai,L,K,dl,du))
assert witnesses[18][2] == 7226474  # V19
assert witnesses[19][2] == 7606769  # V20
assert witnesses[19][3] == 41500221 # K20
assert H == witnesses[19][2]+510
assert M == witnesses[19][2]+witnesses[19][3]-(witnesses[18][2]+1)

# Each witness is blocked only by narrow displacements whose width
# is strictly smaller than its positive offset; comparisons certified
# by opposite rational endpoints, with no numeric decision thresholds.
blocked = {}
for i,ai,L,K,dl,du in witnesses:
    items = []
    for beta,aa,dv,dj,cost,wl,wu in narrow:
        if K == -dj and L == -dv:  # exact equality: also blocks strict entry
            items.append((beta,dv,dj,cost))
        else:
            assert du < wl or wu < dl, ('undecided_width_order',i,beta)
            if wu < dl:
                items.append((beta,dv,dj,cost))
    blocked[i] = items


def cuts(raw, upper):
    return sorted({0,upper+1} | {v for v in raw if 0<v<=upper})

# For p=(v,j), write s=v+j. Each admissibility test is a threshold
# on exactly one of v, j, s. Partition the integer triangle into
# critical cells where ALL such predicates are constant.
V20 = witnesses[-1][2]
v_cuts = cuts([L+1 for i,ai,L,K,dl,du in witnesses] +
              [-dv for beta,aa,dv,dj,cost,wl,wu in narrow if dv < 0], V20)
j_cuts = cuts([K+1 for i,ai,L,K,dl,du in witnesses] +
              [-dj for beta,aa,dv,dj,cost,wl,wu in narrow if dj < 0], H)
s_cuts = cuts([K+L-M for i,ai,L,K,dl,du in witnesses] +
              [H-cost+1 for beta,aa,dv,dj,cost,wl,wu in narrow if dv > 0], H)
assert (len(v_cuts),len(j_cuts),len(s_cuts)) == (24,8,8)
feasible_count = 0
usage = {}
for vv in range(len(v_cuts)-1):
    vl,vh = v_cuts[vv],v_cuts[vv+1]-1
    for jj in range(len(j_cuts)-1):
        jl,jh = j_cuts[jj],j_cuts[jj+1]-1
        for ss in range(len(s_cuts)-1):
            sl,sh = s_cuts[ss],s_cuts[ss+1]-1
            # Every integer between vl+jl and vh+jh occurs as v+j.
            if max(vl+jl,sl)>min(vh+jh,sh):
                continue
            feasible_count += 1
            found = False
            for i,ai,L,K,dl,du in witnesses:
                if vh > L or jh > K or sl < K+L-M:
                    continue
                # A narrow forward displacement (+,+) is possible iff
                # s <= H-cost. A backward one (-,-) iff both coordinates
                # exceed its required magnitude. Split boundaries make
                # these booleans constant throughout the critical cell.
                if any((sh <= H-cost if dv>0 else
                        vl >= -dv and jl >= -dj)
                       for beta,dv,dj,cost in blocked[i]):
                    continue
                usage[i] = usage.get(i,0)+1
                found = True
                break
            assert found, ('uncovered_critical_cell',vl,vh,jl,jh,sl,sh)
assert feasible_count == 194
print('PASS_CRITICAL_CELL_COVER', 'feasible_cells',feasible_count,
      'uncovered',0, 'used_witnesses',len(usage))

# Top v>V20: j<=509. The exact gamma spacing lemma follows by
# unimodular-coefficient sign cases (proved in PROOF.md).
# The six m offsets below all lie strictly between 0 and gamma.
V,K = witnesses[-1][2:4]
for m in range(1,7):
    L = V+68+79*m
    KK = K+371+431*m
    al,au = enc(KK,-L)
    assert 0 < al < au < GL
    assert KK > H
    assert KK+L-(V+1) <= M
assert V+68+79*6 >= H
print('PASS_TOP_ROWS', H-V20, 'gamma_witnesses',6)

# Exterior cells: E(0,ell)<-H and E(k,0)>rH.
left = H*Q//LO+1
right = HI*H//Q+1
assert LO*left>H*Q and right*Q>HI*H
assert max(left,right) <= M
print('PASS_EXTERIOR',left,right)

# Previous universal scaled-gap first-entry theorem at t=V19+1
# gives exact lower bound K20+V20-t; together with the covered upper
# endpoint and monotonicity this proves the plateau on integer h.
t = witnesses[18][2]+1
assert t+510 == 7226985 and H == 7607279
assert K+V-t == M
print('PASS_PLATEAU20', 'h_start',t+510, 'h_end',H,'N_exact',M)
print('PASS_S23_AV_ANALYTIC_PLATEAU_20_CRITICAL_CELLS')
