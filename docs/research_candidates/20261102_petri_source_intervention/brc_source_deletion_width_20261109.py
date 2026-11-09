"""Exact rational checks for bounded-width source knockout tomography.
External finite source-set model; not the native EM BRC runtime.
"""
from fractions import Fraction as Q
from math import comb


def subsets(m, k=None):
    return tuple(s for s in range(1 << m) if k is None or s.bit_count() <= k)


def knockout(p, u):
    return sum((w for s, w in p.items() if not (s & u)), Q(0))


def recover(m, r, D):
    E = {}
    for t in subsets(m, r):
        E[t] = sum(((-1 if u.bit_count() & 1 else 1) * D[u]
                    for u in subsets(m) if (u & t) == u), Q(0))
    W = {s: Q(0) for s in subsets(m, r)}
    for t, z in E.items():
        u = t
        while True:
            W[u] += (-1 if (t.bit_count()-u.bit_count()) & 1 else 1) * z
            if u == 0:
                break
            u = (u - 1) & t
    return W


def test_positive(m, r):
    allowed = subsets(m, r)
    raw = {s: 1 + ((13*s+7) % 19) for s in allowed}
    total = sum(raw.values())
    p = {s: Q(w,total) for s, w in raw.items()}
    D = {u: knockout(p,u) for u in allowed}
    rec = recover(m,r,D)
    assert rec == p, (m,r,rec,p)
    for u in subsets(m):
        assert knockout(p,u)==knockout(rec,u)
    return {'m':m,'r':r,'N':sum(comb(m,j) for j in range(r+1)),
            'full_table':2**m,'checked_queries':2**m}


def test_sharp(r):
    m=r+1
    even={s:Q(1,2**(m-1)) for s in subsets(m) if s.bit_count()%2==0}
    odd ={s:Q(1,2**(m-1)) for s in subsets(m) if s.bit_count()%2==1}
    for u in subsets(m,r):
        assert knockout(even,u)==knockout(odd,u)==Q(1,2**u.bit_count())
    assert knockout(even,(1<<m)-1)==Q(1,2**r)
    assert knockout(odd, (1<<m)-1)==Q(0)
    return {'r':r,'m':m,'lower_order_queries':sum(comb(m,j) for j in range(r+1)),
            'distinguishing_query':(1<<m)-1,'gap':str(Q(1,2**r))}


if __name__ == '__main__':
    pos=[test_positive(m,r) for m,r in [(3,1),(5,2),(6,3),(8,2),(8,3)]]
    sharp=[test_sharp(r) for r in range(0,7)]
    print('PASS bounded-support inversion',pos)
    print('PASS parity sharpness',sharp)
