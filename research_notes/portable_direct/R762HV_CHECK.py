#!/usr/bin/env python3
"""R762HV exact parity-closure counts and twisted-spectrum certificates.
Only Python standard library; all computations use unbounded integers.
"""
from itertools import combinations
from collections import defaultdict

PORTS = list(combinations(range(6), 2))
EDGES = [[] for _ in PORTS]
for i, p in enumerate(PORTS):
    for j, q in enumerate(PORTS):
        if len(set(p) & set(q)) == 1:
            triple = set(p) | set(q)
            EDGES[i].append((j, sum(1 << a for a in triple)))
assert len(PORTS) == 15 and all(len(es) == 8 for es in EDGES)

# Full mod-2 residue BRC dynamic programming. State=(Port, six-bit parity).
dp = {(0, 0): 1}
E, P = [1], [1]
for n in range(1, 27):
    nd = defaultdict(int)
    for (p, parity), count in dp.items():
        for q, triple_bits in EDGES[p]:
            nd[(q, parity ^ triple_bits)] += count
    dp = nd
    E.append(dp.get((0, 0), 0))
    P.append(sum(count for (p, mask), count in dp.items() if p == 0))
    assert sum(dp.values()) == 8**n
assert all(E[n] == 0 for n in range(1, 27, 2))
for n in range(2, 27, 2):
    assert P[n] == (8**n + 14 * 2**n) // 15

# Independent Fourier/character computation for n<=12, retaining all 64 twists.
sums = [0] * 13
for x in range(64):
    v = [0]*15
    v[0] = 1
    for n in range(1,13):
        v = [sum((-1 if ((x&t).bit_count() & 1) else 1)*v[q]
                 for q,t in EDGES[p]) for p in range(15)]
        sums[n] += v[0]
for n in range(1, 13):
    assert sums[n] % 64 == 0 and sums[n] // 64 == E[n]

# Characteristic polynomials by the exact Newton traces recurrence:
# det(tI-M) = t^15+c_1 t^14+...+c_15.
def matmul(a,b):
    cols = list(zip(*b))
    return [[sum(x*y for x,y in zip(row,col)) for col in cols] for row in a]

def charpoly(x):
    M = [[0]*15 for _ in range(15)]
    for p,es in enumerate(EDGES):
        for q,t in es:
            M[p][q] = -1 if (x&t).bit_count() & 1 else 1
    power = [row[:] for row in M]
    traces = []
    for n in range(1,16):
        traces.append(sum(power[i][i] for i in range(15)))
        if n<15: power=matmul(power,M)
    c=[1]
    for n in range(1,16):
        v=sum(c[n-j]*traces[j-1] for j in range(1,n+1))
        assert v%n==0
        c.append(-v//n)
    return c

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def powpoly(a,k):
    r=[1]
    for _ in range(k):r=mul(r,a)
    return r

def poly(*factors):
    ans=[1]
    for f in factors:ans=mul(ans,f)
    return ans

# polynomials in ascending t powers, reverse for c_0..c_15.
expected={}
expected[0]=poly([-8,1],powpoly([-2,1],5),powpoly([2,1],9))
expected[1]=poly(powpoly([2,1],5),[-32,-2,1],powpoly([-2,-2,1],4))
expected[2]=poly(powpoly([0,1],3),powpoly([2,1],2),[4,1],powpoly([-4,-2,1],3),[32,-28,-2,1])
expected[3]=poly(powpoly([0,1],5),[-28,0,1],powpoly([-6,-2,1],2),powpoly([-6,2,1],2))
for k in range(4):
    actual=list(reversed(charpoly((1<<k)-1)))
    assert actual==expected[k], (k,actual,expected[k])

# Opposite character twists (x and x xor 63) negate the entire matrix.
for k in range(4,7):
    actual=list(reversed(charpoly((1<<k)-1)))
    base=expected[6-k]
    # 15x15: det(tI-(-M)) = -det((-t)I-M).
    should=[(-1)**(15-j)*c for j,c in enumerate(base)]
    assert actual==should, (k,actual,should)

print('PASS R762HV: all 2..26 parity counts, Fourier crosscheck 1..12, all 7 characteristic polynomials')
print('n,parity_even_rooted_loops,all_rooted_loops')
for n in range(2,27,2): print(n,E[n],P[n],sep=',')
