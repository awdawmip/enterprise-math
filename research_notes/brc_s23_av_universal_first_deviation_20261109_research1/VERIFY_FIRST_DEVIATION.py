#!/usr/bin/env python3
"""Integer-only certificates for the universal first-deviation theorem.
The strict P/Q < theta < (P+1)/Q enclosure is inherited from
enterprise-math@540863cb933fe4c5b76523c08f5379fe04b66d8f/PROOF.md.
All floor and ordering assertions below certify both interval endpoints.
"""
P=262204504569236716045286
Q=10**24

def sub(x,y):return x[0]-y[0],x[1]-y[1]
def add(x,y):return x[0]+y[0],x[1]+y[1]
def bounds(z):
    a,b=z
    return min(a*Q+b*P,a*Q+b*(P+1)),max(a*Q+b*P,a*Q+b*(P+1))
def less(x,y):
    if x==y:return False
    assert bounds(x)[1]<bounds(y)[0] or bounds(y)[1]<bounds(x)[0],(x,y)
    return bounds(x)[1]<bounds(y)[0]
def pos(z):return bounds(z)[0]>0

def t(j):
    if j==0:return (0,0)
    k=j*P//Q
    assert k==j*(P+1)//Q
    z=(k+1,-j)
    assert 0<bounds(z)[0]<bounds(z)[1]<Q
    return z

def nearest_return(d):
    k=d*P//Q
    assert k==d*(P+1)//Q
    x=(-k,d);y=(k+1,-d)
    return x if less(x,y) else y

def risk(m,L):
    n=m+L
    cuts=sorted(((t(j),j) for j in range(n)), key=lambda z:bounds(z[0])[0])
    assert all(bounds(cuts[j][0])[1]<bounds(cuts[j+1][0])[0] for j in range(n-1))
    old=[i for i,(_,j) in enumerate(cuts) if j<m]
    max_sum=(0,0)
    for ix,start in enumerate(old):
        end=old[(ix+1)%m]
        if end<=start:end+=n
        best=None
        for z in range(start,end):
            g=sub(cuts[(z+1)%n][0],cuts[z%n][0])
            if z+1==n:g=add(g,(1,0))
            if best is None or less(best,g):best=g
        max_sum=add(max_sum,best)
    out=sub((1,0),max_sum)
    assert bounds(out)[0]>=0 and bounds(out)[1]<=Q
    return out

def main():
    for m in (1,3,4,19,42,61,128,200,553,717):
        eps=None;dstar=None
        for d in range(1,m+1):
            val=nearest_return(d)
            if eps is None or less(val,eps):eps=val;dstar=d
        q=m+1
        while not less(nearest_return(q),eps):q+=1
        H=q-m
        before=risk(m,H)
        after=risk(m,H+1)
        assert before==(H*eps[0],H*eps[1]),(m,q,before)
        after_increment=sub(after,before)
        assert not less(after_increment,(0,0))
        assert less(after_increment,eps)
        assert not less(nearest_return(q),after_increment)
        print('CERT_FIRST_DEVIATION',f'm={m}',f'best_d={dstar}',
              f'q_next={q}',f'linear_through={H}',f'first_failure={H+1}',
              f'epsilon={eps}',f'first_increment={after_increment}',
              f'risk_before={before}',f'risk_after={after}',flush=True)
    print('PASS_ALL_CERTIFIED_FIRST_DEVIATIONS',flush=True)
if __name__=='__main__':main()
