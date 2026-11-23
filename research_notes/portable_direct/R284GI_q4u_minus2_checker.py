"""R284GI: all real u>=2, q>=4u-2, nonheavy impossibility.
SciPy finds witnesses; Fraction checks every leaf. No upper parameter bound.
"""
from itertools import combinations
from fractions import Fraction as F
import numpy as np
from scipy.optimize import linprog
D=9
def row(pats,q=0,u=0):
    a=[0]*D; a[-2:]=q,u
    for p in pats: a[p-1]+=1
    return tuple(a)
def lower(p,c,d): return (tuple(-x for x in row(p,-c,-d)),-1)
def bit(p,i): return 0 if i==0 else (p>>(i-1))&1
def last(p,i): return next((i-k)%4 for k in range(1,5) if bit(p,(i-k)%4)!=bit(p,(i-k+1)%4))
G=[[(1,),(3,),(5,7)],[(2,),(6,),(1,5)],[(4,),(3,),(2,5)],[(7,),(6,),(4,5)]]
DI=[(3,6,2,7),(3,6,1,4)]
for i,g in enumerate(G):
    groups={}
    for p in range(1,8):
        if bit(p,i)!=bit(p,(i+1)%4): groups.setdefault(last(p,i),[]).append(p)
    assert sorted(map(tuple,groups.values()))==sorted(g)
for (i,j),(h,k,l,m) in zip(((0,2),(1,3)),DI):
    edges={p:(last(p,i),last(p,j)) for p in range(1,8) if bit(p,i)!=bit(p,j)}
    assert set(edges)=={h,k,l,m}
    def adj(a,b): return any(x==y for x,y in zip(edges[a],edges[b]))
    assert not adj(h,k) and not adj(l,m)
    assert all(adj(a,b) for a in (h,k) for b in (l,m))
choices=[]
for h,j,k,l in DI:
    choices.append([lower((p,),2,2) for p in (h,j,k,l)]+[lower((p,r),3,2) for p in (h,j) for r in (k,l)]+[lower((h,j,k,l),4,2)])
for g in G:
    choices.append([lower(tuple(p for a in sub for p in a),len(sub)+1,4) for j in range(1,len(g)+1) for sub in combinations(g,j)])
base=[(row(range(1,8),-4,-8),1),(row([],-1,4),2),(row([],0,-1),-2)]
for i in range(D):
    v=[0]*D;v[i]=-1;base.append((tuple(v),0))
def exact_certificate(a):
    matrix=np.array([list(v)+[b] for v,b in a],dtype=float).T
    r=linprog(np.ones(len(a)),A_eq=matrix,b_eq=[0]*D+[-1],bounds=(0,None),method='highs')
    assert r.success,r.message
    c=[F(float(x)).limit_denominator(1000000) for x in r.x]
    assert all(v>=0 for v in c)
    assert all(sum(v*r[0][j] for v,r in zip(c,a))==0 for j in range(D))
    assert sum(v*r[1] for v,r in zip(c,a))==-1
    return max(v.denominator for v in c)
def check(a,j):
    r=linprog(np.zeros(D),A_ub=[v for v,b in a],b_ub=[b for v,b in a],bounds=[(None,None)]*D,method='highs')
    if r.status==2: return 1,exact_certificate(a)
    assert r.success,r.message
    assert j<len(choices),('unexpected feasible leaf',r.x)
    c=[check(a+[v],j+1) for v in choices[j]]
    return sum(n for n,d in c),max(d for n,d in c)
if __name__=='__main__':
    for nh in combinations((3,5,6),2):
        print(nh,check(base+[(row([p],-2,-2),-1) for p in nh],0),flush=True)
