#!/usr/bin/env python3
"""Stage308-B reproducible exact rational positive-branch observer calculations.
No P000 native X6 dynamics or native research/admission authority is claimed.
"""
from fractions import Fraction as Q
from math import comb

p0,p1=Q(1,4),Q(3,4)
weights={
    (0,0,0):(63,1), (0,0,1):(21,3), (0,1,0):(21,3), (0,1,1):(7,9),
    (1,0,0):(9,7), (1,0,1):(3,21), (1,1,0):(3,21), (1,1,1):(1,63),
}
def b(k,t): return t**k*(1-t)**(3-k)
def A(t): return 1-3*t*t+2*t**3
def f(t): return -Q(9,128)*t-Q(3,32)*t*t+Q(1,8)*t**3
def g(t): return Q(117,4096)*t-Q(123,1024)*t*t+Q(23,256)*t**3

def rate_table(u=Q(0),v=Q(0)):
    r={h:(p0 if a>bb else p1) for h,(a,bb) in weights.items()}
    r[(1,0,0)]=p0+u
    r[(0,1,1)]=p1-v
    return r

def score(table):
    public=joint=Q(0)
    for w in range(2):
        for y in range(2):
            for k in range(4):
                ideal=sum((a*b(k,p0)+bb*b(k,p1) for (j,ww,yy),(a,bb) in weights.items() if (ww,yy)==(w,y)),Q(0))/256
                compressed=sum(((a+bb)*b(k,table[(j,w,y)]) for (j,ww,yy),(a,bb) in weights.items() if (ww,yy)==(w,y)),Q(0))/256
                public+=Q(comb(3,k),2)*abs(ideal-compressed)
    for h,(a,bb) in weights.items():
        for k in range(4):
            joint+=Q(comb(3,k),512)*(a*abs(b(k,p0)-b(k,table[h]))+bb*abs(b(k,p1)-b(k,table[h])))
    return public,joint

def main():
    assert len(weights)==8 and sum(a for a,_ in weights.values())==128
    assert sum(bb for _,bb in weights.values())==128
    assert all(a>0 and bb>0 for a,bb in weights.values())
    P0,T0=score(rate_table());assert (P0,T0)==(Q(11,256),Q(77,1024))
    # Exact analytic signs on the whole [1/4,27/100] interval:
    # b0 strictly decreases; b1,b2,b3 strictly increase there.
    # The public residual at g=00 equals 16*b_k(1/4+u)-8*(b_k(1/4)+b_k(3/4)).
    r=lambda k,u:16*b(k,p0+u)-8*b(k,p0)-8*b(k,p1)
    assert r(0,Q(1,50))>0 and r(1,Q(0))>0
    assert r(2,Q(1,50))<0 and r(3,Q(1,50))<0
    assert p0+Q(1,50)<Q(1,3)
    # Matching source TV sign regions near p0 and p1.
    assert b(1,p0)>b(1,p1) and b(2,p0)<b(2,p1)
    assert all(b(k,p0+Q(1,50))>b(k,p1) for k in (0,1))
    assert all(b(k,p0+Q(1,50))<b(k,p1) for k in (2,3))
    for i in range(21):
        u=Q(i,1000)
        # Exact values independently accumulated over all S/J/G branches.
        P,T=score(rate_table(u,Q(0)))
        assert P-P0==f(u)
        assert T-T0==g(u)
        assert f(u)==(A(p0+u)-A(p0))/16
        assert g(u)==(9*(Q(27,64)-(Q(3,4)-u)**3)+7*(A(p0+u)-A(p0)))/256
    for i in range(11):
        for j in range(11-i):
            u,v=Q(i,1000),Q(j,1000)
            P,T=score(rate_table(u,v))
            assert (P,T)==(P0+f(u)+f(v),T0+g(u)+g(v))
            assert f(u)+f(v)-f(u+v)==Q(3,16)*u*v*(1-2*(u+v))
            assert g(u)+g(v)-g(u+v)==u*v*(123-138*(u+v))/512
    h=Q(1,100)
    split=score(rate_table(h,h));concentrated=score(rate_table(2*h,Q(0)))
    assert split==(Q(5193,125000),Q(9695073,128000000))
    assert concentrated==(Q(20763,500000),Q(9692067,128000000))
    assert (split[0]-concentrated[0],split[1]-concentrated[1])==(Q(9,500000),Q(1503,64000000))
    # Exact analytic curvature and monotonicity bounds for u in [0,1/50].
    assert Q(-3,16)+Q(3,4)*Q(1,50)<0  # f''(u)
    assert (Q(-123)+276*Q(1,50))/512<0 # g''(u)
    assert Q(117,4096)-Q(246,1024)*Q(1,50)>0 # g'(u) lower bound (omit positive square)
    assert Q(9,128)==-Q(-9,128) and Q(117,4096)/(Q(9,128))==Q(13,32)
    # Positive toward/away first-order joint slopes over all 8 branch pairs.
    toward={(j,w,y):Q(27*max(a,bb)-18*min(a,bb),4096) for (j,w,y),(a,bb) in weights.items()}
    away={(j,w,y):Q(27*max(a,bb)+18*min(a,bb),4096) for (j,w,y),(a,bb) in weights.items()}
    assert min(toward.values())==Q(117,4096)
    assert min(away.values())>min(toward.values())
    assert {h for h,c in toward.items() if c==Q(117,4096)}=={(1,0,0),(0,1,1)}
    assert toward[(0,0,0)]==toward[(1,1,1)]==Q(1683,4096)
    # Two minority fibers achieve sharp local supporting slope; majority fibers do not.
    assert toward[(1,0,0)]==Q(13,32)*Q(9,128)
    assert toward[(0,1,1)]==Q(13,32)*Q(9,128)
    assert toward[(0,0,0)]>Q(13,32)*Q(9,32)
    assert toward[(1,1,1)]>Q(13,32)*Q(9,32)
    print('BASELINE_PUBLIC_JOINT',str(P0),str(T0))
    print('SPLIT_U_V',str(h),str(h),'PUBLIC',str(split[0]),'JOINT',str(split[1]))
    print('CONCENTRATED',str(2*h),'PUBLIC',str(concentrated[0]),'JOINT',str(concentrated[1]))
    print('STRICT_PUBLIC_GAIN',str(split[0]-concentrated[0]))
    print('STRICT_JOINT_GAIN',str(split[1]-concentrated[1]))
    print('FULL_EIGHT_RATE_JOINT_ENDPOINT_TANGENT',str(Q(13,32)))
    print('STAGE308B_SHARP_ENDPOINT_AND_SYMMETRY_BREAKING_EXACT_PASS')

if __name__=='__main__': main()
