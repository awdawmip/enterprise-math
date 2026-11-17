#!/usr/bin/env python3
from itertools import permutations,combinations
from math import factorial
P=list(permutations(range(4)))
I=(0,1,2,3)
def mul(p,q):return tuple(p[q[i]] for i in range(4))
def pow_(x,k,op,e):
    z=e
    for _ in range(k):z=op(z,x)
    return z
def parity(p):return sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2
def cyc(*seq):
    p=list(I)
    for i,j in zip(seq,seq[1:]+seq[:1]):p[i]=j
    return tuple(p)
a=cyc(1,2,3);b=cyc(0,1)
assert pow_(a,3,mul,I)==I and pow_(b,2,mul,I)==I
assert pow_(mul(a,b),4,mul,I)==I
G={I};todo=[I]
while todo:
    g=todo.pop()
    for h in (a,b):
        v=mul(g,h)
        if v not in G:G.add(v);todo.append(v)
assert G==set(P) and len(G)==24
edges=list(combinations(range(4),2))
edge_action=lambda p:tuple(edges.index(tuple(sorted((p[u],p[v])))) for u,v in edges)
assert len({edge_action(p) for p in G})==24
assert all(factorial(n)<24 for n in (1,2,3))
E={(p,j) for p in P for j in range(4) if j%2==parity(p)}
op=lambda x,y:(mul(x[0],y[0]),(x[1]+y[1])%4)
one=(I,0);z=(I,2)
assert len(E)==48
assert all(op(x,y) in E for x in E for y in E)
assert {v for v in E if v[0]==I}=={one,z}
assert all(op(z,x)==op(x,z) for x in E)
A=(a,0);B=(b,1)
assert pow_(A,3,op,one)==one and pow_(B,2,op,one)==z
assert pow_(op(A,B),4,op,one)==one
assert all(pow_((b,j),2,op,one)==z for j in (1,3))
print("PASS |S4|=24, 6-edge faithful S4=24, minimal degree=4")
print("PASS |E|=48, central kernel=C2, extension nonsplit by abelianization")
print("PASS A^3=1,B^2=z,(AB)^4=1; all lifts of b square to z")
