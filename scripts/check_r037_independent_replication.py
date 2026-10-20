#!/usr/bin/env python3
"""Independent R037 FCC/HCP/Barlow replication runner.

This file intentionally does not import or execute the frozen R033/R034 experiment
implementations.  It rebuilds the graph models from the taskbook definitions and
uses integer/Fraction arithmetic for theorem-critical checks.
"""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from fractions import Fraction as F
import json

FCC_DIRS = (
    (0,-1,-1),(0,-1,1),(0,1,-1),(0,1,1),
    (-1,0,-1),(-1,0,1),(1,0,-1),(1,0,1),
    (-1,-1,0),(-1,1,0),(1,-1,0),(1,1,0),
)
TRI = ((1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1))
NEG_TRI = ((0,0),(-1,0),(0,-1))
POS_TRI = ((0,0),(1,0),(0,1))


def fcc_neighbors(p):
    x,y,z=p
    return tuple((x+a,y+b,z+c) for a,b,c in FCC_DIRS)


def hcp_neighbors(p):
    i,j,k=p
    same=[(i+a,j+b,k) for a,b in TRI]
    shifts=POS_TRI if (k & 1) else NEG_TRI
    return tuple(same+[(i+a,j+b,k-1) for a,b in shifts]+[(i+a,j+b,k+1) for a,b in shifts])


