#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction as F
from itertools import combinations
import json

R=[(2,0,0),(1,3,0),(-1,3,0),(-2,0,0),(-1,-3,0),(1,-3,0)]
U=[(1,1,1),(-1,1,1),(0,-2,1)]
MODELS={
    "FCC_C":R+U+[(0,2,-1),(-1,-1,-1),(1,-1,-1)],
    "HCP_H":R+U+[(1,1,-1),(-1,1,-1),(0,-2,-1)],
}

def sub(a,b): return tuple(a[i]-b[i] for i in range(3))
def dot(a,b): return sum(a[i]*b[i] for i in range(3))
def cross(a,b):
    return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def qshell(a,b):
    x,y,z=sub(a,b); return 3*x*x+y*y+8*z*z

def facets(P):
    out=set()
    for i,j,k in combinations(range(len(P)),3):
        n=cross(sub(P[j],P[i]),sub(P[k],P[i]))
        if n==(0,0,0): continue
        d=dot(n,P[i]); s=[dot(n,p)-d for p in P]
        if all(x>=0 for x in s) or all(x<=0 for x in s):
            f=frozenset(t for t,x in enumerate(s) if x==0)
            if len(f)>=3: out.add(f)
    return sorted(out,key=lambda f:(len(f),tuple(sorted(f))))

def edges(P,Fc):
    return sorted({tuple(sorted((i,j))) for f in Fc for i,j in combinations(f,2) if qshell(P[i],P[j])==12})

def solve3(A,b):
    M=[[F(A[i][j]) for j in range(3)]+[F(b[i])] for i in range(3)]
    for c in range(3):
        r=next(r for r in range(c,3) if M[r][c])
        M[c],M[r]=M[r],M[c]
        z=M[c][c]; M[c]=[x/z for x in M[c]]
        for r in range(3):
            if r==c: continue
            z=M[r][c]
            if z: M[r]=[M[r][j]-z*M[c][j] for j in range(4)]
    return tuple(M[i][3] for i in range(3))

def dual_vertices(P,Fc):
    V=[]
    for f in Fc:
        ids=sorted(f); u=None
        for tri in combinations(ids,3):
            try: q=solve3([P[i] for i in tri],[F(1,2)]*3)
            except (ValueError,StopIteration): continue
            if all(sum(F(P[i][j])*q[j] for j in range(3))==F(1,2) for i in ids):
                u=q; break
        assert u is not None
        assert all(sum(F(p[j])*u[j] for j in range(3))<=F(1,2) for p in P)
        V.append(u)
    return V

def dual_edges(Fc,E):
    D=set()
    for e in E:
        inc=[k for k,f in enumerate(Fc) if set(e)<=f]
        assert len(inc)==2
        D.add(tuple(sorted(inc)))
    return sorted(D)

def qdual(a,b):
    x,y,z=sub(a,b); return 4*x*x+12*y*y+F(3,2)*z*z

def cycle(ids,E):
    adj={i:[] for i in ids}
    for a,b in E:
        adj[a].append(b); adj[b].append(a)
    assert all(len(adj[i])==2 for i in ids)
    s=min(ids); out=[]; prev=None; cur=s
    while True:
        out.append(cur); a,b=adj[cur]; nxt=a if a!=prev else b
        prev,cur=cur,nxt
        if cur==s: break
    assert len(out)==4
    return out

def analyze(name,P):
    assert len(P)==12 and all(qshell((0,0,0),p)==12 for p in P)
    Fc=facets(P); E=edges(P,Fc)
    kinds=Counter()
    for f in Fc:
        d=sorted(qshell(P[i],P[j]) for i,j in combinations(f,2))
        if len(f)==3:
            assert d==[12,12,12]; kinds["triangle"]+=1
        elif len(f)==4:
            assert d==[12,12,12,12,24,24]; kinds["square"]+=1
        else: raise AssertionError
    ef=Counter()
    for e in E:
        inc=[f for f in Fc if set(e)<=f]
        assert len(inc)==2
        a,b=sorted("T" if len(f)==3 else "S" for f in inc)
        ef[a+"-"+b]+=1
    assert (len(P),len(E),len(Fc))==(12,24,14)
    assert len(P)-len(E)+len(Fc)==2 and sum(map(len,Fc))==48
    central=all(tuple(-x for x in p) in set(P) for p in P)

    V=dual_vertices(P,Fc); DE=dual_edges(Fc,E)
    vk=Counter()
    for i in range(12):
        ids=[k for k,f in enumerate(Fc) if i in f]
        FE=[e for e in DE if e[0] in ids and e[1] in ids]
        o=cycle(ids,FE); Q=[V[k] for k in o]
        side=sorted(qdual(Q[j],Q[(j+1)%4]) for j in range(4))
        diag=sorted([qdual(Q[0],Q[2]),qdual(Q[1],Q[3])])
        vec=[sub(Q[(j+1)%4],Q[j]) for j in range(4)]
        par=sum(cross(vec[j],vec[j+2])==(0,0,0) for j in range(2))
        if side==[F(3,8)]*4:
            assert diag==[F(1,2),F(1)] and par==2; vk["rhombus"]+=1
        else:
            assert side==[F(1,6),F(3,8),F(3,8),F(2,3)]
            assert diag==[F(17,24),F(17,24)] and par==1
            vk["isosceles_trapezoid"]+=1
    assert (len(V),len(DE),12)==(14,24,12) and 14-24+12==2
    expected={
        "FCC_C":({"S-T":24},True,{"rhombus":12}),
        "HCP_H":({"S-S":3,"S-T":18,"T-T":3},False,{"rhombus":6,"isosceles_trapezoid":6}),
    }[name]
    assert dict(ef)==expected[0] and central==expected[1] and dict(vk)==expected[2]
    return {
        "shell":{"V":12,"E":24,"F":14,"faces":dict(kinds),"edge_face":dict(ef),"centrally_symmetric":central},
        "voronoi":{"V":14,"E":24,"F":12,"faces":dict(vk)},
    }

def barlow():
    C=Counter()
    for m in "ABC":
        for l in "ABC":
            for r in "ABC":
                if l==m or r==m: continue
                C["HCP_H" if l==r else "FCC_C"]+=1
    assert C==Counter({"HCP_H":6,"FCC_C":6})
    return dict(C)

if __name__=="__main__":
    out={"models":{k:analyze(k,v) for k,v in MODELS.items()},"barlow_local_types":barlow()}
    print(json.dumps(out,sort_keys=True,indent=2))
