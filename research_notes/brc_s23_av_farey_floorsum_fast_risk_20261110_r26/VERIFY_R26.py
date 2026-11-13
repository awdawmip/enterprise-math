#!/usr/bin/env python3
"""Exact Farey-bracket / floor-sum rank evaluator for irrational-circle prediction risk.
Uses no floats, no sorting of future phase points, no loops proportional to n.
"""
from fractions import Fraction
from bisect import bisect_right
import csv
from pathlib import Path

P=262204504569236716045286
Q=10**24
LO=Fraction(P,Q)
HI=Fraction(P+1,Q)
MID=(LO+HI)/2
M=128


def floor_sum_unsigned(n,m,a,b):
    assert n>=0 and m>0 and a>=0 and b>=0
    ans=0
    while True:
        if a>=m:
            ans+=n*(n-1)*(a//m)//2
            a%=m
        if b>=m:
            ans+=n*(b//m)
            b%=m
        z=a*n+b
        if z<m: return ans
        n=z//m
        b=z%m
        m,a=a,m


def floor_sum_range(left,right,alpha):
    assert 0<=left<=right
    return floor_sum_unsigned(right-left,alpha.denominator,alpha.numerator,alpha.numerator*left)


def floor_sum_shifted(left,right,shift,alpha):
    # signed b normalisation to nonnegative using exact integer division
    n=right-left
    if n==0:return 0
    mod=alpha.denominator
    a=alpha.numerator
    b=(left-shift)*a
    q,r=divmod(b,mod)
    return n*q+floor_sum_unsigned(n,mod,a,r)


def count_below(index,left,right,alpha):
    z=floor_sum_range(left,right,alpha)-floor_sum_shifted(left,right,index,alpha)
    return z-(right-left)*(index*alpha.numerator//alpha.denominator)


def count_arc(start,end,left,right,alpha):
    if right<=left:return 0
    x=count_below(end,left,right,alpha)-count_below(start,left,right,alpha)
    if (start*alpha.numerator)%alpha.denominator > (end*alpha.numerator)%alpha.denominator:
        x+=right-left
    assert 0<=x<=right-left,(start,end,left,right,x)
    return x


def farey_bracket(alpha,max_den):
    # Accelerated Stern-Brocot: left=a/b < alpha < c/d=right.
    p,q=alpha.numerator,alpha.denominator
    a,b,c,d=0,1,1,1
    jumps=0
    while b+d<=max_den:
        D=p*b-q*a
        E=q*c-p*d
        assert D>0 and E>0
        if D>E:
            k=min((D-1)//E,(max_den-b)//d)
            assert k>=1
            a+=k*c;b+=k*d
        else:
            k=min((E-1)//D,(max_den-d)//b)
            assert k>=1
            c+=k*a;d+=k*b
        jumps+=1
    assert c*b-a*d==1 and b+d>max_den
    assert Fraction(a,b)<alpha<Fraction(c,d)
    return a,b,c,d,jumps


def eval_risk(n,m=M):
    assert n>=max(2,m)
    a,i,c,j,jumps=farey_bracket(MID,n-1)
    assert Fraction(a,i)<LO and HI<Fraction(c,j), 'frozen theta interval crosses Farey boundary'
    assert i+j>=n
    assert i*c-j*a==1
    # u=i theta-a, v=c-j theta, w=u+v
    fam=[(-a,i),(c,-j),(c-a,i-j)]
    intervals=[(0,n-i,0),(j,n,1),(n-i,j,2)]
    assert all(L<=R for L,R,_ in intervals)
    order=sorted(range(m),key=lambda t: (t*MID.numerator)%MID.denominator)
    coeff0=0;coeff1=0
    chosen=[]
    sums=[0,0,0]
    for h,t in enumerate(order):
        e=order[(h+1)%m]
        counts=[count_arc(t,e,l,r,MID) for l,r,_ in intervals]
        # Total number of start phase points in that historical arc
        assert sum(counts)>=1
        for k,z in enumerate(counts):sums[k]+=z
        candidates=[k for k,z in enumerate(counts) if z]
        # Exact extrema agree at both endpoints => globally valid linear expression.
        kmax_lo=max(candidates,key=lambda k: fam[k][0]+fam[k][1]*LO)
        kmax_hi=max(candidates,key=lambda k: fam[k][0]+fam[k][1]*HI)
        assert fam[kmax_lo]==fam[kmax_hi],(n,t,e,kmax_lo,kmax_hi)
        A,B=fam[kmax_lo]
        coeff0-=A;coeff1-=B
        chosen.append((t,e,tuple(counts),kmax_lo))
    coeff0+=1
    assert sum(sums)==n
    risk_lo=coeff0+coeff1*LO
    risk_hi=coeff0+coeff1*HI
    assert 0<=risk_lo<=1 and 0<=risk_hi<=1
    return (coeff0,coeff1),(a,i,c,j),jumps,chosen,sums


def direct_risk(n,m=M):
    # Independent O(n log n) circular phase sorting and subarc maxima.
    pos=sorted(range(n), key=lambda t:(t*MID.numerator)%MID.denominator)
    historic=[False]*n
    for i in range(m):historic[i]=True
    hstart=next(k for k,t in enumerate(pos) if historic[t])
    maxima=[]; mx=Fraction(0)
    for shift in range(n):
        u=pos[(hstart+shift)%n]
        v=pos[(hstart+shift+1)%n]
        gap=((v*MID)%1-(u*MID)%1)%1
        if gap>mx:mx=gap
        if historic[v]:
            maxima.append(mx); mx=Fraction(0)
    assert len(maxima)==m
    return 1-sum(maxima)


def run():
    cases=[128,129,225,226,292,328,329,456,492,493,717,1106,1107,1173,1174,15000,25175,25176,25340,39473,39474,168155,168156,168319,168320,200000,322176,322177,322340,323000]
    prev={}
    with open('/mnt/data/em_r26/CERTIFICATE_R26.tsv','w',newline='') as f:
        w=csv.writer(f,delimiter='\t')
        w.writerow(['n','risk_A','risk_B','farey_lower_num','i','farey_upper_num','j','sb_jumps','count_u','count_v','count_w','direct_checked'])
        for n in cases:
            (A,B),(a,i,c,j),jumps,chosen,sums=eval_risk(n)
            if n<=1200 or n in [15000,25176]:
                dr=direct_risk(n)
                assert A+B*MID==dr,(n,A,B,dr)
                direct=True
            else: direct=False
            prev[n]=(A,B)
            w.writerow([n,A,B,a,i,c,j,jumps,*sums,int(direct)])
            print('CASE',n,'R=',(A,B),'i,j=',(i,j),'jumps=',jumps,'gap_counts=',sums,'direct=',direct)
    target={
        225:(-2047,7808),292:(-4928,18796),
        328:(-4928,18796),456:(-10432,39788),492:(-10432,39788),
        1106:(5505,-20992),1173:(-7091,27047),
        168319:(479873,-1830144),322176:(479873,-1830144),
        323000:(5649153,-21544832)
    }
    for n,val in target.items():
        assert prev[n]==val,(n,prev[n],val)
    # Exhaustive independent small-domain comparison. Cost n^2 log n, bounded 128..500.
    for n in range(128,501):
        (A,B),_,_,_,_=eval_risk(n)
        assert A+B*MID==direct_risk(n),(n,A,B)
    # Probe one huge n with a fully certified input Farey bracket.
    for n in [10**6,2*10**6,10**8,10**9]:
        (A,B),(a,i,c,j),steps,_,sums=eval_risk(n)
        print('LARGE',n,'R=',(A,B),'denom=',(i,j),'steps=',steps,'gap_counts=',sums)
    print('PASS_R26_FAREY_FLOORSUM_EXACT_RISK_ALL_128_500_AND_30_FRONTIER_POINTS')

if __name__=='__main__':run()
