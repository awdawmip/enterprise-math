#!/usr/bin/env python3
"""Exact finite arithmetic certificate for S23/AV capacity plateaux 20..716.
No floating point, threshold-pair enumeration, or extrapolation. Run without -O.
"""
from fractions import Fraction
from hashlib import sha256

MAX_I = 716
Q = 10**26
LO = 545569623581288298975349314
HI = LO + 1


def log_bounds(z):
    total, term = Fraction(0), z
    for m in range(45):
        total += 2*term/(2*m+1)
        term *= z*z
    return total, total + 2*term/(91*(1-z*z))

# Strict rational log enclosure, rebuilt from a convergent series and tail.
a,b = log_bounds(Fraction(1,3))
c,d = log_bounds(Fraction(1,9))
e,f = log_bounds(Fraction(1,15))
assert Fraction(LO,Q) < (3*a-f)/(d+f)
assert (3*b-e)/(c+e) < Fraction(HI,Q)


def bounds(A,B):
    return (A*Q+B*(LO if B>=0 else HI),
            A*Q+B*(HI if B>=0 else LO))

eps_lo,eps_hi = bounds(-431,79)           # epsilon=79r-431
eta_lo,eta_hi = bounds(-60,11)           # eta=11r-60
gamma_lo,gamma_hi = bounds(371,-68)     # gamma=eta-epsilon
d_lo,d_hi = bounds(2074774,-380295)    # d0=2074774-380295r
assert 0 < d_lo < d_hi < eps_lo < eps_hi
assert eta_lo > 4800*eps_hi and gamma_lo > 6*eps_hi
assert 79*60-431*11 == -1

# The exact scaled-gap first-entry theorem supplies the lower bounds.
# Its concrete witness offsets are independently reconstructed here.
witness = {}
for i in range(1,MAX_I+1):
    ai = i*d_lo//eps_hi
    assert ai*eps_hi < i*d_lo and i*d_hi < (ai+1)*eps_lo
    V,K = 380295*i+79*ai, 2074774*i+431*ai
    xlo,xhi = bounds(K,-V)
    assert 0 < xlo < xhi < eps_lo
    witness[i] = (ai,V,K,xlo,xhi)

rows = []
max_classes = 0
max_blocks = 0
last_end = witness[19][1]+510
last_M = witness[19][2]+witness[19][1]-(witness[18][1]+1)

for i in range(20,MAX_I+1):
    ai,V,K,xlo,xhi = witness[i]
    H = V+510
    start = witness[i-1][1]+511
    M = K+V-(witness[i-1][1]+1)
    assert start == last_end+1 and M>last_M
    # For x=a*epsilon+b*eta in (0,epsilon), b=79x-epsilon*dv
    # implies |b|<epsilon*(H+79); cover every possible integer b.
    B = (eps_hi*(H+79)+Q-1)//Q
    narrow=[]
    for beta in range(-B,B+1):
        if beta==0:
            continue
        m=abs(beta)
        rlo = m*eta_lo//eps_hi
        rhi = m*eta_hi//eps_lo
        assert rlo==rhi, (i,beta,rlo,rhi)
        A = -rlo if beta>0 else rlo+1
        dv,dj = 79*A+11*beta,431*A+60*beta
        gap_lo,gap_hi = bounds(-dj,dv)
        assert 0<gap_lo<gap_hi<eps_lo,(i,beta)
        cost=max(max(dv,0)+max(dj,0),max(-dv,0)+max(-dj,0))
        if cost>H:
            continue
        assert dv*dj>0,(i,beta,dv,dj)
        if dv>0:
            low_v,high_v=0,H-cost
        else:
            low_v,high_v=-dv,H+dj
        assert low_v<=high_v
        narrow.append((low_v,high_v,gap_lo,gap_hi,beta))
    max_classes=max(max_classes,len(narrow))

    # A witness (K_s,V_s) covers an entire v-range when all geometrically
    # possible outgoing sub-epsilon differences have width > its offset.
    valid=[]
    for s in range(1,i+1):
        _,Vs,Ks,delta_lo,delta_hi = witness[s]
        if Ks < H:
            continue  # stronger than needed, ensures k=Ks-j >=0 for all j
        left=max(0,Ks+Vs-M)
        right=min(Vs,V)
        if left>right:
            continue
        forbidden=sorted((low_v,high_v) for low_v,high_v,glo,ghi,beta
                         in narrow if glo<=delta_hi)
        cursor=left
        for lo,hi in forbidden:
            if hi<cursor or lo>right:
                continue
            if cursor<lo:
                valid.append((cursor,min(lo-1,right),s))
            cursor=max(cursor,hi+1)
            if cursor>right:
                break
        if cursor<=right:
            valid.append((cursor,right,s))

    # Exact interval covering of all possible bounded-cell left v<=V.
    cursor,selected=0,[]
    while cursor<=V:
        candidates=[(hi,s) for lo,hi,s in valid if lo<=cursor<=hi]
        assert candidates,(i,'UNPROVED_V',cursor)
        hi,s=max(candidates)
        selected.append((cursor,hi,s))
        cursor=hi+1
    assert cursor==V+1
    max_blocks=max(max_blocks,len(selected))

    # The general top-510-row gap lower bound gamma is inherited from
    # predecessor PROOF (integer b decomposition; j<=509). Check six shifts.
    for m in range(1,7):
        L=V+68+79*m
        Ktop=K+371+431*m
        lo,hi=bounds(Ktop,-L)
        assert 0<lo<hi<gamma_lo
        assert Ktop+L-(V+1)<=M
    assert V+68+79*6>=H
    assert K+3498<M

    # Explicit attainability of two exterior cells, with exact strict bounds.
    ext_left=H*Q//LO+1
    ext_right=HI*H//Q+1
    assert LO*ext_left>H*Q and ext_right*Q>HI*H
    assert max(ext_left,ext_right)<=M

    rows.append((i,start,H,M,len(narrow),tuple(selected)))
    last_end,last_M=H,M

# Hash the complete, deterministically reproducible finite block certificate.
certificate=''.join(f'{i}|{a}|{b}|{m}|{ns}|{blocks}\n'
                    for i,a,b,m,ns,blocks in rows).encode('ascii')
print('PASS_LOG_ENCLOSURE', LO,Q,HI)
print('PASS_PLATEAUX', rows[0][0], rows[-1][0], 'count',len(rows))
print('PASS_HORIZON',rows[0][1],rows[-1][2])
print('PASS_LAST_EXACT_CAPACITY',rows[-1][3])
print('PASS_NARROW_MAX',max_classes,'MAX_BLOCKS',max_blocks)
print('CERTIFICATE_SHA256',sha256(certificate).hexdigest())
for i in [20,21,50,100,200,500,716]:
    row=rows[i-20]
    print('CHECKPOINT',row[:5], 'witness_blocks',row[5])
print('PASS_S23_AV_EXACT_PLATEAUX_20_TO_716')
