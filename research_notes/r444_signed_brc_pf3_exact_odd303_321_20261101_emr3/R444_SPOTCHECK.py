#!/usr/bin/env python3
"""Independent exact permutation checks for indexed R444 3x3 Toeplitz minors."""
import itertools, random, hashlib
from pathlib import Path
p=Path(__file__).parent
rows=p.joinpath('R443_INPUTS.txt').read_text().splitlines()
rng=random.Random(44420261101)
count=0
for line in rows:
    w=list(map(int,line.split()));r,n=w[:2];a=w[2:]
    assert len(a)==n==r-1
    def x(i):return a[i] if 0<=i<n else 0
    chosen=[(0,1,2),(0,n,n+1),(n-1,n,n+1),(1,n-1,n),(3,10,20)]
    chosen += [tuple(sorted(rng.sample(range(n+2),3))) for _ in range(120)]
    for j,k,l in chosen:
        mat=[[x(c-i) for c in (j,k,l)] for i in range(3)]
        direct=0
        for perm in itertools.permutations(range(3)):
            inv=sum(perm[i]>perm[t] for i in range(3) for t in range(i+1,3))
            term=1
            for i in range(3):term*=mat[i][perm[i]]
            direct+=(-1 if inv%2 else 1)*term
        cache=(x(j)*x(k-1)-x(k)*x(j-1))*x(l-2) \
              -(x(j)*x(l-1)-x(l)*x(j-1))*x(k-2) \
              +(x(k)*x(l-1)-x(l)*x(k-1))*x(j-2)
        assert direct==cache and direct>0,(r,j,k,l,direct,cache)
        count+=1
print('R444_SPOTCHECK_PASS rows',len(rows),'independent_minor_checks',count)
