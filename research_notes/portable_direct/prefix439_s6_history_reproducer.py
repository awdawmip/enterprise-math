"""PREFIX-439 exact six-axis typed BRC auxiliary reproducer. Python stdlib only."""
from itertools import permutations,product
from pathlib import Path
import sys
root=Path(__file__).resolve()
for candidate in [root.parent,*root.parents]:
    src=candidate/"experiments/x6_signed_native_spatial_v16_20260905"
    if (src/"signed_brc.py").is_file():
        sys.path.insert(0,str(src))
        break
else:
    raise RuntimeError("run from repository checkout with original signed_brc.py")
from signed_brc import shortest_path_multiplicity,return_multiplicity
assert shortest_path_multiplicity((2,2,0,0,0,0))==6
assert return_multiplicity(12)>0
axes=range(6)
def parity(x):return tuple(a&1 for a in x)
def perm(x,pi):
    y=[0]*6
    for i in axes:y[pi[i]]=x[i]
    return tuple(y)
def inv_gauge(pi,p):
    return sum(p[i]*p[j] for i in axes for j in range(i+1,6) if pi[i]>pi[j])&1
def cross(p,q):
    return sum(p[i]*q[j] for i in axes for j in range(i+1,6))&1
def unit():return ((0,)*6,0,0,(0,)*6)
def step(j,sg):
    x=[0]*6;r=[0]*6;x[j]=sg;r[j]=int(sg<0)
    return tuple(x),1,0,tuple(r)
def then(a,b):
    x,n,t,r=a;y,m,u,s=b
    return (tuple(x[i]+y[i] for i in axes),n+m,t^u^cross(parity(x),parity(y)),tuple(r[i]^s[i] for i in axes))
def rotate(a,pi):
    x,n,t,r=a
    return perm(x,pi),n,t^inv_gauge(pi,parity(x)),perm(r,pi)
def word(w):
    a=unit()
    for j,sg in w:a=then(a,step(j,sg))
    return a
def packed(a):
    p=parity(a[0]);t=a[2];r=a[3]
    return sum(p[i]<<i for i in range(5))|(t<<5)|sum(r[i]<<(i+6) for i in range(5))
def update(c,a):
    p=c&31;t=(c>>5)&1;r=(c>>6)&31
    dx=parity(a[0]);phase=a[2];hist=a[3]
    extra=sum(((p>>i)&1)*dx[j] for i in range(5) for j in range(i+1,6))&1
    return (p^sum(dx[i]<<i for i in range(5)))|((t^phase^extra)<<5)|((r^sum(hist[i]<<i for i in range(5)))<<6)
def recover(c,x,n):
    assert n>=sum(x) and (n-sum(x))%2==0
    r=tuple((c>>(i+6))&1 for i in range(5))
    return parity(x),((c>>5)&1),r+((((n-sum(x))//2)&1)^(sum(r)&1),)
G=[step(j,sg) for j in axes for sg in (1,-1)]
for a in G:
    for b in G:
        for c in G:assert then(then(a,b),c)==then(a,then(b,c))
print("PASS 1728 associative generator triples")
S6=list(permutations(axes))
for pi in S6:
    for m in range(64):
        p=tuple((m>>j)&1 for j in axes)
        for j in axes:
            for sg in (1,-1):
                a=(p,0,0,(0,)*6)
                assert rotate(then(a,step(j,sg)),pi)==then(rotate(a,pi),step(pi[j],sg))
print("PASS 552960 S6 gauge / step squares")
for c in range(2048):
    for a in G:
        for b in G:assert update(update(c,a),b)==update(c,then(a,b))
print("PASS 294912 two-step BRC indexed-control compositions")
fiber=set()
for r in product((0,1),repeat=6):
    if sum(r)%2:continue
    k=list(r)
    if sum(r)==0:k[0],k[1]=4,2
    else:k[0]+=(6-sum(r))
    assert sum(k)==6
    w=[(j,sg) for j in axes for _ in range(k[j]) for sg in (1,-1)]
    a=word(w)
    assert a[0]==(0,)*6 and a[1]==12 and a[2]==0 and a[3]==r
    i,j=[v for v in axes if k[v]>0][:2]
    k[i]-=1;k[j]-=1
    other=[(i,1),(j,1),(i,-1),(j,-1)]+[(v,sg) for v in axes for _ in range(k[v]) for sg in (1,-1)]
    b=word(other)
    assert b[0]==a[0] and b[1]==a[1] and b[3]==a[3] and b[2]==1
    fiber.add((a[2],a[3]));fiber.add((b[2],b[3]))
assert len(fiber)==64
print("PASS 64 exact same-effect history Port fibers")
a=word([]);b=word([(5,1)]);pi=(5,1,2,3,4,0)
assert (packed(a)&63)==(packed(b)&63)
assert (packed(rotate(a,pi))&63)!=(packed(rotate(b,pi))&63)
a=word([(1,1),(1,-1)]);b=word([(2,1),(2,-1)])
assert (a[0],a[1],a[2],a[3][0])==(b[0],b[1],b[2],b[3][0])
pi=(1,0,2,3,4,5)
assert rotate(a,pi)[3][0]!=rotate(b,pi)[3][0]
print("PASS two exact standalone information-loss witnesses")
for pi in S6:
    for z in range(64):
        x=tuple((z>>j)&1 for j in axes)
        for m in (0,1,3,31,42,63):
            r=tuple((m>>j)&1 for j in axes)
            n=sum(x)+2*sum(r)
            for t in (0,1):
                a=(x,n,t,r);rot=rotate(a,pi)
                assert recover(packed(a),x,n)==(parity(x),t,r)
                assert recover(packed(rot),rot[0],n)==(parity(rot[0]),rot[2],rot[3])
print("PASS 552960 exact coupled S6 parity/history reconstructions")
print("PREFIX439_REPRODUCER_PASS; original upstream ControlPacket class not imported")