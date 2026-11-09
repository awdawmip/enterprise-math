#!/usr/bin/env python3
"""Exact S23 circle risk certificate; no floats or external files."""
from fractions import Fraction as Q
from bisect import bisect_right
LO=Q(262204504569236716045286,10**24)
HI=Q(262204504569236716045287,10**24)
M=128; N=329
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def sub(x,y): return (x[0]-y[0],x[1]-y[1])
def val(x,t): return x[0]+x[1]*t
P=[]
for i in range(N):
    f=(i*LO)//1
    assert f==(i*HI)//1
    P.append((-f,i))
lo=[val(x,LO) for x in P]
hi=[val(x,HI) for x in P]
old=sorted(range(M),key=lambda i:lo[i])
oldphase=[lo[i] for i in old]
def gap(i,j,wrap):
    g=add(sub(P[j],P[i]),(wrap,0))
    assert 0<val(g,LO)<1 and 0<val(g,HI)<1
    return g
def full_partition(n):
    order=sorted(range(n),key=lambda i:lo[i])
    assert order==sorted(range(n),key=lambda i:hi[i])
    arcs={k:[] for k in range(M)}
    for j,i in enumerate(order):
        nxt=order[(j+1)%n]
        anchor=(bisect_right(oldphase,lo[i])-1)%M
        arcs[anchor].append((gap(i,nxt,int(j==n-1)),i,nxt))
    r=(1,0)
    for entries in arcs.values():
        mx=max(entries,key=lambda z:val(z[0],LO))[0]
        assert all(val(mx,HI)>=val(g,HI) for g,_,__ in entries)
        r=sub(r,mx)
    return r,arcs
for theta in (LO,HI):
    x=[(j*theta)%1 for j in range(225)]
    assert max(range(225),key=lambda j:x[j])==61
    d=[min((j*theta)%1,1-(j*theta)%1) for j in range(1,M)]
    assert min(d)==16-61*theta and d.index(min(d))==60
    a=164*theta-43;b=59-225*theta;delta=16-61*theta
    assert 0<a<b<delta and a+b==delta
    assert x[61]<(225*theta)%1<1
prev,arcs_prev=full_partition(225)
assert prev==(-2047,7808)
cascade=0;flat=0
for n in range(226,N+1):
    risk,arcs=full_partition(n)
    dr=sub(risk,prev)
    if n<=292:
        t=n-1;s=t-225;u=61+s;v=s
        assert 0<=v<u<M
        anchor=(bisect_right(oldphase,lo[u])-1)%M
        assert arcs_prev[anchor]==[((16,-61),u,v)], (n,arcs_prev[anchor])
        assert sorted(g for g,_,__ in arcs[anchor])==sorted([(-43,164),(59,-225)])
        assert dr==(-43,164),(n,dr)
        cascade+=1
    elif n<=328:
        t=n-1
        anchor=(bisect_right(oldphase,lo[t])-1)%M
        assert len([g for g,_,__ in arcs_prev[anchor] if g==(16,-61)])>=2
        assert dr==(0,0),(n,dr)
        flat+=1
    else:
        assert dr==(-43,164),(n,dr)
    prev,arcs_prev=risk,arcs
assert risk==(-4971,18960)
print('PASS_TRANSLATED_GAP_CASCADE_R21')
print('S23_EXACT_PARAMETER_ENDPOINTS=',LO,HI)
print('BASE_GAP=(61,0), MIN_RETURN_D=61 for j=1..127')
print('CASCADE_N=226..292; COUNT=',cascade,'; EACH_INCREMENT=-43+164theta')
print('R_N292=-4928+18796theta')
print('PLATEAU_N=293..328; COUNT=',flat,'; EACH_INCREMENT=0')
print('R_N329=-4971+18960theta')
print('FULL_EXACT_PARTITIONS_CHECKED=',N-225+1)
