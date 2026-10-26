#!/usr/bin/env python3
"""Portable exact certificate for BRC N=3 moment/covariance aggregation."""
from fractions import Fraction as F

Q=F

def lagrange(nodes,j):
    c=[F(1)]; den=F(1)
    for k,x in enumerate(nodes):
        if k==j: continue
        den*=nodes[j]-x
        nxt=[F(0)]*(len(c)+1)
        for i,a in enumerate(c):
            nxt[i]-=a*x; nxt[i+1]+=a
        c=nxt
    return [a/den for a in c]

def cov(w,a,b):
    return sum(u*x*y for u,x,y in zip(w,a,b))-sum(u*x for u,x in zip(w,a))*sum(u*y for u,y in zip(w,b))

def residual(y,K,w,z,b):
    m=len(y)
    assert sum(w)==1 and all(u>=0 for u in w)
    assert all(0<=u<=1 for u in z)
    assert all(sum(k)==1 and all(p>0 for p in k) for k in K)
    assert len({sum(v*p for v,p in zip(y,k)) for k in K})==1
    v=sum(u*t for u,t in zip(w,z))
    D=[b*(v*sum(w[s]*K[s][j] for s in range(len(K)))-sum(w[s]*z[s]*K[s][j] for s in range(len(K)))) for j in range(m)]
    mom=[[sum(k[j]*y[j]**h for j in range(m)) for h in range(m)] for k in K]
    C=[cov(w,z,[row[h] for row in mom]) for h in range(m)]
    rec=[-b*sum(lagrange(y,j)[h]*C[h] for h in range(2,m)) for j in range(m)]
    assert D==rec and sum(D)==0 and sum(y[j]*D[j] for j in range(m))==0
    for h in range(m): assert sum(y[j]**h*D[j] for j in range(m))==-b*C[h]
    tv=sum(abs(x) for x in D)/2
    if m==3: assert tv==b*abs(C[2])/((y[1]-y[0])*(y[2]-y[1]))
    if m==4:
        S=sum(y)
        den=lambda j: abs(__import__('math').prod(y[j]-y[k] for k in range(m) if k!=j))
        assert tv==b*sum(abs((S-y[j])*C[2]-C[3])/den(j) for j in range(m))/2
    return D,tv,C

def O(a,b,z,Y,Ka,Kb):
    # Strict-positive 12-leaf source: stage2 LR masses Q/P
    qax,pax=F(1,6),F(1,6)
    qby,pby=F(2,9),F(2,9)
    choose=(0,2)
    pdec=z*(a*pax*sum(Y[j]*Ka[j] for j in choose)+b*pby*sum(Y[j]*Kb[j] for j in choose))
    qdec=z*(a*qax*sum(Ka[j] for j in choose)+b*qby*sum(Kb[j] for j in choose))
    TP=1+F(2,3)*a+F(1,3)*b+z*(a*pax+b*pby)
    TQ=1+F(1,3)*a+F(2,3)*b+z*(a*qax+b*qby)
    return (pdec,1-qdec,TP,TQ)

def main():
    Y3=(F(1,2),F(1),F(3,2))
    Ka3=(F(1,4),F(1,2),F(1,4)); Kb3=(F(1,3),)*3
    d3,tv3,c3=residual(Y3,(Ka3,Kb3),(F(1,2),)*2,(F(1),F(0)),F(1,6))
    assert c3[2]==-F(1,96) and tv3==F(1,144)
    print('PASS ternary covariance/TV:',c3[2],tv3)
    Y=(F(1,2),F(3,4),F(5,4),F(3,2))
    Ka=tuple(F(i,16) for i in (3,6,2,5)); Kb=tuple(F(i,16) for i in (5,2,6,3))
    assert all(sum(K)==1 and sum(x*k for x,k in zip(Y,K))==1 for K in (Ka,Kb))
    assert sum(x*x*(ka-kb) for x,ka,kb in zip(Y,Ka,Kb))==0
    assert sum(x**3*(ka-kb) for x,ka,kb in zip(Y,Ka,Kb))==F(3,128)
    d4,tv4,c4=residual(Y,(Ka,Kb),(F(1,2),)*2,(F(1),F(0)),F(1))
    assert c4[2]==0 and c4[3]==F(3,512) and tv4==F(3,32)
    assert d4==[F(1,32),-F(1,16),F(1,16),-F(1,32)]
    print('PASS fourpoint covariance/TV:',c4[2],c4[3],tv4)
    # Positivity and normalization of all root, stage2, stage3 P/Q masses.
    stages=[((F(1,3),F(2,3)),(F(2,3),F(1,3))),
            ((F(1,2),F(1,2)),(F(1,4),F(3,4))),
            ((F(2,3),F(1,3)),(F(1,3),F(2,3)))]
    assert all(all(sum(v)==1 and all(0<x<1 for x in v) for v in pq) for pq in stages)
    assert all(x>0 and x*k>0 for x,k in zip(Y,Ka))
    assert all(x>0 and x*k>0 for x,k in zip(Y,Kb))
    A=O(F(1),F(0),F(1),Y,Ka,Kb)
    B=O(F(0),F(3,4),F(0),Y,Ka,Kb)
    C=O(F(1,2),F(3,8),F(1,2),Y,Ka,Kb)
    mid=tuple((x+y)/2 for x,y in zip(A,B))
    delta=tuple(x-y for x,y in zip(C,mid))
    assert A==(F(1,24),F(91,96),F(11,6),F(3,2))
    assert B==(F(0),F(1),F(5,4),F(3,2))
    assert mid==(F(1,48),F(187,192),F(37,24),F(3,2))
    assert delta==(F(1,64),-F(1,64),F(0),F(0))
    df,tvf,cf=residual(Y,(Ka,Kb),(F(1,2),)*2,(F(1),F(0)),F(1,6))
    assert tvf==F(1,64) and cf[2]==0
    print('PASS 12-leaf observer delta:',tuple(map(str,delta)),'flow TV',tvf)
    Y5=(F(1,4),F(1,2),F(1),F(3,2),F(7,4))
    K0=(F(1,5),)*5
    K1=tuple(K0[i]+F(1,40)*v for i,v in enumerate((2,-3,1,0,0)))
    K2=tuple(K0[i]+F(1,80)*v for i,v in enumerate((0,0,1,-3,2)))
    _,tv5,c5=residual(Y5,(K0,K1,K2),(F(1,2),F(1,3),F(1,6)),(F(1,3),F(1),F(1,4)),F(2,7))
    assert tv5==F(73,20160)
    print('PASS fivepoint interpolation:',tv5,'moments',tuple(map(str,c5[2:])))
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':main()
