#!/usr/bin/env python3
"""R143 exact interval-projection membership and residue-class thresholds.
Run: python check_r143.py 20. Only Python integers and Fraction are used.
"""
from fractions import Fraction as Q
import sys

def farey_cells(m):
    a,b,c,d=0,1,1,m
    while True:
        assert b*c-a*d==1
        yield a,b,c,d
        k=(m+b)//d
        a,b,c,d=c,d,k*c-a,k*d-b
        if a>=b: break

def all_words(m):
    out=set()
    for a,b,c,d in farey_cells(m):
        slope=Q(a*d+b*c,2*b*d)
        cuts={Q(0),Q(1)}
        cuts.update((-j*slope)%1 for j in range(1,m+1))
        cuts=sorted(cuts)
        for lo,hi in zip(cuts,cuts[1:]):
            rho=(lo+hi)/2
            w=0
            last=int(rho)
            for j in range(1,m+1):
                cur=int(rho+j*slope)
                w=(w<<1)|(cur-last)
                last=cur
            out.add(w)
    return out

def support(w,m):
    s=[0]
    for i in range(m):
        s.append(s[-1]+((w>>(m-1-i))&1))
    a,b=Q(0),Q(1)
    for i in range(m):
        for j in range(i+1,m+1):
            v=s[j]-s[i]
            a=max(a,Q(v-1,j-i))
            b=min(b,Q(v+1,j-i))
    if a>=b: return None
    u=min(Q(s[j]+1)-j*a for j in range(m+1))
    e=max(Q(s[j])-j*b for j in range(m+1))
    return a,b,u,e,s

def member(data,K):
    assert K>=2
    a,b,u,e,_=data
    A=(K-1)*a-u
    B=(K-1)*b-e
    return (A.numerator//A.denominator+1)<B

def witness(data,K):
    assert member(data,K)
    a,b,u,e,s=data
    L=K-1
    A=L*a-u
    N=A.numerator//A.denominator+1
    low=max([Q(0)]+[Q(N+sj,L+j) for j,sj in enumerate(s)])
    high=min([Q(1)]+[Q(N+sj+1,L+j) for j,sj in enumerate(s)])
    assert low<high
    theta=(low+high)/2
    w=0
    for i in range(len(s)-1):
        w=(w<<1)+(int((L+i+1)*theta)-int((L+i)*theta))
    return theta,w

def permanent(data):
    a,b,u,e,_=data
    step=a.denominator
    delta=b-a
    h=u-e
    last_bad=0
    for r in range(step):
        z=r*a-u
        f=z-(z.numerator//z.denominator)
        C=(1-f-h)/delta
        y=(C-r)/step
        L=r+step*(y.numerator//y.denominator)
        if L>=1:
            assert not member(data,L+1)
            assert member(data,L+step+1)
            last_bad=max(last_bad,L)
    return last_bad+2

def direct(K,m):
    L=K-1
    cuts={Q(0),Q(1)}
    # Critical: include L, since the leftmost prefix floor also jumps.
    for q in range(max(1,L),L+m+1):
        cuts.update(Q(i,q) for i in range(1,q))
    cuts=sorted(cuts)
    trial=cuts[:-1]+[(x+y)/2 for x,y in zip(cuts,cuts[1:])]
    out=set()
    for theta in trial:
        if not 0<theta<1: continue
        w=0
        for i in range(m):
            w=(w<<1)+int((L+i+1)*theta)-int((L+i)*theta)
        out.add(w)
    return out

def verify(max_m=20):
    comparisons=0
    for m in range(1,11):
        words=all_words(m)
        for K in range(2,33):
            predicted={w for w in words if member(support(w,m),K)}
            assert predicted==direct(K,m),(m,K,predicted^direct(K,m))
            comparisons+=1
    expected={2:2,3:3,4:4,5:7,6:9,7:16,8:19,9:29,
              10:33,12:51,15:92,18:129,20:163}
    word_checks=0
    for m in range(2,max_m+1):
        words=all_words(m)
        T=2
        maximizers=[]
        for w in words:
            data=support(w,m)
            tw=permanent(data)
            assert member(data,tw)
            if tw>2: assert not member(data,tw-1)
            theta,original=witness(data,tw)
            assert original==w and 0<theta<1
            if tw>T:
                T=tw
                maximizers=[w]
            elif tw==T:
                maximizers.append(w)
            word_checks+=1
        if m in expected: assert T==expected[m],(m,T)
        E=(m-2)*((m-1)//2)+1 if m>=5 else None
        print("R143_T",m,len(words),T,E,len(maximizers),flush=True)
    print("R143_PROJECTION_RESIDUE_PASS",comparisons,word_checks)

if __name__=="__main__":
    verify(int(sys.argv[1]) if len(sys.argv)>1 else 20)
