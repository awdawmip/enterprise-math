#!/usr/bin/env python3
"""C267: self-contained exact rational proof of full (0,16) auxiliary hull.
Requires only Python standard library. No finite sampling is used for the proof.
Evidence class: author exact, not independent Driver-admitted, not native BRC.
"""
from fractions import Fraction as F
NUM=(0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 2, 1, 3, 3, 1, 6, 2, 3, 6, 1, 6, 3, 2, 7, 3, 4, 8, 1, 21, 9, 6, 4, 10, 14, 5, 11, 2, 9, 12, 13, 14, 3, 7, 15, 17, 14, 5, 6, 13, 15, 17, 10, 11, 13, 16, 18, 22, 28, 36, 46, 63, 96, 152, 246, 528, 1971, 1)
DEN=(1, 2057, 539, 289, 136, 93, 68, 51, 39, 31, 27, 21, 17, 15, 13, 11, 10, 9, 8, 7, 13, 6, 11, 5, 14, 13, 4, 23, 7, 10, 19, 3, 17, 8, 5, 17, 7, 9, 17, 2, 41, 17, 11, 7, 17, 23, 8, 17, 3, 13, 17, 18, 19, 4, 9, 19, 21, 17, 6, 7, 15, 17, 19, 11, 12, 14, 17, 19, 23, 29, 37, 47, 64, 97, 153, 247, 529, 1972, 1)
U=tuple(F(a,b) for a,b in zip(NUM,DEN))
I=(5,50,55,56);J=tuple(j for j in range(79) if j not in I)
Z=F(141421356237309504880,10**20)
Q=2**128;H=2**166;A=F(6912*50000**2,17**2)
assert len(U)==79 and all(U[j]<U[j+1] for j in range(78))
B={}
for j in J:
    v=F(Q)*A/H/((2-U[j]**2)*(3-U[j]**2))**3
    for p in range(79):
        if p!=j:v*=(Z-U[p])/abs(U[j]-U[p])
    B[j]=v.numerator//v.denominator
    assert B[j]>0

def fac(j,p,t):
    return (Z-t)/(Z-U[p])*abs(U[j]-U[p])/abs(U[j]-t)

def affine(j,p,lo,hi):
    s=(lo+hi)/2
    val=fac(j,p,s)
    slope=val*(-1/(Z-s)-1/(s-U[j]))
    x=val+slope*(lo-s);y=val+slope*(hi-s)
    if x>=0 and y>=0:return x,y
    e=lo if j>p else hi
    return fac(j,p,e),fac(j,p,e)

def mov(k,lo,hi):
    d=I.index(k);t=(lo[d]+hi[d])/2
    val=F(Q)*A/H/((2-t*t)*(3-t*t))**3
    slope=6*t/(2-t*t)+6*t/(3-t*t)
    for j in J:
        val*=(Z-U[j])/abs(t-U[j]);slope-=1/(t-U[j])
    for p in I:
        if p==k:continue
        dd=I.index(p);e=lo[dd] if p<k else hi[dd]
        val*=(Z-e)/abs(t-e);slope-=1/(t-e)
    e=lo[d] if slope>=0 else hi[d]
    return max(F(0),val*(1+slope*(e-t)))

def bound(lo,hi,axes):
    f=[F(0) for _ in range(4)]
    for j in J:
        c=F(B[j])
        for d,p in enumerate(I):
            if d not in axes:
                e=lo[d] if j>p else hi[d]
                c*=fac(j,p,e)
        (x0,x1)=affine(j,I[axes[0]],lo[axes[0]],hi[axes[0]])
        (y0,y1)=affine(j,I[axes[1]],lo[axes[1]],hi[axes[1]])
        for n,t in enumerate((x0*y0,x0*y1,x1*y0,x1*y1)):f[n]+=c*t
    return min(f)+sum((mov(k,lo,hi) for k in I),F(0))

