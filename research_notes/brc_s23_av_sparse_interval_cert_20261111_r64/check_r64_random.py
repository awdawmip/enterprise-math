"""Reproduce R64's 399 seeded exact-rational interval certification experiments."""
from fractions import Fraction as F
from random import Random
from check_r64_min import cert, win

rng=Random(640211)
cases=passed=inconclusive=oracle=0
for _ in range(400):
    m=rng.randint(2,9)
    q=rng.choice([101,103,107,109,113,127,131,137])
    p=rng.randint(1,q-1)
    th=F(p,q)
    j=rng.randint(50,140)
    x=F(rng.randrange(1,26),rng.choice([31,37,41]))
    width=F(1,rng.choice([10000,20000,100000,1000000,5000000,100,180,300]))
    L,U=th-width,th+width
    if L<=0 or U>=1:continue
    size=rng.randint(1,29)
    timestamps=set(rng.sample(range(j-200,j),size))
    z=rng.randrange(m)
    cases+=1
    if cert(th,L,U,m,j,x,timestamps,z):
        passed+=1
        baseline=win(th,m,j,x,timestamps,z)
        for i in range(9):
            assert win(L+(U-L)*F(i,8),m,j,x,timestamps,z)==baseline
            oracle+=1
    else:inconclusive+=1
assert (cases,passed,inconclusive,oracle)==(399,268,131,2412)
print('R64_RANDOM_PASS',cases,passed,inconclusive,oracle)