def fcc_distance(p):
    x,y,z=p
    if (x+y+z) & 1:
        raise ValueError("FCC state must lie in D3")
    a,b,c=abs(x),abs(y),abs(z)
    return max(max(a,b,c),(a+b+c)//2)


def hex_norm(i,j):
    return max(abs(i),abs(j),abs(i+j))


def hcp_distance(p):
    i,j,k=p
    t=abs(k)
    if t % 2 == 0:
        return max(t,t//2+hex_norm(i,j))
    m=(t-1)//2
    h=min(hex_norm(i,j),hex_norm(i+1,j),hex_norm(i,j+1))
    return t+max(0,h-m)


def bfs(neighbors, radius):
    origin=(0,0,0)
    dist={origin:0}
    q=deque([origin])
    while q:
        p=q.popleft()
        if dist[p] >= radius:
            continue
        for z in neighbors(p):
            if z not in dist:
                dist[z]=dist[p]+1
                q.append(z)
    return dist


def path_counts(neighbors, N):
    rows=[]
    counts={(0,0,0):1}
    for n in range(N+1):
        rows.append(dict(counts))
        if n == N:
            break
        nxt=defaultdict(int)
        for p,c in counts.items():
            for q in neighbors(p):
                nxt[q]+=c
        counts=nxt
    return rows


def fcc_r2(p):
    x,y,z=p
    return F(x*x+y*y+z*z,2)


def hcp_r2(p):
    i,j,k=p
    s=F(1,3) if (k & 1) else F(0)
    u,v=F(i)+s,F(j)+s
    return u*u+u*v+v*v+F(2,3)*k*k


def radial_moment(row, r2, power, n):
    return sum(F(c)*r2(p)**power for p,c in row.items()) / 12**n


def shell_edge_stats(neighbors, distance, r):
    d=bfs(neighbors,r+1)
    shell={p for p,v in d.items() if v == r}
    induced=sum(1 for p in shell for q in neighbors(p) if q in shell)//2
    exposed=sum(1 for p in shell for q in neighbors(p) if distance(q)>r)
    return induced,exposed


def barlow_neighbors(p, eps):
    """General ideal Barlow graph in a layer-coordinate gauge.

    eps(k) in {+1,-1} is the registry turn from layer k to k+1.  Consecutive
    layers are therefore always distinct; arbitrary bi-infinite eps encodes any
    legal Barlow stacking.
    """
    i,j,k=p
    same=[(i+a,j+b,k) for a,b in TRI]
    up=NEG_TRI if eps(k)==1 else POS_TRI
    down=POS_TRI if eps(k-1)==1 else NEG_TRI
    return tuple(same+[(i+a,j+b,k+1) for a,b in up]+[(i+a,j+b,k-1) for a,b in down])


def barlow_returns(eps,N=12):
    rows=path_counts(lambda p: barlow_neighbors(p,eps),N)
    return [row.get((0,0,0),0) for row in rows]


def run():
    # Independent distance/BFS route, r=0..20.
    df=bfs(fcc_neighbors,20)
    dh=bfs(hcp_neighbors,20)
    assert all(fcc_distance(p)==r for p,r in df.items())
    assert all(hcp_distance(p)==r for p,r in dh.items())
    Af=[sum(v==r for v in df.values()) for r in range(21)]
    Ah=[sum(v==r for v in dh.values()) for r in range(21)]
    assert Af[0]==Ah[0]==1
    assert all(Af[r]==10*r*r+2 for r in range(1,21))
    assert all(Ah[r]==((21*r*r+4)//2 if r%2==0 else (21*r*r+3)//2) for r in range(1,21))

    # Shell adjacency and exposed-face crossing counts.
    for r in range(1,9):
        ef,of=shell_edge_stats(fcc_neighbors,fcc_distance,r)
        eh,oh=shell_edge_stats(hcp_neighbors,hcp_distance,r)
        assert ef==24*r*r
        assert eh==(27*r*r if r%2==0 else 27*r*r-3)
        assert of==oh==12*(3*r*r+3*r+1)

    # Exact integer path counts and exact radial moments through n=12.
    pf=path_counts(fcc_neighbors,12)
    ph=path_counts(hcp_neighbors,12)
    supports=[]
    returns=[]
    for n in range(13):
        supports.append([len(pf[n]),len(ph[n])])
        rf=pf[n].get((0,0,0),0); rh=ph[n].get((0,0,0),0)
        returns.append([rf,rh])
        assert rf==rh
        assert radial_moment(pf[n],fcc_r2,1,n)==n
        assert radial_moment(ph[n],hcp_r2,1,n)==n
        target4=F(5*n*n-2*n,3)
        assert radial_moment(pf[n],fcc_r2,2,n)==target4
        assert radial_moment(ph[n],hcp_r2,2,n)==target4
        if n>=1:
            f6=F(n*(35*n*n-42*n+16),9)
            h6=F(210*n**3-252*n*n+95*n+1,54)
            assert radial_moment(pf[n],fcc_r2,3,n)==f6
            assert radial_moment(ph[n],hcp_r2,3,n)==h6
            assert h6-f6==-F(n-1,54)
    assert supports[2]==[55,57]
    assert Counter(pf[2].values())==Counter({1:12,2:24,4:18,12:1})
    assert Counter(ph[2].values())==Counter({1:18,2:18,3:2,4:18,12:1})

    # Independent finite return checks for several unrelated legal Barlow stacks.
    patterns=(
        lambda k: 1,
        lambda k: 1 if k%2==0 else -1,
        lambda k: 1 if (k*k+3*k+1)%5 in (0,1,2) else -1,
        lambda k: 1 if ((17*k+5)%7)<3 else -1,
    )
    br=[barlow_returns(e,12) for e in patterns]
    assert all(row==br[0] for row in br[1:])
    assert br[0]==[x[0] for x in returns]

    return {
        "schema":"R037_INDEPENDENT_RUNNER_V1",
        "status":"PASS",
        "distance_bfs_radius":20,
        "fcc_shell_r1_r3":Af[1:4],
        "hcp_shell_r1_r3":Ah[1:4],
        "supports_n0_n12":supports,
        "return_counts_n0_n12":[x[0] for x in returns],
        "barlow_sample_stacks":len(patterns),
        "barlow_returns_equal_through_n":12,
    }


if __name__ == "__main__":
    print(json.dumps(run(),sort_keys=True,separators=(",",":")))
