#!/usr/bin/env python3
"""Exact rational verification: Stage288-B flat Hausdorff moment atomic certificates.

A checker for stated finite instances. General theorems are proved separately.
Stdlib Fraction only; no floats or numerical root solver.
"""
from fractions import Fraction as F


def mat_rank(rows):
    if not rows:
        return 0
    a = [[F(v) for v in row] for row in rows]
    h, w, rank = len(a), len(a[0]), 0
    for col in range(w):
        pivot = next((i for i in range(rank, h) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [v / scale for v in a[rank]]
        for i in range(h):
            if i != rank and a[i][col]:
                factor = a[i][col]
                a[i] = [x-factor*y for x,y in zip(a[i],a[rank])]
        rank += 1
        if rank == h:
            break
    return rank


def exact_solve(a, b):
    n = len(a)
    assert n and all(len(row) == n for row in a) and len(b) == n
    v = [[F(x) for x in row] + [F(rhs)] for row, rhs in zip(a,b)]
    for k in range(n):
        p = next((i for i in range(k,n) if v[i][k]), None)
        assert p is not None, 'Singular input matrix'
        v[k],v[p] = v[p],v[k]
        scale=v[k][k]
        v[k]=[x/scale for x in v[k]]
        for i in range(n):
            if i != k:
                t=v[i][k]
                v[i]=[x-t*y for x,y in zip(v[i],v[k])]
    return [v[i][-1] for i in range(n)]


def gram(m, d):
    return [[m[i+j] for j in range(d+1)] for i in range(d+1)]


def square_expectation(coeffs,m):
    assert len(m) >= 2*len(coeffs)-1
    return sum(coeffs[i]*coeffs[j]*m[i+j] for i in range(len(coeffs)) for j in range(len(coeffs)))


def flat_annihilator(m, d):
    assert len(m) >= 2*d+1
    r = mat_rank(gram(m,d))
    assert 1 <= r <= d and mat_rank(gram(m,d-1)) == r
    a = [[m[i+j] for j in range(r)] for i in range(r)]
    c = exact_solve(a,[-m[r+i] for i in range(r)])
    q = c+[F(1)]
    assert square_expectation(q,m) == 0
    assert all(sum(q[j]*m[k+j] for j in range(r+1))==0 for k in range(2*d-r+1))
    return r,q


def rational_irrational_pair(n):
    assert n >= 4
    m=[F(1),F(1,2)]
    while len(m) <= n:
        m.append(m[-1]-m[-2]/8)
    return m


def rational_poly(q,t):
    return sum(v*t**j for j,v in enumerate(q))


def verify_rank_two():
    m=rational_irrational_pair(5)
    assert m == [F(1),F(1,2),F(3,8),F(5,16),F(17,64),F(29,128)]
    r,q=flat_annihilator(m,2)
    assert (r,q)==(2,[F(1,8),F(-1),F(1)])
    Fpol=[F(8)*v for v in q]
    # Actual sign changes with monotonic branches on either side of 1/2:
    assert rational_poly(Fpol,F(1,8))>0
    assert rational_poly(Fpol,F(3,16))<0
    assert rational_poly(Fpol,F(13,16))<0
    assert rational_poly(Fpol,F(7,8))>0
    # Discriminant of primitive polynomial 8x^2 - 8x + 1 = 32, not Q-square.
    assert (-8)**2-4*8*1==32
    assert 5**2<32<6**2
    # Symmetric root sums yield moments without evaluating irrational roots.
    power=[F(2),F(1)]
    while len(power)<=5:
        power.append(power[-1]-power[-2]/8)
    assert all(m[k]==power[k]/2 for k in range(6))
    return m,q


def verify_rank_three():
    two=rational_irrational_pair(6)
    m=[two[k]/2 + F(1,2)*(F(1,2)**k) for k in range(7)]
    assert m==[F(1),F(1,2),F(5,16),F(7,32),F(21,128),F(33,256),F(107,1024)]
    r,q=flat_annihilator(m,3)
    assert r==3 and q==[F(-1,16),F(5,8),F(-3,2),F(1)]
    # q3=(t-1/2)*(t^2-t+1/8), weights 1/4,1/2,1/4.
    return m,q


def verify_brc_two_sources(m):
    p=(F(1,16),F(3,16),F(9,16),F(3,16))
    q=(F(1,9),F(2,9),F(4,9),F(2,9))
    n=len(m)-1
    terminal=[m[j]-m[j+1] for j in range(n)]+[m[n]]
    assert sum(terminal)==1 and all(x>0 for x in terminal)
    assert terminal==[F(1,2),F(1,8),F(1,16),F(3,64),F(5,128),F(29,128)]
    summaries=[]
    for source,weights in (('P',p),('Q',q)):
        leaves={}
        for i,w in enumerate(weights):
            r=i//2
            s=i%2
            for x in (0,1):
                t=r^x
                for j,v in enumerate(terminal):
                    leaves[(r,s,x,t,j)]=w*F(1,2)*v
        assert len(leaves)==48 and all(v>0 for v in leaves.values())
        assert sum(leaves.values())==1
        for x in (0,1):
            for j in range(n+1):
                assert sum(v for (r,s,xx,t,jj),v in leaves.items() if xx==x and jj==j)==F(1,2)*terminal[j]
        summaries.append((source,len(leaves),sum(leaves.values())))
    return terminal,summaries


def verify_rational_interior():
    # Boole's 5-node positive rational quadrature integrates t^0,...,t^5.
    nodes=(F(0),F(1,4),F(1,2),F(3,4),F(1))
    weights=(F(7,90),F(32,90),F(12,90),F(32,90),F(7,90))
    assert all(w>0 for w in weights)
    assert sum(weights)==1
    for k in range(6):
        assert sum(w*t**k for t,w in zip(nodes,weights))==F(1,k+1)
    return nodes,weights


def main():
    m2,q2=verify_rank_two()
    m3,q3=verify_rank_three()
    terminal,summaries=verify_brc_two_sources(m2)
    nodes,weights=verify_rational_interior()
    print('RANK2_MOMENTS',','.join(str(v) for v in m2))
    print('RANK2_ANNIHILATOR_LOW_TO_HIGH',','.join(str(v) for v in q2))
    print('RANK3_MOMENTS',','.join(str(v) for v in m3))
    print('RANK3_ANNIHILATOR_LOW_TO_HIGH',','.join(str(v) for v in q3))
    print('BOOLE_RATIONAL_NODES',','.join(str(v) for v in nodes))
    print('BOOLE_RATIONAL_WEIGHTS',','.join(str(v) for v in weights))
    print('N5_TERMINAL_DISTRIBUTION',','.join(str(v) for v in terminal))
    for source,count,total in summaries:
        print('BRC_LEAVES',source,count,'TOTAL',total)
    print('STAGE288B_FLAT_ALGEBRAIC_CERTIFICATE_EXACT_PASS')

if __name__=='__main__':
    main()
