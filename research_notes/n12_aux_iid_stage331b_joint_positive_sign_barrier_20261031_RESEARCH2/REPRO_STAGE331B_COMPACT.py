#!/usr/bin/env python3
"""Independent compact Stage331-B verifier: exact integer interval cover + rational witnesses."""
from collections import Counter
from fractions import Fraction as F
from functools import lru_cache
from hashlib import sha256
import json
D=1<<22; D3=D**3; M=(61,21,9,9); W=(1,3,3,1); T=F(1831,200000)
@lru_cache(None)
def ext(a,b):
    p=lambda n:[27*n**k*(D-n)**(3-k) for k in range(4)]
    aa,bb=p(a),p(b)
    lo=[min(aa[k],bb[k]) for k in range(4)]
    hi=[max(aa[k],bb[k]) for k in range(4)]
    if 3*a<=D<=3*b:hi[1]=max(hi[1],4*D3)
    if 3*a<=2*D<=3*b:hi[2]=max(hi[2],4*D3)
    return lo,hi

def bounds(a,b,c,d):
    l,h=ext(a,b);j,k=ext(c,d)
    return ([32*(4*l[t]+j[t])-27*M[t]*D3 for t in range(4)],
            [32*(4*h[t]+k[t])-27*M[t]*D3 for t in range(4)])

def kind(a,b,c,d):
    lo,hi=bounds(a,b,c,d)
    if hi[1]<0:return 'r1<0'
    if hi[3]<0:return 'r3<0'
    A=sum(W[t]*(lo[t] if lo[t]>0 else -hi[t] if hi[t]<0 else 0) for t in range(4))
    if A*T.denominator>T.numerator*1024*27*D3:return 'b>T'
    return None

def split(a,b,c,d,depth,leaves):
    label=kind(a,b,c,d)
    if label:
        leaves.append((label,a,b,c,d,depth));return
    if b-a==d-c==1:raise AssertionError('resolution insufficient')
    if b-a>1 and (d-c==1 or 4*(b-a)>=d-c):
        m=(a+b)//2
        split(a,m,c,d,depth+1,leaves);split(m,b,c,d,depth+1,leaves)
    else:
        m=(c+d)//2
        split(a,b,c,m,depth+1,leaves);split(a,b,m,d,depth+1,leaves)

def B(k,z):return z**k*(1-z)**(3-k)
def r(x,y):return tuple((4*B(k,x)+B(k,y))/5-F(M[k],160) for k in range(4))
def cost(x,y):return F(5,32)*sum(W[k]*abs(v) for k,v in enumerate(r(x,y)))
def main():
    leaves=[];split(0,D,0,D,0,leaves)
    assert len(leaves)==97 and max(e[-1] for e in leaves)==41
    assert Counter(e[0] for e in leaves)=={'r1<0':43,'r3<0':31,'b>T':23}
    assert all(kind(*e[1:5])==e[0] for e in leaves)
    assert all(0<=e[1]<e[2]<=D and 0<=e[3]<e[4]<=D for e in leaves)
    assert sum((e[2]-e[1])*(e[4]-e[3]) for e in leaves)==D*D
    manifest=json.dumps(leaves,separators=(',',':'))
    print('D=',D,'LEAVES=',len(leaves),'MAX_DEPTH=',max(e[5] for e in leaves))
    print('COUNTS=',dict(sorted(Counter(e[0] for e in leaves).items())))
    print('COVER_AREA=',sum((e[2]-e[1])*(e[4]-e[3]) for e in leaves))
    print('MANIFEST_SHA256=',sha256(manifest.encode()).hexdigest())
    examples={'---':(F(23,100),F(3,5)),'--+':(F(23,100),F(31,50)),
              '-+-':(F(47,200),F(53,100)),'+--':(F(9,40),F(3,5)),
              '+-+':(F(9,40),F(5,8)),'++-':(F(23,100),F(13,25))}
    for pattern,(x,y) in sorted(examples.items()):
        R=r(x,y)
        assert ''.join('+' if R[k]>0 else '-' if R[k]<0 else '0' for k in (0,1,3))==pattern
        assert R[2]>0 and sum(W[k]*R[k] for k in range(4))==0
        assert cost(x,y)-F(23860079,6400000000)<F(2181407226,10**12)
        print('SIGN',pattern,'x=',x,'y=',y,'b=',cost(x,y))
    x,y=F(248529,10**6),F(603541,10**6)
    assert r(x,y)[1]>0 and r(x,y)[3]>0
    assert T<cost(x,y)<F(9155372,10**9)
    print('POSITIVE_PAIR_WITNESS',x,y,'b=',cost(x,y))
    print('STAGE331B_GLOBAL_JOINT_SIGN_EXCLUSION_AND_SIX_CHAMBERS_EXACT_PASS')
if __name__=='__main__':main()
