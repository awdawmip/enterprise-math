"""R66 independent exact branch-preservation and subtree-bound regression, Python 3.10+."""
from dataclasses import dataclass
from fractions import Fraction as F
from math import floor
from bisect import bisect_right

def fr(x):return x-floor(x)
def cl(x):return -floor(-x)
@dataclass(frozen=True)
class N:
    k:tuple;prio:int;left:object;right:object;cnt:int;lo:F;hi:F;tlo:int;thi:int

def mk(k,p,l=None,r=None):
    a=[k[0]]+[l.lo] if l else [k[0]]
    if r:a.append(r.lo)
    b=[k[0]]+[l.hi] if l else [k[0]]
    if r:b.append(r.hi)
    t=[k[1]]+([l.tlo] if l else [])+([r.tlo] if r else [])
    u=[k[1]]+([l.thi] if l else [])+([r.thi] if r else [])
    return N(k,p,l,r,1+(l.cnt if l else 0)+(r.cnt if r else 0),min(a),max(b),min(t),max(u))

def cut(n,k):
    if not n:return None,None
    if n.k<k:
        a,b=cut(n.right,k);return mk(n.k,n.prio,n.left,a),b
    a,b=cut(n.left,k);return a,mk(n.k,n.prio,b,n.right)

def join(a,b):
    if not a:return b
    if not b:return a
    if a.prio>b.prio:return mk(a.k,a.prio,a.left,join(a.right,b))
    return mk(b.k,b.prio,join(a,b.left),b.right)

def add(n,k,p):
    if n is None:return mk(k,p)
    if k==n.k:raise ValueError('duplicate branch')
    if p>n.prio:
        a,b=cut(n,k);return mk(k,p,a,b)
    if k<n.k:return mk(n.k,n.prio,add(n.left,k,p),n.right)
    return mk(n.k,n.prio,n.left,add(n.right,k,p))

def remove(n,k):
    if not n:raise KeyError(k)
    if k==n.k:return join(n.left,n.right)
    if k<n.k:return mk(n.k,n.prio,remove(n.left,k),n.right)
    return mk(n.k,n.prio,n.left,remove(n.right,k))

def excluded(n,anchor,L,U,j,x,z,nxt):
    ds=(L-anchor,U-anchor)
    shifts=[t*d for t in (n.tlo,n.thi) for d in ds]
    a0=fr((j+z)*anchor-x);c0=fr((j+nxt)*anchor-x)
    if c0<=a0:c0+=1
    aa=[a0+(j+z)*d for d in ds];cc=[c0+(j+nxt)*d for d in ds]
    if any(not 0<c-a<1 for a,c in zip(aa,cc)):return False
    return cl(n.lo+min(shifts)-max(cc))>floor(n.hi+max(shifts)-min(aa))

def label(th,m,j,x,t):
    a=sorted((fr(z*th),z) for z in range(m))
    return a[bisect_right([p for p,z in a],fr(x+(t-j)*th))-1][1]

def run():
    a=F(1,30);L=a;U=F(1003,30000)
    # Persistent same-time sibling: deleting one branch cannot delete the other.
    tree=None;key=lambda t,b:(fr(t*a),t,b)
    tree=add(tree,key(70,1),93);both=add(tree,key(70,2),81)
    one=remove(both,key(70,1))
    assert both.cnt==2 and one.cnt==1 and tree.cnt==1
    # R65 exact certified internal reordering: 390 phase moves past 1.
    x=F(13,15);j=500;m=13;z=12
    hist=sorted((fr(v*a),v) for v in range(m));lab=[v for p,v in hist]
    nxt=lab[(lab.index(z)+1)%m]
    pair=add(add(None,key(1,0),90),key(390,0),50)
    assert fr(390*a)<fr(1*a) and fr(390*U)>fr(1*U)
    assert excluded(pair,a,L,U,j,x,z,nxt)
    for th in [L,(L+U)/2,U]:
        assert label(th,m,j,x,1)!=z and label(th,m,j,x,390)!=z
    # R64 stale-index warning: old winner is not stable across this interval.
    j=10000;x=F(8,15);z=12
    times=(9,15,6042)
    vals=[max((t for t in times if label(th,13,j,x,t)==z),default=None) for th in (L,U)]
    assert vals==[6042,15]
    print('R66_MIN_PASS branch_versions=3 subtree_swap=1 exact_winner_change=1')
if __name__=='__main__':run()
