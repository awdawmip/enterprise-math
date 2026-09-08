#!/usr/bin/env python3
from __future__ import annotations
import itertools, json
from pathlib import Path

LINES=((1,1,0),(1,-1,0),(1,0,1),(1,0,-1),(0,1,1),(0,1,-1))
AX=(0,2,5,3,4,1)
SLICES={"A":(0,2,5),"B":(0,3,4),"C":(1,2,4),"D":(1,3,5)}
NATIVE={"A":(0,1,2),"B":(0,3,4),"C":(1,4,5),"D":(2,3,5)}
ORIENT={"A":{0:1,2:-1,5:-1},"B":{0:1,3:-1,4:-1},"C":{1:1,2:-1,4:1},"D":{1:1,3:-1,5:1}}
W=tuple(LINES[j] for j in AX)
A=tuple(tuple(W[c][r] for c in range(6)) for r in range(3))
K=((1,-1,-1,0,0,0),(1,0,0,-1,-1,0),(0,-1,0,0,1,1))
HCP=((2,0,0),(1,3,0),(-1,3,0),(-2,0,0),(-1,-3,0),(1,-3,0),(1,1,1),(-1,1,1),(0,-2,1),(1,1,-1),(-1,1,-1),(0,-2,-1))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(M,v): return tuple(sum(M[r][c]*v[c] for c in range(len(v))) for r in range(len(M)))
def mm(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def psign(p): return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def rotations():
    out=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product((-1,1),repeat=3):
            if psign(p)*s[0]*s[1]*s[2]!=1: continue
            out.append(tuple(tuple(s[r] if c==p[r] else 0 for c in range(3)) for r in range(3)))
    assert len(out)==24
    return out

def line_match(w):
    for j,v in enumerate(LINES):
        if w==v: return j,1
        if w==tuple(-x for x in v): return j,-1
    raise AssertionError(w)

def det3(cols):
    M=[[A[r][c] for c in cols] for r in range(3)]
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def lift(lp,ls):
    inv={line:i for i,line in enumerate(AX)}
    M=[[0]*6 for _ in range(6)]
    for i,line in enumerate(AX): M[inv[lp[line]]][i]=ls[line]
    return tuple(tuple(r) for r in M)

def main():
    for s,inds in SLICES.items():
        vs=[tuple(ORIENT[s][i]*x for x in LINES[i]) for i in inds]
        assert tuple(sum(v[r] for v in vs) for r in range(3))==(0,0,0)
        assert all(dot(v,v)==2 for v in vs)
        assert all(dot(vs[i],vs[j])==-1 for i in range(3) for j in range(i+1,3))
        assert frozenset(AX[i] for i in NATIVE[s])==frozenset(inds)
    assert all(len(set(SLICES[s])&set(SLICES[t]))==1 for s,t in itertools.combinations("ABCD",2))
    assert all(mv(A,k)==(0,0,0) for k in K)
    minors={abs(det3(c)) for c in itertools.combinations(range(6),3) if det3(c)}
    assert minors=={2}
    rays={w for v in W for w in (v,tuple(-x for x in v))}; assert len(rays)==12
    for x,y,z in itertools.product(range(-5,6),repeat=3):
        if (x+y+z)%2: continue
        a=(x+y-z)//2; b=(x+z-y)//2; c=(y+z-x)//2
        assert mv(A,(a,b,0,0,c,0))==(x,y,z)
    frames=list(itertools.permutations(range(6)))
    fa=[f for f in frames if frozenset(f[i] for i in NATIVE["A"])==frozenset(SLICES["A"])]
    fab=[f for f in fa if frozenset(f[i] for i in NATIVE["B"])==frozenset(SLICES["B"])]
    assert (len(frames),len(fa),len(fab))==(720,36,4)
    ss={s:frozenset(v) for s,v in SLICES.items()}; acts=[]
    for R in rotations():
        m=[line_match(mv(R,v)) for v in LINES]; lp=tuple(x[0] for x in m); ls=tuple(x[1] for x in m); sm={}; tau={}
        for s,inds in SLICES.items():
            t=[u for u,z in ss.items() if z==frozenset(lp[i] for i in inds)][0]; sm[s]=t
            vals={ORIENT[s][i]*ls[i]*ORIENT[t][lp[i]] for i in inds}; assert len(vals)==1; tau[s]=vals.pop()
        acts.append((R,lp,ls,sm,tau))
    byR={a[0]:a for a in acts}
    assert len({a[1] for a in acts})==24
    assert len({tuple(a[3][s] for s in "ABCD") for a in acts})==24
    assert [sum(a[1][i]==i for a in acts) for i in range(6)]==[4]*6
    assert {s:sum(a[3][s]==s for a in acts) for s in "ABCD"}=={s:6 for s in "ABCD"}
    assert {e:sum(a[4][s]==e for a in acts for s in "ABCD") for e in (-1,1)}=={-1:48,1:48}
    lifts={a[0]:lift(a[1],a[2]) for a in acts}
    for a1 in acts:
        assert mm(A,lifts[a1[0]])==mm(a1[0],A)
        for a2 in acts:
            R12=mm(a2[0],a1[0]); a12=byR[R12]
            assert mm(lifts[a2[0]],lifts[a1[0]])==lifts[R12]
            for s in "ABCD": assert a12[4][s]==a2[4][a1[3][s]]*a1[4][s]
    pts=set(HCP); missing=[(p,tuple(-x for x in p)) for p in HCP if tuple(-x for x in p) not in pts]
    assert len(missing)==6 and ((1,1,1),(-1,-1,-1)) in missing
    cert=Path(__file__).with_name("exact_certificate_20260905.json")
    data=json.loads(cert.read_text()); assert data["classification"]["mathematical_replication"]=="PASS"
    assert data["rotation"]["lift_composition_checks"]==576 and data["rotation"]["chart_cocycle_checks"]==2304
    print("PASS: P000 FCC frame-conditioned atlas replication; unframed bridge remains an S6 torsor/groupoid.")

if __name__=="__main__": main()
