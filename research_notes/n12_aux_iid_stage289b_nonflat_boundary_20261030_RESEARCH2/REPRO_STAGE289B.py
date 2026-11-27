#!/usr/bin/env python3
"""Stage289-B: exact rational boundary-moment / BRC source-leaf witness.

All input and arithmetic are Fraction; checks test the stated n=5,6 examples,
not the universal representation theorem. No floating point and no native X6.
"""
from fractions import Fraction as F


def rank_and_kernel(rows):
    a = [[F(x) for x in row] for row in rows]
    nr, nc = len(a), len(a[0])
    piv = []
    k = 0
    for c in range(nc):
        j = next((i for i in range(k, nr) if a[i][c]), None)
        if j is None:
            continue
        a[k], a[j] = a[j], a[k]
        scale = a[k][c]
        a[k] = [x / scale for x in a[k]]
        for i in range(nr):
            if i != k:
                v = a[i][c]
                a[i] = [x-v*y for x, y in zip(a[i],a[k])]
        piv.append(c)
        k += 1
        if k == nr:
            break
    free = [c for c in range(nc) if c not in piv]
    if not free:
        return len(piv), None
    v = [F(0)] * nc
    v[free[0]] = 1
    for i, c in enumerate(piv):
        v[c] = -a[i][free[0]]
    assert all(sum(x*y for x,y in zip(row,v))==0 for row in rows)
    return len(piv), v


def hankel(m, order):
    return [[m[i+j] for j in range(order+1)] for i in range(order+1)]


def localizer(m, order, variant):
    if variant=='t':
        return [[m[i+j+1] for j in range(order+1)] for i in range(order+1)]
    if variant=='t(1-t)':
        return [[m[i+j+1]-m[i+j+2] for j in range(order+1)] for i in range(order+1)]
    raise ValueError(variant)


def pair_powers(n):
    s=[F(2),F(1)]
    while len(s)<=n:
        s.append(s[-1]-s[-2]/8)
    return s


def poly_value(coeffs,t):
    return sum(a*t**i for i,a in enumerate(coeffs))


def sturm_variations(t):
    # Exact Sturm chain for 8t^2-8t+1: [P,P',-rem(P/P')]=[P,16t-8,1].
    values=(poly_value((F(1),F(-8),F(8)),t), 16*t-8, F(1))
    assert all(z!=0 for z in values)
    signs=[1 if z>0 else -1 for z in values]
    return sum(a!=b for a,b in zip(signs, signs[1:]))


def check_case(n, m, weights):
    d=n//2
    hhi=rank_and_kernel(hankel(m,d))[0]
    hlo=rank_and_kernel(hankel(m,d-1))[0]
    variant='t' if n%2 else 't(1-t)'
    loc=localizer(m,d if n%2 else d-1,variant)
    lrank, ker=rank_and_kernel(loc)
    assert hhi==d+1 and hlo==d and lrank==2
    assert ker is not None
    q=(F(1,8),F(-1),F(1))
    assert ker==list(q), (n,ker)
    assert sum(q[i]*q[j] * (
        m[i+j+1] if variant=='t' else m[i+j+1]-m[i+j+2])
        for i in range(3) for j in range(3))==0
    # Algebraic pair has x+y=1, xy=1/8, hence power sum s_k.
    s=pair_powers(n)
    if n==5:
        assert weights==[F(1,2),F(1,4),F(1,4)]
        assert m==[F(1)]+[s[k]/4 for k in range(1,n+1)]
        assert 8*(m[1]-m[2])==F(1,2)
    else:
        assert n==6 and weights==[F(1,4)]*4
        assert m==[F(1)]+[(1+s[k])/4 for k in range(1,n+1)]
        assert 8*(m[1]-m[2])==F(1,2)
        assert 8*(m[2]-m[3])==F(1,4)
    terminal=[m[j]-m[j+1] for j in range(n)]+[m[n]]
    assert sum(terminal)==1 and all(x>0 for x in terminal)
    # A full ordered leaf records RS, X, T=R XOR X, 1^j0 / 1^n.
    sources={
        'P':(F(1,16),F(3,16),F(9,16),F(3,16)),
        'Q':(F(1,9),F(2,9),F(4,9),F(2,9)),
    }
    for source,prob in sources.items():
        leaves={}
        for rs, p in enumerate(prob):
            r,sbit=divmod(rs,2)
            for x in (0,1):
                for j,bj in enumerate(terminal):
                    t=r^x
                    leaves[(r,sbit,x,t,j)]=p*F(1,2)*bj
        assert len(leaves)==4*2*(n+1)
        assert all(w>0 for w in leaves.values())
        assert sum(leaves.values())==1
        for x in (0,1):
            for j,bj in enumerate(terminal):
                assert sum(w for (r,s,xx,t,jj),w in leaves.items()
                           if xx==x and jj==j)==F(1,2)*bj
        print(f'N{n}_SOURCE_{source}_LEAVES {len(leaves)} MASS {sum(leaves.values())}')
    print(f'N{n}_MOMENTS',','.join(map(str,m)))
    print(f'N{n}_H_RANKS',hlo,hhi,'LOCALIZER_RANK',lrank)
    print(f'N{n}_LOCALIZER_NULL',','.join(map(str,ker)))
    print(f'N{n}_TERMINAL',','.join(map(str,terminal)))


def main():
    assert [(sturm_variations(a),sturm_variations(b)) for a,b in
            [(F(1,8),F(3,16)),(F(13,16),F(7,8))]]==[(2,1),(1,0)]
    assert 5**2<32<6**2  # irreducible quadratic, no rational roots
    print('STURM_RATIONAL_ROOT_COUNTS (1/8,3/16)=1 (13/16,7/8)=1')
    s=pair_powers(6)
    odd=[F(1)]+[s[k]/4 for k in range(1,6)]
    even=[F(1)]+[(1+s[k])/4 for k in range(1,7)]
    assert odd==[F(1),F(1,4),F(3,16),F(5,32),F(17,128),F(29,256)]
    assert even==[F(1),F(1,2),F(7,16),F(13,32),F(49,128),F(93,256),F(355,1024)]
    check_case(5,odd,[F(1,2),F(1,4),F(1,4)])
    check_case(6,even,[F(1,4)]*4)
    print('STAGE289B_NONFLAT_BOUNDARY_EXACT_PASS')


if __name__=='__main__':
    main()