# Preorder tree: 0..3 split axes; a=(v50,v55),c=(v5,v55),e=(v55,v56).
TREE='323200111e00aa1e2ee003aa32aaa323aa301aa11a2aa2aa0a1aa2a30aaa1003aa31aaa312a30aaaa2a1aa1ee111e1e2e33aaa32302aaa0aa30101a2a3aa1a2a3aa02a3aa2a3aa112aa2a30aaa2a30aaa0012aa2aa12aa2aa12a1aa2aa23aa300a2aa2aa0aa13123aa3002aa2aa2aa0aa2aa21aa13aaa1ee0111e1e2ee323aa3011a2aa2aaa01aaa2a30aaa1312a30aaaa2a1aa1ee111e0aa03aaa103aaa1ee00111e00aa1e3aa003aa3aa33011a2aa2aa112aa223aa3aa3aa223aa3aa3aa01aa11a2aa2aa30a1aaa1003aa3aa3130a22aaa0aaa13aaa1ee111e1e330aaaa33010122aaa2230aaa30aaa32aaa122aaa2230aaa30a3aaa30aaa02230a2aaa30a2aaa320aaaa22302aa2aa0aa302aa2aa0aa302aa2aaa11223aa3aa3aa02232aaa33aaa32aaa223aa3aa3aa02232a0aaa302aa2aaa320aaaa2232aaa32aaa32aaa0011a22aaa22aaa11a22aaa22aaa110aa223aaaa223aa3aa3aa30011aaa11aaa11aa2aa0aa131300122aaaa122aaaa122aaaa00a1aa1aaa130aaaa1ee0111e1e3aa330112aa223aa3aa3aa223aa3aa3aa11aaa011a2aa2aaa301aaaa1313022aaaa0aaa1aa1ee111e0aa03aaa103aaa1ee0021011ea0aa11ea32aaa100aa32aaa1ee1011ea0aa11ea3aa100aa3aa1ee2111e3aa32aaa132aaa1ee111ea33aaa131aaae02111ea32aaa132aaa1ee111ea3aa13aae21011eaa11eaa10aae1011eaa1ea1ae32001011e0aa0a3aa11e1ee3320aaa2aaa100a3aa312aaaa1ee111e1e32aaa332001aa1aa11aaaa20aaa32aaa131230aaaaa1aa1ee0111e1ee3320aaa2aaa1312aaaa1ee1011eaa11eaa10aae001011eaa11eaa1ae111eaa1ae0111eaa1ae10aa1ae20010311eaaa311eaaa10aae1311caaa1ae01311eaaa1ae101aaa1ae0aa32200103aa3aa1ae13aa1ac013aa1aea0010aa1ae13aa1ac0aa2aa2aa'
AXES={'a':(1,2),'c':(0,2),'e':(2,3)}
LO=(F(4,543),F(43,62),F(18,23),F(13,16))
HI=(F(9,613),F(57,79),F(38,47),F(121,147))
for d,k in enumerate(I): assert U[k-1]<LO[d]<=HI[d]<U[k+1]
assert HI[2]<LO[3] and HI[3]<Z
cursor=[0];leaves=[0];splits=[0];minmargin=[10**100]
def walk(lo,hi):
    char=TREE[cursor[0]];cursor[0]+=1
    if char in AXES:
        f=bound(lo,hi,AXES[char]);m=f.numerator//f.denominator-Q
        assert m>0,(cursor[0],m)
        minmargin[0]=min(minmargin[0],m);leaves[0]+=1;return
    axis=int(char);s=(lo[axis]+hi[axis])/2
    assert lo[axis]<s<hi[axis]
    lh=list(hi);lh[axis]=s;rl=list(lo);rl[axis]=s
    splits[0]+=1
    walk(lo,tuple(lh));walk(tuple(rl),hi)
walk(LO,HI)
assert cursor[0]==len(TREE)==1343
assert (leaves[0],splits[0])==(672,671)
assert minmargin[0]==1625047347588520275838004208484642
print('C267_STANDALONE_EXACT_PASS',672,671,'margin',minmargin[0])
