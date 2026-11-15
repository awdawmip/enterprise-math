#!/usr/bin/env python3
"""X6 signed N=2500 free shortest-BRC: exact six-axis DP, independent 3+3 check."""
from collections import defaultdict
from math import comb, factorial, isqrt

N=2500
expected=(102539052,46263931428930653590904265855801056735441499817749479001025131238806458196360489958119492948372)

# Build every signed-axis endpoint up to norm N, accounting for exact path shuffles.
states={(0,0,0):1}
for _ in range(6):
    new=defaultdict(int)
    for (q,L,s),w in states.items():
        for k in range(isqrt(N-q)+1):
            new[q+k*k,L+k,s+(k>0)]+=w*(2 if k else 1)*comb(L+k,k)
    states=new
support_mass=defaultdict(int)
for (q,L,s),w in states.items():
    if q==N: support_mass[s]+=w
assert support_mass[1]+support_mass[2]==6641732296455342852372
assert sum(support_mass.values())==expected[1]

# Independent enumeration of absolute triples, then 3+3 shuffle convolution.
fac=[factorial(i) for i in range(125)]
three=defaultdict(lambda: defaultdict(int))
end=defaultdict(int)
for a in range(51):
    for b in range(isqrt(N-a*a)+1):
        for c in range(isqrt(N-a*a-b*b)+1):
            q=a*a+b*b+c*c; L=a+b+c
            signed=1 << ((a>0)+(b>0)+(c>0))
            three[q][L]+=signed*fac[L]//(fac[a]*fac[b]*fac[c])
            end[q]+=signed
paths=0
for q,left in three.items():
    for L,u in left.items():
        for M,v in three.get(N-q,{}).items():
            paths+=u*v*comb(L+M,L)
endpoints=sum(end[q]*end[N-q] for q in range(N+1))

# Classical Jacobi six-square representation count, separate from BRC weights.
chi=lambda d: (1 if d%4==1 else -1 if d%4==3 else 0)
divisors=[d for d in range(1,N+1) if N%d==0]
jacobi=16*sum(chi(N//d)*d*d for d in divisors)-4*sum(chi(d)*d*d for d in divisors)
assert endpoints==jacobi==expected[0]
assert paths==expected[1]
print('PASS_X6_FULL_SIGNED_N2500_SIX_AXIS',endpoints,paths)
