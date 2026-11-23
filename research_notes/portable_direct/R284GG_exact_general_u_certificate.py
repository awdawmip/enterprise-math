"""R284GG exact certificate replay (stdlib only). No LP solver required.
Certificate tree generated locally using SciPy/HiGHS and verified with Fraction.
Variables x1,...,x7,q,u. All rows are A*x <= b.
"""
from fractions import Fraction as F
from itertools import combinations
import base64, zlib, json, hashlib

DATA = """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"""
D=9
def row(pats,q=0,u=0):
    a=[0]*D
    a[-2:]=q,u
    for p in pats: a[p-1]+=1
    return tuple(a)
def lower(p,c,d): return (tuple(-x for x in row(p,-c,-d)),-1)
def subsets(a):
    for j in range(1,len(a)+1): yield from combinations(a,j)
G=[[(1,),(3,),(5,7)],[(2,),(6,),(1,5)],[(4,),(3,),(2,5)],[(7,),(6,),(4,5)]]
DI=[(3,6,2,7),(3,6,1,4)]
def bit(p,i): return 0 if i==0 else (p>>(i-1))&1
def last(p,i):
    return next((i-k)%4 for k in range(1,5) if bit(p,(i-k)%4)!=bit(p,(i-k+1)%4))
# Independently reconstruct source groups and opposite-cut incidence.
for i,g in enumerate(G):
    groups={}
    for p in range(1,8):
        if bit(p,i)!=bit(p,(i+1)%4):
            groups.setdefault(last(p,i),[]).append(p)
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
    choices.append([lower(tuple(p for a in sub for p in a),len(sub)+1,4) for sub in subsets(g)])
base=[(row(range(1,8),-4,-8),1),(row([],-1,4),-1)]
for i in range(D):
    v=[0]*D
    v[i]=-1
    base.append((tuple(v),-1 if i==D-1 else 0))
def verify(a,cert):
    assert all(v>=0 for v in cert)
    assert all(sum(v*r[0][j] for v,r in zip(cert,a))==0 for j in range(D))
    assert sum(v*r[1] for v,r in zip(cert,a))<0
def checktree(a,remaining,t):
    if isinstance(t,list):
        c=[F(0)]*len(a)
        seen=set()
        for i,s in t:
            assert 0<=i<len(a) and i not in seen
            seen.add(i)
            c[i]=F(s)
        verify(a,c)
        return 1
    j=t['j']
    assert j in remaining and len(t['children'])==len(choices[j])
    return sum(checktree(a+[v],tuple(k for k in remaining if k!=j),child) for v,child in zip(choices[j],t['children']))
if __name__=='__main__':
    raw=zlib.decompress(base64.b64decode(DATA))
    assert hashlib.sha256(raw).hexdigest()=='e4f5712be8d86aa7b865c0423e14b3194d6548535bcdf294457c52140c69b166'
    data=json.loads(raw)
    counts=[]
    for nh in combinations((3,5,6),2):
        a=base+[(row([p],-2,-2),-1) for p in nh]
        count=checktree(a,tuple(range(6)),data[''.join(map(str,nh))])
        counts.append(count)
        print(nh,count)
    assert counts==[157,159,157]
    print('Exact Farkas coverage verified:',sum(counts))
