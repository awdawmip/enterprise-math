from math import gcd, isqrt, lcm
from collections import Counter
import itertools
import repair,original

def mm(a,b,n):
    return tuple(sum(a[2*i+k]*b[2*k+j] for k in range(2))%n
                 for i in range(2) for j in range(2))
def trace(P,e,n):
    m=(P,-1,1,0)
    r=(1,0,0,1)
    while e:
        if e&1:
            r=mm(r,m,n)
        m=mm(m,m,n)
        e//=2
    return (r[0]+r[3])%n
def assertfactor(r):
    d=r['factor']; n=r['params']['N']
    assert isinstance(d,int) and 1<d<n and n%d==0

assert original.factor_cyclotomic_torus(108391,50,(2,)) is None
assert original.wheel_factorial_dichotomy_factor(1497)==(0,0,'Unsplit')
count=0
for N,P,B in itertools.product(range(3,101),range(2,8),range(2,16)):
    T=P
    for q in repair.prime_powers(B,lambda x:None): T=repair.lucas(T,q,N,lambda x:None)
    assert T==trace(P,lcm(*range(1,B+1)),N)
    count+=1
print('matrix',count)
for N in range(2,100):
    for D in (2,6,12,30,210):
        r=repair.screen(N,7,D,100000,'both')
        if r['status']=='FACTOR_FOUND': assertfactor(r)
        else: assert r['status']=='NO_HIT_IN_DECLARED_SEARCH' and all(N%k for k in range(2,isqrt(N)+1))
        assert r['used']==sum(r['work'].values())
counts=Counter(); misses=[]
for N,D in itertools.product(range(2,1000),(2,6,12,30,210)):
    r=repair.screen(N,7,D,100000,'wheel'); counts[r['status']]+=1
    if r['status']=='FACTOR_FOUND': assertfactor(r)
    else:
        divisors=[k for k in range(2,isqrt(N)+1) if N%k==0]
        if divisors:
            misses.append((N,D)); p=divisors[0]; co=N//p
            assert any(co%k==0 for k in range(2,isqrt(co)+1))
print('wheel',counts,len(misses),misses[:12])
cases=((108391,50,210,'lucas'),(1497,50,210,'wheel'),(97,2,6,'both'),(21,2,210,'wheel'),(121,2,210,'wheel'),(2,2,210,'both'),(15,2,6,'both'))
checks=0
for n,b,d,route in cases:
    full=repair.screen(n,b,d,10000,route); used=full['used']
    for budget in range(used+2):
        r=repair.screen(n,b,d,budget,route)
        assert r['used']==min(used,budget) and sum(r['work'].values())==r['used']
        if budget<used: assert r['status']=='BUDGET_EXHAUSTED' and r['remaining']==0
        else: assert (r['status'],r['factor'])==(full['status'],full['factor'])
        checks+=1
    print(n,route,used,full['factor'],full['degenerate_gcd'])
print('budget',checks)
p=repair.screen(97,2,6,30,'both'); print('mid',p)
assert repair.screen(1)['status']==repair.screen(17,1)['status']==repair.screen(17,2,1)['status']==repair.screen(17,2,6,-1)['status']=='INVALID_INPUT'
assert repair.screen(385,2,2,1000,'wheel')['degenerate_gcd']==2
print('ok')
