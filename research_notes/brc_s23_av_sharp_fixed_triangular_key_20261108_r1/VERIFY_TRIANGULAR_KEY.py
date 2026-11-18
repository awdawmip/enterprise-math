#!/usr/bin/env python3
"""Exact finite integer checks for triangular cut-and-project keys.

Proof remains in PROOF.md; no floating point is used in any assertions.
"""
from math import gcd
from random import Random

Q=10**26
LO=545569623581288298975349314
HI=LO+1
P=2074774
D=380295
N=P+D
W=(79,431)
W_NEG=(W[0]-D,W[1]-P)

def divceil(a,b):
    return -((-a)//b)

def FS(n,m,a,b):
    """Sum floor((a*i+b)/m) for i=0..n-1, m>0, arbitrary integer b."""
    assert n>=0 and m>0
    qa,a=divmod(a,m)
    qb,b=divmod(b,m)
    s=qa*n*(n-1)//2+qb*n
    while True:
        if a>=m:
            s+=n*(n-1)//2*(a//m)
            a%=m
        if b>=m:
            s+=n*(b//m)
            b%=m
        y=a*n+b
        if y<m:
            return s
        n=y//m
        b=y%m
        m,a=a,m

def clip(x,low,high):
    return min(high,max(low,x))

def count_below(H,m):
    """#{(v,j) in triangle: P*v-D*j < m}."""
    A=clip(divceil(m,P),0,H+1)
    B=clip(divceil(D*H+m,P+D),0,H+1)
    l=B-A
    assert l>=0,(H,m,A,B)
    return A*(H+1)-A*(A-1)//2+l*H-l*(A+B-1)//2-FS(l,D,P,P*A-m)

def select_key(H,rank):
    M=(H+1)*(H+2)//2
    assert 0<=rank<M
    low=-D*H
    high=P*H+1
    while low<high:
        mid=(low+high)//2
        if count_below(H,mid)>rank:
            high=mid
        else:
            low=mid+1
    key=low-1
    assert count_below(H,key)==rank
    assert count_below(H,key+1)==rank+1
    return key

def decode_key(H,key):
    """Unique nonnegative lift of v mod D, if it exists in triangle H<N."""
    assert 0<=H<N
    v0=(key*pow(P,-1,D))%D
    j0=(P*v0-key)//D
    t=max(0,divceil(-j0,P))
    v=v0+D*t
    j=j0+P*t
    assert v>=0 and j>=0 and v+j<=H,(H,key,v,j,t)
    assert P*v-D*j==key
    return v,j,t

def all_triangular_pairs(H):
    return [(v,j) for v in range(H+1) for j in range(H-v+1)]

def A(h):
    return (h+1)*(h+2)//2 if h>=0 else 0

def verify():
    assert gcd(P,D)==1
    assert P*W[0]-D*W[1]==1
    assert P*W_NEG[0]-D*W_NEG[1]==1
    err=max(abs(LO*D-P*Q),abs(HI*D-P*Q))
    assert D*err<Q, (D*err,Q)
    assert LO*D>(P-1)*Q
    print('EXACT_BOUND_CERT: gcd=1; D*max(|LO*D-PQ|,|HI*D-PQ|)<Q; (LO/Q)*D>P-1')
    print('MAX_TRIANGULAR_KEY_H',N-1)
    for H in range(1,91):
        pts=all_triangular_pairs(H)
        ordered=sorted(pts,key=lambda z:P*z[0]-D*z[1])
        M=len(pts)
        all_keys=[P*v-D*j for v,j in ordered]
        assert len(set(all_keys))==M
        for rank,(v,j) in enumerate(ordered):
            key=P*v-D*j
            assert count_below(H,key)==rank,(H,rank)
            assert select_key(H,rank)==key,(H,rank)
            assert decode_key(H,key)[:2]==(v,j)
        # exact zero-and-one integer key gap displacements and totals
        count1=0
        for (v,j),(vv,jj) in zip(ordered,ordered[1:]):
            if P*(vv-v)-D*(jj-j)==1:
                assert (vv-v,jj-j) in (W,W_NEG)
                count1+=1
        assert count1==A(H-510)+A(H-(N-510)),(H,count1)
    print('SMALL_H_EXHAUSTIVE: H=1..90, all ranks/select/decode and gap-one class checks PASS')
    r=Random(240512)
    for H in [510,30000,D-1,D,D+1,500000,1000000,N-510,N-1]:
        total=(H+1)*(H+2)//2
        ranks={0,1,2,total//4,total//2,3*total//4,total-3,total-2,total-1}
        for _ in range(20):
            ranks.add(r.randrange(total))
        for rank in sorted(ranks):
            key=select_key(H,rank)
            v,j,t=decode_key(H,key)
            assert count_below(H,key)==rank
            assert P*v-D*j==key
        # check randomly chosen points beyond old D constraint, including noncanonical lifts
        for _ in range(30):
            v=r.randrange(H+1)
            j=r.randrange(H-v+1)
            key=P*v-D*j
            rank=count_below(H,key)
            assert select_key(H,rank)==key
            assert decode_key(H,key)[:2]==(v,j)
        expected=A(H-510)+A(H-(N-510))
        anchors=[(0,0),(max(0,H-510),0)]
        for av,aj in anchors:
            if av+aj+510<=H:
                a=P*av-D*aj
                b=P*(av+79)-D*(aj+431)
                assert b-a==1
                assert count_below(H,b)==count_below(H,a)+1
        if H>=N-510:
            # reverse-oriented unit-key gap pair at its birth
            neg_v,neg_j =D-79,P-431
            assert count_below(H,0)==count_below(H,P*neg_v-D*neg_j)+1
        print('LARGE_H_PASS',H,'points',total,'unit_key_gaps',expected)
    assert P*D-D*P==0
    assert N==2455069
    print('SHARP_COLLISION: at H=N, (0,0) and (D,P) are distinct equal-key points')
    print('PASS_S23_AV_TRIANGULAR_KEY_SHARP_HORIZON_AND_UNIT_GAP_CLASSES')

if __name__=='__main__':
    verify()
