"""R53 reproducible exact indexed-node treap for labelled phase-cut events."""
from bisect import bisect_right
from heapq import nlargest
from math import isqrt
import random
S23=(262204504569236716045286,262204504569236716045287,10**24)
D=10**30
q=isqrt(2*D*D)
assert q*q<2*D*D<(q+1)*(q+1)
QUAD=(q-D,q+1-D,D)

class AgeTrees:
    def __init__(self,m,H,owner):
        self.m,self.H=m,H
        rng=random.Random(53011)
        self.pr=[0]+[rng.getrandbits(128) for r in range(H)]
        self.l=[0]*(H+1);self.r=[0]*(H+1)
        self.roots=[0]*m;self.owner=owner[:]
        for age in range(1,H+1):
            z=owner[age];self.roots[z]=self.ins(self.roots[z],age)
    def rotR(self,x):
        y=self.l[x];self.l[x]=self.r[y];self.r[y]=x;return y
    def rotL(self,x):
        y=self.r[x];self.r[x]=self.l[y];self.l[y]=x;return y
    def ins(self,x,a):
        if not x:return a
        if a<x:
            self.l[x]=self.ins(self.l[x],a)
            if self.pr[self.l[x]]<self.pr[x]:x=self.rotR(x)
        elif a>x:
            self.r[x]=self.ins(self.r[x],a)
            if self.pr[self.r[x]]<self.pr[x]:x=self.rotL(x)
        else:raise AssertionError("duplicate")
        return x
    def merge(self,a,b):
        if not a:return b
        if not b:return a
        if self.pr[a]<self.pr[b]:
            self.r[a]=self.merge(self.r[a],b);return a
        self.l[b]=self.merge(a,self.l[b]);return b
    def erase(self,x,a):
        assert x
        if x==a:
            w=self.merge(self.l[x],self.r[x]);self.l[x]=self.r[x]=0;return w
        if a<x:self.l[x]=self.erase(self.l[x],a)
        else:self.r[x]=self.erase(self.r[x],a)
        return x
    def move(self,a,old,new):
        assert self.owner[a]==old and old!=new
        self.roots[old]=self.erase(self.roots[old],a)
        self.roots[new]=self.ins(self.roots[new],a)
        self.owner[a]=new
    def ages(self):
        out=[]
        for x in self.roots:
            if not x:out.append(None);continue
            while self.l[x]:x=self.l[x]
            out.append(x)
        return tuple(out)
    def audit(self):
        seen=set()
        def walk(x,z,lo,hi):
            if not x:return
            assert lo<x<hi and x not in seen and self.owner[x]==z
            seen.add(x)
            if self.l[x]:assert self.pr[x]<=self.pr[self.l[x]]
            if self.r[x]:assert self.pr[x]<=self.pr[self.r[x]]
            walk(self.l[x],z,lo,x)
            walk(self.r[x],z,x,hi)
        for z,rt in enumerate(self.roots):walk(rt,z,0,self.H+1)
        assert len(seen)==self.H
def exercise(name,m,H,enc,depth=None):
    L,U,D=enc;K=m+H-1;B=L+U;Q=2*D
    phase_L=sorted(range(1,K+1),key=lambda s:(s*L)%D,reverse=True)
    phase_U=sorted(range(1,K+1),key=lambda s:(s*U)%D,reverse=True)
    assert phase_L==phase_U
    if depth is None:depth=K
    if depth==K:cuts=sorted(range(1,K+1),key=lambda s:(s*B)%Q,reverse=True)
    else:cuts=nlargest(depth,range(1,K+1),key=lambda s:(s*B)%Q)
    assert cuts==phase_L[:depth]
    hist=sorted(((z*B)%Q,z) for z in range(m))
    pred={z:hist[i-1][1] for i,(_,z) in enumerate(hist)}
    def reconstruct(s,t,mod):
        hs=sorted(((z*t)%mod,z) for z in range(m))
        pts=[p for p,_ in hs]
        return [-1]+[hs[bisect_right(pts,((s-r)*t)%mod)-1][1] for r in range(1,H+1)]
    owners=[reconstruct(s,L,D) for s in cuts]
    for j,s in enumerate(cuts):
        assert owners[j]==reconstruct(s,U,D)==reconstruct(s,B,Q)
    t=AgeTrees(m,H,owners[0]);t.audit()
    old=t.ages();moves=changes=0
    for j in range(1,len(cuts)):
        s=cuts[j-1]
        for z in range(max(0,s-H),min(m-1,s-1)+1):
            age=s-z;t.move(age,z,pred[z]);moves+=1
        assert t.owner==owners[j]
        t.audit()
        direct=[None]*m
        for r in range(1,H+1):
            z=t.owner[r]
            if direct[z] is None:direct[z]=r
        new=t.ages()
        assert new==tuple(direct)
        changes+=new!=old;old=new
    if depth==K:
        last=cuts[-1]
        assert moves+sum(1 for z in range(m) if 1<=last-z<=H)==m*H
    print("PASS_R53_COMPACT",name,"cells",len(cuts),"moves",moves,
          "changed",changes,"live_nodes",H,"top",cuts[:5])
    return len(cuts),moves

if __name__=="__main__":
    runs=[exercise("S23_full",128,225,S23),
          exercise("sqrt2_5_8",5,8,QUAD),
          exercise("sqrt2_8_17",8,17,QUAD),
          exercise("sqrt2_16_25",16,25,QUAD),
          exercise("sqrt2_23_31",23,31,QUAD),
          exercise("sqrt2_8_99993",8,99993,QUAD,5)]
    assert tuple(sum(v[i] for v in runs) for i in range(2))==(486,29945)
    assert nlargest(7,range(1,13),key=lambda s:(s*(QUAD[0]+QUAD[1]))%(2*QUAD[2]))==[12,7,2,9,4,11,6]
    print("PASS_R53_COMPACT_6_CASES")
