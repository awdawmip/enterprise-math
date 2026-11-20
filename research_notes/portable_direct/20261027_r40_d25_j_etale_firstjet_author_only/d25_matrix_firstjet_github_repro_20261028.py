#!/usr/bin/env python3
"""Exact finite-ring replay of the D25 matrix first-jet witness; author-only."""
import itertools
import json


def mul_pair(x,y,m):
    a,b=x; c,d=y
    return ((a*c+2*b*d)%m,(a*d+b*c)%m)


def mul(x,y,m):
    r=len(x)
    return [[tuple(sum(mul_pair(x[i][k],y[k][j],m)[t] for k in range(r))%m
                   for t in (0,1)) for j in range(r)] for i in range(r)]


def sig(x,m):
    return [[(a,-b%m) for a,b in row] for row in x]


def jet(p,a,b):
    r=len(a); m=p*p
    return [[((int(i==j)+p*a[i][j])%m,p*b[i][j]%m)
             for j in range(r)] for i in range(r)]


def check(p,r,a,b,c,d):
    z=[[0]*r for _ in range(r)]
    eta=jet(p,a,b)
    expected=jet(p,[[2*a[i][j]%p for j in range(r)] for i in range(r)],z)
    assert mul(eta,sig(eta,p*p),p*p)==expected
    u=jet(p,c,d)
    uinv=jet(p,[[-v for v in row] for row in c],
                [[-v for v in row] for row in d])
    moved=mul(mul(u,eta,p*p),sig(uinv,p*p),p*p)
    assert moved==jet(p,a,[[(b[i][j]+2*d[i][j])%p for j in range(r)]
                           for i in range(r)])


def main():
    tested=0
    for p in (3,5,7,13,19,373):
        for r in (1,2,3):
            for s in range(9):
                arr=[[[((i+1)*(j+3)+(q+1)*s+s*s)%p for j in range(r)]
                       for i in range(r)] for q in range(4)]
                check(p,r,*arr); tested+=1
    counts=[]
    for p in (3,5,7):
        full=set(); diagonal=set(); scalar=set()
        for B in itertools.product(range(p),repeat=4):
            full.add(B)
            diagonal.add((B[1],B[2]))
            scalar.add((B[1],B[2],(B[0]-B[3])%p))
        assert (len(full),len(diagonal),len(scalar))==(p**4,p**2,p**3)
        counts.append({'p':p,'marked':len(full),'diagonal_orbits':len(diagonal),
                       'scalar_orbits':len(scalar)})
    p=373;z=[[0,0],[0,0]];odd=[[0,1],[0,0]]
    check(p,2,z,z,z,[[0,pow(2,-1,p)],[0,0]])
    assert mul(jet(p,z,odd),sig(jet(p,z,odd),p*p),p*p)==jet(p,z,z)
    print(json.dumps({'status':'PASS_AUTHOR_EXACT_NOT_NATIVE','direct_checks':tested,
          'exhaustive_rank2_counts':counts,'p373_full_gauge_D12':187},indent=2))


if __name__=='__main__':
    main()
